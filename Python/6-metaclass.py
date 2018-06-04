class Metaclass(type):

    def __init__(cls, name, bases, dict):

        super(Metaclass, cls).__init__(name, bases, dict)

        new_origin = cls.__new__

        def new_custom(cls, *args, **kwargs):
            if cls.instance == None:
                cls.instance = new_origin(cls, *args, **kwargs)
            return cls.instance

        cls.instance = None
        cls.__new__ = staticmethod(new_custom)

class MyClass(object):

    __metaclass__ = Metaclass

    def __init__(self,val):
        self.val = val

    def __str__(self):
        return repr(self) + self.val

a = MyClass('first')
b = MyClass('second')
c = MyClass('third')

print('a: ', a)
print('b: ', b)
print('c: ', c)

print(a is b is c)
