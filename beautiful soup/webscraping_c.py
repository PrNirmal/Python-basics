# text file
# getting company links
from bs4 import BeautifulSoup
import requests

list1 = []
url = "https://www.zaubacorp.com/company-by-address/villupuram"
data = requests.get(url)
soup = BeautifulSoup(data.text, "html.parser")
soup.find_all('td a')
for link in soup.find_all('td'):
    if link.a != None:
        list1.append(link.a['href'])

# extracting data
for i in range(len(list1)):
    # print(i)
    url = list1[i]
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    thesoup = soup.find(class_="col-12").p.text
    soup = soup.h1.text
    thesoup = thesoup.lstrip(" Email ID: ")
    with open("comdata.txt", 'a+') as fp:
        fp.write(f'{i + 1}.' + "Company Name:" + soup + ",")
        fp.write("Email ID:" + thesoup + "\n")
import shutil
import os
main="C:/Users/prnir/PycharmProjects/pythonProject"
des="E:/company datas/text"
list_1=os.listdir(main)
for i in range(len(list_1)):
    if list_1[i].endswith(".txt"):
        newpath=os.path.join(main,list_1[i])
        shutil.move(newpath,des)
print("completed")


#excel
from bs4 import BeautifulSoup
import requests
import pandas as pd

# list2=["Tirunelveli"]
list2=["Tiruchirappalli"]
for num in range(len(list2)):
    print(num)
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
    doi=[]
    csta=[]
    for i in range(len(list1)):
        print(i)
        url = list1[i]
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        table = soup.find(class_='table table-striped').tbody.find_all('tr')
        the_age = table[7].find_all('p')
        thesoup = soup.find(class_="col-12").p.text
        the_act = table[1].find_all('p')
        the_sta = the_act[1].find('span').text
        name.append(soup.h1.text)
        mail.append(thesoup.lstrip(" Email ID: "))
        doi.append(the_age[1].text)
        csta.append(the_sta)
    print("data saved")
    thedatas = pd.DataFrame({'Company': name, 'Email': mail,'Date of Incoporation':doi,'Company Status':csta})
    writer = pd.ExcelWriter(f'{list2[num]}'+'.xlsx', engine='xlsxwriter')
    thedatas.to_excel(writer, index=False)
    writer.close()
    print("the end")
print("fully completed")
# import shutil
# import os
# main="C:/Users/prnir/PycharmProjects/pythonProject"
# des="E:/company datas/excel"
# list_1=os.listdir(main)
# for i in range(len(list_1)):
#     if list_1[i].endswith(".xlsx"):
#         newpath=os.path.join(main,list_1[i])
#         shutil.move(newpath,des)





import requests
from bs4 import BeautifulSoup
url="https://www.zaubacorp.com/company-by-address/ariyalur"
list1 = []
data = requests.get(url)
soup = BeautifulSoup(data.text, "html.parser")
soup.find_all('td a')
for link in soup.find_all('td'):
    if link.a != None:
        list1.append(link.a['href'])
print("initially saved")
# extracting data
csta=[]
for i in range(len(list1)):
    print(i)
    url = list1[i]
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    table = soup.find(class_='table table-striped').tbody.find_all('tr')
    the_act = table[1].find_all('p')
    the_sta = the_act[1].find('span').text
    if the_sta != None:
        csta.append(the_sta)
    else:
        csta.append('-')
print("data saved")
    # thedatas = pd.DataFrame({'Company': name, 'Email': mail,'Date of Incoporation':doi})
    # writer = pd.ExcelWriter(f'{list2[num]}'+'.xlsx', engine='xlsxwriter')
    # thedatas.to_excel(writer, index=False)
    # writer.close()
    # print("the end")
print("fully completed")
