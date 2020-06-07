.. title: Obtener clase original cuando hay herencia

Si usamos herencia normal de modelos (no abstracta), se vuelve difícil obtener el objeto original de la base de datos cuando sólo tenemos una referencia a un ancestro (esto pasa a menudo cuando tenemos relaciones a un modelo que fue derivado). Este cacho de código define una clase abstracta ``SubclassedModel``, cuyos descendientes tienen en ``objects`` un Manager por defecto que devuelve directamente objetos de la clase con la que fueron creados.

.. code-block:: python

    from django.db import models
    from django.db.models.query import QuerySet
    from django.contrib.contenttypes.models import ContentType


    def _as_original_class(inst):
        """
        Returns the instance that corresponds to `inst`
        in its original class.
        """
        model = inst.content_type.model_class()
        if (model == inst.__class__):
            return inst
        return model.objects.get(id=inst.id)


    class OriginalClassQuerySet(QuerySet):
        """
        A QuerySet that returns original classes.
        """
        def __getitem__(self, k):
            result = super(OriginalClassQuerySet, self).__getitem__(k)
            if isinstance(result, models.Model):
                return _as_original_class(result)
            else:
                return result

        def __iter__(self):
            for item in super(OriginalClassQuerySet, self).__iter__():
                yield _as_original_class(item)


    class OriginalClassManager(models.Manager):
        """
        A Manager that fetches original classes.
        """
        def get_query_set(self):
            return OriginalClassQuerySet(self.model)


    class SubclassedModel(models.Model):
        content_type = models.ForeignKey(ContentType, editable=False, null=True)
        objects = OriginalClassManager()

        class Meta:
            abstract = True

        def save(self, *args, **kwargs):
            if(not self.content_type):
                self.content_type = \
                    ContentType.objects.get_for_model(self.__class__)
                super(SubclassedModel, self).save(*args, **kwargs)


Para usarlo, supongamos el siguente ``models.py`` en la app ``example``:

.. code-block:: python

    from django.db import models
    from <el módulo de arriba> import SubclassedModel

    class Foo(SubclassedModel):
        [...]
        def __unicode__(self):
            return "A Foo"

    class Bar(Foo):
        [...]
        def __unicode__(self):
            return "A Bar"

    class Baz(Foo):
        [...]
        def __unicode__(self):
            return "A Baz"


Entonces:

.. code-block:: bash

    $ django-admin.py shell --settings=<nombre del proyecto>.settings
    Python 2.6.5 (r265:79063, Apr 16 2010, 13:09:56)
    [GCC 4.4.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> from example import models
    >>> bar_instance = models.Bar([...])
    >>> bar_instance.save()
    >>> baz_instance = models.Baz([...])
    >>> baz_instance.save()
    >>> foo_instance = models.Foo([...])
    >>> foo_instance.save
    >>> l = models.Foo.objects.all()
    >>> l
    [<A Bar>, <A Baz>, <A Foo>]


OJO: este mecanismo deshabilita el feature de Django según el cual un modelo no tiene un Manager por defecto cuando tiene cualquier Manager explícito. Se me ocurre que eso puede romper algo en subclases de ``SubclassedModel`` si uno no lo tiene en cuenta.

.. _bar: /ListaDeCorreo/bar
.. _foo: /foo
