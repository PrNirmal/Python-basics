# In Python, the term monkey patch refers to dynamic (or run-time) modifications of a class or module.
# In Python, we can actually change the behavior of code at run-time.

def themain():
    print("this is in the mainfunc")
def thesec():
    print("the second")

a=themain
a()
themain=thesec
themain()
