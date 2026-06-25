# time.time() and time.ctime()
import time

seconds = time.time()  # returns the number of seconds passed since epoch.
# For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point where time begins)
print("Seconds since epoch =", seconds)
time.ctime(seconds)  # seconds passed since epoch as an argument and returns a string representing local time.

# time.sleep()
import time

print("This is printed immediately.")
time.sleep(4)  # delays execution of the current thread for the given number of seconds.
print("This is printed after 4 seconds.")

print("it executes immediately")
time.sleep(3)
print("this will execute after 3 sec")

# time.localtime()
import time

a = time.time()
b = time.localtime(a)
b.tm_min
b.tm_hour
b.tm_wday  # for days(0-6) 0 for monday

# time.gmtime()
import time

x = time.time()
y = time.gmtime(x)  # return im struct_time format and in utc (i.e coordinated universal time) for india +5:30
y.tm_year
y.tm_min

# time.mktime()
import time

t = (2022, 11, 6, 13, 20, 22, 5, 310, 0)  # takes struct_time as an argument
local = time.mktime(t)  # this is reverse of lotime function

# comparison
import time

second = 1667722171
print(second)
local_time = time.localtime(second)
print(local_time)
new_seconds = time.mktime(local_time)
print(new_seconds)

# time.asctime
import time  # takes the struct_time as an argument

t = (2022, 11, 6, 13, 20, 22, 5, 310, 0)
result = time.asctime(t)
print(result)
second = time.time()
loca = time.localtime(second)
timm_1 = time.asctime(loca)
print(timm_1)

# time.strftime()
import time

named_tuple = time.localtime()  # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)  # m-month,d-date,Y-year,H-hour,M-minute,S-second
print(time_string)

# time.strptime()
import time

time_string = "21 May, 2018"
result = time.strptime(time_string, "%d %B, %Y")

print(result)

import time as t
l=t.time()
t.ctime(l)