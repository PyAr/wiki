Como colaborar en el Wiki de Pyar
=================================

.. todo:: Sacar esto de moin-moin y poner lo que corresponda

Primeros Pasos
~~~~~~~~~~~~~~

 * Registrarse en el wiki!
 * Completar tu pagina personal (es opcional pero muy recomendado)
 * Si no queres responder 500 veces de que color es el caballo blanco de san martín podes pedirle a algun admin, o en la lista, que te agregen al ReadWriteGroup

Colaborando con Código
~~~~~~~~~~~~~~~~~~~~~~

* Podes agregar tus recetas en el [[Recetario | Recetario]]

Tenemos Instalado Pygments, asi que podes colorear tu codigo con:

::

    #!code moin
    {{{
    #!code python
    print "Hola Mundo"
    }}}

Y queda:

::
    
    {{{
    #!code python
    print "Hola Mundo"
    }}}

Ademas de colorear python, colorea el lenguaje que quieras... incluso java

Como agregar mails de forma un poco mas segura
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando Agregamos direcciones de mail conviene usar el macro MailTo, que evita que los mails queden en plano en el wiki (cuando ponemos mails que no son nuestros)


::
    
    {{{
    #!code moin
    <<MailTo(joac ARROBA NO QUIERO SPAM algundominio GUION otrodominio PUNTO com)>>   
    }}}

Y queda:
<<MailTo(joac ARROBA NO QUIERO SPAM algundominio GUION otrodominio PUNTO com)>> 


Mas Funcionalidades Copadas
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mapas
++++


::
    
    {{{
    #!code moin
    <<GoogleMaps(msa=0,msid=117626973029192648931.000447d968ea4d494125a,t="h",ll="-39.774769,-57.216797",spn="40.500047,77.607422",z=4)>>   
    }}}


    <<GoogleMaps(msa=0,msid=117626973029192648931.000447d968ea4d494125a,t="h",ll="-39.774769,-57.216797",spn="40.500047,77.607422",z=4)>>

Twitter
+++++++

::
    
    {{{
    #!code moin
    <<Twitter(usuario="pyconar")>>
    }}}

    <<Twitter(usuario="pyconar")>>

Restructured Text
+++++++++++++++++

::

    {{{{
    #!code moin
    {{{
    #!rst

    ========================
    Restructured Text
    ========================

    Otro Título
    ===========
    **Algo En Negrita**
    }}}
    }}}}
    {{{
    #!rst

    ========================
    Restructured Text
    ========================

    Otro Título
    ===========
    **Algo En Negrita**

    }}}

Video HTML 5
++++++++++++

::

    {{{
    #! moin
    <<Video(http://pyar.usla.org.ar/charlasabiertas2010/intro_python.ogg)>>
    }}}
    <<Video(http://pyar.usla.org.ar/charlasabiertas2010/intro_python.ogg)>>

Figuras
+++++++

::
    
    {{{{
    !#code moin
    {{{#!aafig aspect=0.5 scale=2
            ddddddddd
            dd  ddddddddd
            ddddddddddddd 
            ddddddddddddd
    dddddddddddddddddddd eeeeee
    dddddddddddddddddddd  eeeeeee
    dddddddd             eeeeeeee
    ddddddd  eeeeeeeeeeeeeeeeeeee
    dddddd eeeeeeeeeeeeeeeeeee
            eeeeeeeeeeeee
            eeeeeeeeeeeee
            eeeeeeeee  ee  
            eeeeeeeeee

    }}}

    }}}}


    {{{#!aafig aspect=0.5 scale=2

            ddddddddd
            dd  ddddddddd
            ddddddddddddd 
            ddddddddddddd
    dddddddddddddddddddd eeeeee
    dddddddddddddddddddd  eeeeeee
    dddddddd             eeeeeeee
    ddddddd  eeeeeeeeeeeeeeeeeeee
    dddddd eeeeeeeeeeeeeeeeeee
            eeeeeeeeeeeee
            eeeeeeeeeeeee
            eeeeeeeee  ee  
            eeeeeeeeee

    }}}
