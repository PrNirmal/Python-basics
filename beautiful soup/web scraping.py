import requests
from bs4 import BeautifulSoup

url = "https://filesamples.com/formats/pdf"
des = "https://filesamples.com"
data = requests.get(url)
count = 1
soup = BeautifulSoup(data.text, 'html.parser')
for link in soup.find_all('a', class_="btn"):
    new = des + link["href"]
    path = requests.get(new)
    with open(f'file{count}.pdf', 'wb') as fp:
        fp.write(path.content)
    count += 1

# problem 2:
import requests
from bs4 import BeautifulSoup

url = "https://economictimes.indiatimes.com/wealth/fuel-price/diesel"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
data = soup.find(id="mainPage")
for i in data.findAll('span', 'fPrice'):
    print(i.text)

# problem 3:
import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/forms/d/1AEdsd1X9qswONsd1uxMIUwBkHyKASt0ZubJnzYPkp0w/edit#responses"
data = requests.get(url)
soup = BeautifulSoup(data.text, "html.parser")
print(soup.prettify())
soup.find("span")

# eg :
a = [11, 2, 3]
b = [11, 2, 3]
# b=a
if a is b:
    print("yes")
else:
    print("nope")

import copy

a = ["string", 2]
b = copy.copy(a)
a[0] = [1, 2]
id(a[0])
id(b[0])

# shallow copy :
# changes the surface things in nested list

help('keyword')

from bs4 import BeautifulSoup
import requests

url = "https://www.zaubacorp.com/charges"
data = requests.get(url)

soup = BeautifulSoup(data.text, "html.parser")
soup.prettify()
print(soup.title)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.title.name)
print(soup.p)
print(soup.find_all('p'))
print(soup.p['class'])
print(soup.find_all(id='drop-it'))
print(soup.get_text())

with open("E:\webDesign\project_3\index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
print(soup)
soup = BeautifulSoup("<html>a web page</html>", "html.parser")
print(soup)

url = "https://www.zaubacorp.com/company-by-address/villupuram"
data = requests.get(url)
soup = BeautifulSoup(data.text, "html.parser").find_all('td')
soup = BeautifulSoup(data.text, "html.parser").string
# soup['class']
soup.attrs['id'] = 1
del soup['id']
soup.get('id')

doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
doc.find(text="INSERT FOOTER HERE").replace_with(footer)
# 'INSERT FOOTER HERE'
print(doc)
# <?xml version="1.0" encoding="utf-8"?>
# <document><content/><footer>Here's the footer</footer></document>
# Since the BeautifulSoup object doesn’t correspond to an actual HTML


# text file
# getting company links
from bs4 import BeautifulSoup
import requests



list1 = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
url = "https://www.zaubacorp.com/company-by-address/villupuram"
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, "html.parser")
soup.find_all('td a')
for link in soup.find_all('td'):
    if link.a != None:
        list1.append(link.a['href'])

# extracting data
for i in range(len(list1)):
    # print(i)
    url = list1[i]
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    thesoup = soup.find(class_="col-12").p.text
    soup = soup.h1.text
    thesoup = thesoup.lstrip(" Email ID: ")
    with open("comdata.txt", 'a+') as fp:
        fp.write(f'{i + 1}.' + "Company Name:" + soup + ",")
        fp.write("Email ID:" + thesoup + "\n")

# excel

from bs4 import BeautifulSoup
import requests
import pandas as pd

list2 = ['cuddalore', 'villupuram','chidambaram']
for num in range(len(list2)):
    url = "https://www.zaubacorp.com/company-by-address/" + f'{list2[num]}'
    list1 = []
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    soup.find_all('td a')
    for link in soup.find_all('td'):
        if link.a != None:
            list1.append(link.a['href'])
    print("initially saved")
    # extracting data
    name = []
    mail = []
    for i in range(len(list1)):
        # print(i)
        url = list1[i]
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        thesoup = soup.find(class_="col-12").p.text
        name.append(soup.h1.text)
        mail.append(thesoup.lstrip(" Email ID: "))
    print("data saved")
    thedatas = pd.DataFrame({'Comapany': name, 'Email': mail})
    writer = pd.ExcelWriter(f'{list2[num]}'+'.xlsx', engine='xlsxwriter')
    thedatas.to_excel(writer, index=False)
    writer.close()
    print("the end")
import shutil
import os
main="C:/Users/prnir/PycharmProjects/pythonProject"
des="E:/company datas"
list_1=os.listdir(main)
for i in range(len(list_1)):
    if list_1[i].endswith(".xlsx"):
        newpath=os.path.join(main,list_1[i])
        shutil.move(newpath,des)


import pandas as pd

# dataframe Name and Age columns
df = pd.DataFrame({'Name': ['A', 'B', 'C', 'D'],
                   'Age': [10, 0, 30, 50]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.close()

