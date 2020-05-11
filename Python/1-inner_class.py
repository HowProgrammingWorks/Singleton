class Singletone:

    class __Singletone:
        def __init__(self, arg):

            self.val = arg
        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):
        if not Singletone.instance:
            Singletone.instance = Singletone.__Singletone(arg)
        else:
            Singletone.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)


a = Singletone('first')
print(a)
b = Singletone('second')
print(b)
c = Singletone('third')
print('a: ', a)
print('b: ', b)
print('c: ', c)
