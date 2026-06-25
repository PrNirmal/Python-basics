help('raise')
try:
        print(1/0)
except Exception as exp:
    raise Exception("my own exception")

help('assert')
assert True, "printed"
# assert False, 'not printed'#if the executed line,False then the next line will not be executed
# assert 5>8, 'printed'

help('nonlocal')
x='nirmal'
def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x #it will not set the variable global
    x = "hello"
  myfunc2()
  return x

print(myfunc1())