# typecasting
str(23.2)
float(87)
int(3.4)
tuple({1,2,3,4})#tuple of set=tuple
tuple(dict({'2':4}))#tuple of dict =keys
tuple('str')#tuple of str=tuple
list(zip({1,2},{4,5}))#list of zip=list   (DOUT in zip)
dict(zip({1,2},{4,5}))#dict of zip=dict
set([6,7])#set of list=set
#
# numbers,casting,booleans,operators
# int,float,complex
x=2
y=2.7
z=2j
print(type(x))
print(type(y))
print(type(z))
# type conversion
x=2
y=2.7
z=2j
print(float(x))
print(int(y))
print(complex(x))# print(int(z)) can"t convert compelx into int
# casting
x=str(2)
y=float(1)
z=int(2.8)
print(x)
print(y)
print(z)
#
import  pip
locals()
globals()
import bs4
#
import requests
from bs4 import BeautifulSoup
# url="http://samples/document/pdf/sample3.pdf"
# url="https://filesamples.com/formats/pdf"
url='https://filesamples.com/samples/document/pdf/sample3.pdf'
# def pdf(url):
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
links=soup.find_all('a')
i=0
for link in links:
    if('.pdf' in link.get('href',[])):
        i +=1
        print("downloading file:",i)
        response=requests.get(link.get('href'))
        pdf=open("pdf"+str(i)+".pdf",'wb')
        pdf.write(response.content)
        pdf.close()
        print("file",i,"downloaded")
print("all pdf files downloaded")



