class SingletoneDict:

    _state_dict = {}

    def __init__(self):
        self.__dict__ = self._state_dict


class Singletone(SingletoneDict):

    def __init__(self, arg):
        SingletoneDict.__init__(self)
        self.val = arg

    def __str__(self): 
    	return self.val


a = Singletone('first')
print(a)
b = Singletone('second')
print(b)
c = Singletone('third')
print('a: ', a)
print('b: ', b)
print('c: ', c)
