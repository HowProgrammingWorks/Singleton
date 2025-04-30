class Singletone(object):

    __instance = None

    def __new__(cls, val):
        if Singletone.__instance is None:
            Singletone.__instance = object.__new__(cls)
        Singletone.__instance.val = val
        return Singletone.__instance


a = Singletone('first')
print(a)
b = Singletone('second')
print(b)
c = Singletone('third')
print('a: ', a)
print('b: ', b)
print('c: ', c)
