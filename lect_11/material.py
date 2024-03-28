### CASE 7
import time

def decorator_1(my_function):
    def wrapper(*args):
        current_time = time.time()
        rez = my_function(*args)
        delta_time = time.time() - current_time
        print(f'Час виконання: {delta_time}')
        # print(rez)
        # return rez
    return wrapper

@decorator_1
def list_gen(a, b):
    lst = []
    for i in range(a, b):
        i += 1
        lst.append(i)
    print('DONE')
    return lst

# list_gen(0, 30000000)
### CASE 8
def num_decorator(n):
    def decorator_1(function):
        def wrapper(*args):
            stars = (n * "*")
            result = function(*args)
            result = stars, result, stars
            return result

        return wrapper
    return decorator_1


@num_decorator(25)
def calculate(a, b):
    return (a+b) * 2

print(calculate(2, 25))




## functools
### CASE 9
from functools import partial

def myltipleText(myStr, n):
    return myStr*n

doubleMyltipleText = partial(myltipleText, 2)
tripleMyltipleText = partial(myltipleText, 3)
print(doubleMyltipleText("Python")) #PythonPython
print(tripleMyltipleText("Python")) #PythonPythonPython

## CASE 10
from functools import reduce

numbers = [1, 2, 3, 4, 5]

def mySum(x, y):
    return x+y


result1 = reduce(mySum, numbers)
print(f"sum is {result1}") #15
result2 = reduce(mySum, numbers, 10)
print(f"sum is {result2}") #15

#######
### TUPLE
myEmptyTuple1=()
myEmptyTuple2= tuple()

print(myEmptyTuple1)
print(type(myEmptyTuple1))
print(myEmptyTuple1)
print(type(myEmptyTuple2))

myTuple1 = ('element1', 12, 35.6, False)
myTuple2 = ('item1')
myTuple3 = ('item1',)

print("myTuple1:", myTuple1, "type: ", type(myTuple1))
print("myTuple2:", myTuple2, "type: ", type(myTuple2))
print("myTuple3:", myTuple3, "type: ", type(myTuple3))

userTypes = 'admin', 'student', 'teacher'
userName = 'Jane',

print("userTypes:", userTypes, "type: ", type(userTypes))
print("userName:", userName, "type: ", type(userName))

userTypes=('admin','student','teacher','moderator')
# userTypes[0]='user' # !!!!!! error !!!!!!!!
### BUT!1!!!!

tup1 = ('user', 555, [1, 2])
print(tup1)
tup1[2][0] = 9999
print(tup1)

### set
set_1 = set((1, 2))
set_2 = {1, 2}
print(type(set_1))
print(type(set_2))


