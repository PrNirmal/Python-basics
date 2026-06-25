# factorial:
def fact(x):
        if x==1:
                return 1
        else:
                fact_1=x*fact(x-1)
        return fact_1
fact(5)

#fibbonacci

def fibbo(x):
        if x==0:
                return 0
        elif x==1:
                return 1
        else:
                return (fibbo(x-2))+(fibbo(x-1))

x=9
for i in range(x):
        if i<x-2:
                print(fibbo(i),end="+")
        elif(i==x-2):
                print(fibbo(i),end="=")
        else:
               print(fibbo(i))