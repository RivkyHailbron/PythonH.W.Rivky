import time
from time import sleep
from functools import  wraps
#1
def run_time(func):
    @wraps(func)
    def wrapper(*arg, **kwargs):
        print("start run time")
        start = time.time()
        sleep(0.5)
        func(*arg,**kwargs)
        end= time.time()
        print(f"run time: {end-start}")
        print("end run time")
    return  wrapper



@run_time
def f1():
    print("ggggggggggg")
    print("jjjjjjjjjjj")

f1()

#2
def cache(func):
    cache_dict = {}
    @wraps(func)
    def wrapper(*args):
        print("start cache")

        if args in cache_dict:  # אם התוצאה כבר מחושבת, נחזיר מהמטמון
            # print("Returning cached result")
            return cache_dict[args]

        result = func(*args)  # אחרת, נחשב את התוצאה ונשמור אותה
        cache_dict[args] = result
        print("end cache")
        return result


    return wrapper
# @run_time
@cache
def fibonacci(n):
    if n==1 or n==2:
        return 1
    a = 1
    b = 1
    for _ in range(n-2):
        c = a+b
        a = b
        b = c
    return c


print(fibonacci.__name__)
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))