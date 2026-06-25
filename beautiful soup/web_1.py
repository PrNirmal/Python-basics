# from bs4 import BeautifulSoup
# import requests
# import pandas as pd

# a_tag1=[]
# for i in range(1,184):
#     url="https://www.veethi.com/places/cuddalore-district_yellowpages_list-23&page-"+f'{i}.htm'
#     # url="https://www.veethi.com/places/cuddalore-district_yellowpages_list-23&page-1.htm"
#     datas=requests.get(url)
#     soup1=BeautifulSoup(datas.text,"html.parser")
#     for link in soup1.find_all(class_="list_view"):
#         if link.a!=None:
#             # print(str(link.a['href']))
#             x='https://www.veethi.com'+link.a['href']
#             a_tag1.append(x)
#     print(i)
# print('completed')

# # extracting data
# names=[]
# number=[]
# for j in range(len(a_tag1)):
#     url1=a_tag1[j]
#     data_re=requests.get(url1)
#     soup2=BeautifulSoup(data_re.text,'html.parser')
#     # name=soup2.h1.text
#     # names.append(name)
#     if(soup2.find('span',class_='mobile')):
#         num=soup2.find('span',class_='mobile').text.strip()
#     elif(soup2.find('span', class_='phone')):
#         num = soup2.find('span', class_='phone').text.rstrip()
#     else:
#         num='-'
#     number.append(num)
#     print(number)
#     print(j)
# print('datas completed')

# # excel
# df=pd.DataFrame({'Company':names,'Number':number})
# ex_writer=pd.ExcelWriter('Cuddalore.xlsx',engine='xlsxwriter')
# df.to_excel(ex_writer,index=False)
# ex_writer.close()
# print('completed')
# a_tag1.remove('https://www.veethi.com/icici-bank-ltd-virudhachalam\xa0/YP189640')
# len(names)
# len(number)





from bs4 import BeautifulSoup
import requests
from pathlib import Path

url=requests.get("https://www.carwale.com/hyundai-cars/venue/")

soup=BeautifulSoup(url.content,"html.parser")

# title_text=soup.title.text

# title1=soup.find("h2")
# price=soup.find("span",class_="o-j4 o-jk o-js o-jJ").text
# print(title1.text, price)


tbody=soup.find("tbody")
table_rows=tbody.find_all("tr")
images_dir = Path("images")
images_dir.mkdir(exist_ok=True)

for row in table_rows:
    data_list=row.find_all("td")
    model_name = data_list[0].a.text.strip()
    print(f"model={model_name}, ,price={data_list[1].span.text}")
    link=f'https://www.carwale.com{data_list[0].a["href"]}'
    url_2=requests.get(link)
    soup_2=BeautifulSoup(url_2.content,"html.parser")
    image_tag = soup_2.find("img", class_="o-D o-hP o-iB o-iT o-G o-Q o-a0 o-aa o-hl o-ed")
    if image_tag:
        image_src = image_tag.get("data-src") or image_tag.get("src")
        if image_src:
            image_response = requests.get(image_src)
            if image_response.status_code == 200:
                safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in model_name)
                image_path = images_dir / f"{safe_name}.jpg"
                with open(image_path, "wb") as image_file:
                    image_file.write(image_response.content)
                print(f"Saved image: {image_path}")
            else:
                print(f"Failed to download image for {model_name}: HTTP {image_response.status_code}")
        else:
            print(f"No image source found for {model_name}")
    else:
        print(f"No image tag found for {model_name}")
    # print(f"Its variant is {len(soup_2.find("tbody").find_all("tr"))}")
    # link=data_list[0].a.get("href")


