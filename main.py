def staa(func):
    def inner(*args, **kwargs):
        print('decorator working')
        fun = func(*args, **kwargs)
        print('decorator worked')
        return  fun
    return inner

class Mathematics:
    @staa
    def addNumbers(self,x, y):
        return x + y

# create addNumbers static method
@staa
def cla():
    pass


