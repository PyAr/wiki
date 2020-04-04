.. title: Un ejemplo de class decorators (python 3)


.. code-block:: python

    class LimitExceededException(Exception):
        pass

    class limit_instances:
        def __init__(self, limit):
            self.limit = limit

        def __call__(self, cls):
            prev_new = cls.__new__
            cls.__num = 0
            def __new__(cls, *a, **kw):
                cls.__num += 1
                if cls.__num > self.limit:
                    raise LimitExceededException()
                return prev_new(cls, *a, **kw)
            cls.__new__ = __new__
            return cls

    @limit_instances(5)
    class C:
        pass

    for n in range(10):
        c=C()
        print(c)
