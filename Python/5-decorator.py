class SingletoneDecorator:

    def __init__(self, arg_class):
        self.arg_class = arg_class
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.arg_class(*args, **kwargs)
        return self.instance

class MyClass: 
	pass


MyClass = SingletoneDecorator(MyClass)

a = MyClass()
b = MyClass()
c = MyClass()

a.val = 'first'
b.val = 'second'
c.val = 'third'

print(a.val)
print(b.val)
print(c.val)

print(a is b is c)
