class Singletone(object):

    class __Singletone:
        def __init__(self):
            self.val = None

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __new__(cls):
        if not Singletone.instance:
            Singletone.instance = Singletone.__Singletone()
        return Singletone.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
        

a = Singletone()
a.val = 'first'
print(a)

b = Singletone()
b.val = 'second'
print(b)

c = Singletone()
c.val = 'third'

print('a: ', a)
print('b: ', b)
print('c: ', c)
