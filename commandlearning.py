import sys

arg = sys.argv
print(arg)
a = int(arg[1])# by default cmd argument is passed as string so we declaring a int
b = int(arg[2])


def sq(a, b):
    return a + b

print(sq(a, b))

