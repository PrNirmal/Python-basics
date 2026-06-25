# decorators
#1.
def mess(sub):
    print(sub)
mess("hello")
cont=mess
cont("bye")

#2.
def result():
    def result2():
        print("hello")
    return result2
main_result=result()
main_result()

#3.
def outer(func):
    def inner():
        print("start of decorator")
        func()
    return inner
def thepart():
    print("end of decorator")
thepart2=outer(thepart)
thepart2()

# or

@outer
def thepart():
    print("end of decorator")
thepart()

# division problem using decorators
# decoration function with paramenters
#4.
def thedivide(func):
    def inner(a,b):
        print("gonna divide ",a," and ",b)
        if b==0:
            print("cant able to divide")
            return
        return func(a,b)
    return inner

@thedivide
def main_div(a,b):
    print(a/b)

import time
start = time.time()
main_div(5,2)
end = time.time()
print("the time taken ",end-start)
