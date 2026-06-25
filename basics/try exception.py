#try exception
try:
    # import requests
    import requestss
except ImportError as e:
    if str(e)=="No module named 'requestss'":
        print("no module")
    print(e)
except ZeroDivisionError:
    print( "zero")
#
try:
    # a=10/5
    a = 1/0
except Exception as e:
    print(e)
# except ZeroDivisionError:
#     print( "zero")
else:
    print('else')
finally:
    print('finally')

#
try:
    a=1/0
# except ImportError as e:
except Exception as e:
    if str(e)=="division by zero":
        print("zero error")
    print(e)
except ZeroDivisionError:
    print( "zero")
#
try:
    # print(kavya)
    import requestss
except:
    print('nothing')