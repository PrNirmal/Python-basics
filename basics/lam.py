#lamnbda function
#Syntax
#lambda arguments : expression

add = lambda a, b: a + b
print(add(5,3))

sub = lambda x, y: x - y
print(sub(4,6))

square = lambda x: x * x
print(square(4))

even_odd = lambda n: "Even" if n%2==0 else "Odd"
print(even_odd(3))

div = lambda a, b: a/b
print(div(10,2))

multi = lambda a, b: a * b
print(multi(7, 4))

#map 

numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)

#filter

numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)


def Calculator(a, b):
    
    Add = lambda: a + b
    Sub = lambda: a - b
    Mul = lambda: a * b
    Div = lambda: a / b

    print("addition:", Add())
    print("subtraction:", Sub())
    print("multiplication:", Mul())
    print("division:", Div())


# Function call
Calculator(10, 5)

def Calculator(a, b):
    print("addition:", (lambda x, y: x + y)(a, b))
    print("subtraction:", (lambda x, y: x - y)(a, b))
    print("multiplication:", (lambda x, y: x * y)(a, b))
    print("division:", (lambda x, y: x / y)(a, b))


Calculator(10, 5)

numbers = [5, 2, 8, 1, 3]
result = sorted(numbers, key =lambda x: x)
print(result)

numbers = [5, 2, 8, 1, 3]
result = sorted(numbers, key =lambda x: x, reverse = False)
print(result)


