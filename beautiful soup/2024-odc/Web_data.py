import pandas as pd
def merge_multiple_excel_files(file_list, output_file):
    # Create an empty list to store dataframes
    dataframes = []

    # Loop through each file in the list
    for file in file_list:
        # Read each Excel file and append to the list
        data = pd.read_csv(file)
        dataframes.append(data)

    # Concatenate all dataframes into a single dataframe
    merged_data = pd.concat(dataframes, ignore_index=True)

    # Save the merged dataframe to a new Excel file
    merged_data.to_excel(output_file, index=False)
    print(f"Merged file saved as {output_file}")


# Example usage
file_list = [
    r"C:\Users\prnir\PycharmProjects\NGO_Data of State- TELANGANA, from 1 to 902.csv",
    r"C:\Users\prnir\PycharmProjects\NGO_Data of State- TELANGANA, from 681 to 902.csv",
    r"C:\Users\prnir\PycharmProjects\NGO_Data of State- TELANGANA, from 848 to 902.csv",
]
output_file = "Telangana-NGO.xlsx"  # Replace with your desired output file name

merge_multiple_excel_files(file_list, output_file)

import pandas as pd
import numpy as np
import urllib.request
from bs4 import BeautifulSoup
import requests
import json
import re

main = {'ANDAMAN & NICOBAR ISLANDS': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/113/35/{}',
 'ANDHRA PRADESH': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/3914/28/{}',
 'ARUNACHAL PRADESH': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/389/12/{}',
 'ASSAM': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/1793/18/{}',
 'BIHAR': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/3496/10/{}',
 'CHANDIGARH': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/178/4/{}',
 'CHHATTISGARH': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/1517/22/{}',
 'DADRA & NAGAR HAVELI': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/24/26/{}',
 'DAMAN & DIU': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/15/25/{}',
 # 'DELHI': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/7865/7/{}',
 'GOA': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/209/30/{}',
 'GUJARAT': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/5010/24/{}',
 'HARYANA': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/2223/6/{}',
 'HIMACHAL PRADESH': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/620/2/{}',
 'JAMMU & KASHMIR': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/1235/1/{}',
 'JHARKHAND': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/1746/20/{}',
 # 'KARNATAKA': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/5827/29/{}',
 # 'KERALA': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/3037/32/{}',
 'LADAKH': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/144/37/{}',
 'LAKSHADWEEP': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/2/31/{}',
 'MADHYA PRADESH': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/5230/23/{}',
 'MAHARASHTRA': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/13933/27/{}',
 'MANIPUR': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/2064/14/{}',
 'MEGHALAYA': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/234/17/{}',
 'MIZORAM': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/196/15/{}',
 'NAGALAND': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/352/13/{}',
 'ORISSA': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/3137/21/{}',
 # 'PUDUCHERRY': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/248/34/{}',
 'PUNJAB': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/1307/3/{}',
 'RAJASTHAN': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/3911/8/{}',
 'SIKKIM': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/91/11/{}',
 # 'TAMIL NADU': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/7287/33/{}',
 # 'TELANGANA': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/2301/36/{}',
 'TRIPURA': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/397/16/{}',
 'UTTAR PRADESH': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/14418/9/{}',
 'UTTARAKHAND': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/1500/5/{}',
 'WEST BENGAL': 'https://ngodarpan.gov.in/index.php/home/statewise_ngo/7900/19/{}'}

state = input('Enter state').upper()

def get_token(sess):
    req_csrf = sess.get('https://ngodarpan.gov.in/index.php/ajaxcontroller/get_csrf')
    print("CSRF response:", req_csrf.text)  # Debugging line
    if req_csrf.status_code == 200:
        try:
            return req_csrf.json()['csrf_token']
        except (KeyError, json.JSONDecodeError):
            raise ValueError("Failed to fetch a valid CSRF token.")
    else:
        raise ConnectionError(f"Failed to fetch CSRF token. Status code: {req_csrf.status_code}")

url = main[state]
detail_url = 'https://ngodarpan.gov.in/index.php/ajaxcontroller/show_ngo_info'

sess = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
sess.headers.update(headers)

first = int(input('Enter starting page: '))
last = int(input('Enter ending page: '))
lis = []

# import time
sum=2341
for i in range(first, last + 1):
    print(sum)
    sum+=1
    html = urllib.request.urlopen(url.format(i)).read()
    soup = BeautifulSoup(html, 'html.parser')  # Specify parser explicitly
    table = soup.find_all('table')
    if not table:
        print(f"No table found on page {i}")
        continue
    all_a = table[0].find_all('a')
    for j in range(len(all_a)):
        file = {}
        link_match = re.findall(r"show_ngo_info\(\"([^\"]+)\"\);", all_a[j].get('onclick', ''))
        if not link_match:
            print(f"Failed to extract link for element: {all_a[j]}")
            continue
        link = link_match[0]

        response = sess.post(
            detail_url,
            headers={'X-Requested-With': 'XMLHttpRequest'},
            data={'id': link, 'csrf_test_name': get_token(sess)}
        )
        if response.status_code != 200:
            print(f"Failed request for link {link}. Status code: {response.status_code}, response: {response.text}")
            continue
        try:
            req_details = response.json()
        except json.JSONDecodeError:
            print(f"Invalid JSON response for link {link}: {response.text}")
            continue
        # time.sleep(1)

        # Extract data
        file['Unique ID of VO/NGO'] = req_details['infor']['0']['UniqueID']
        file['NGO Name'] = req_details['infor']['0']['ngo_name']
        file['Email ID'] = req_details['infor']['0']['Email']
        file['Contact #'] = req_details['infor']['0']['Mobile']
        file['City'] = req_details['registeration_info'][0]['nr_city']
        # file['State'] = 'Kerala'
        file['Sector'] = req_details['infor']['issues_working_db']
        file['Website URL'] = req_details['infor']['0']['ngo_url']
        lis.append(file)
print("fully completed")

df = pd.DataFrame(lis)

df.to_csv('NGO_Data of State- {}, from {} to {}.csv'.format(state, first, last))

import pandas as pd


def convert_csv_to_excel(csv_file, excel_file):
    # Read the CSV file
    data = pd.read_csv(csv_file)

    # Write the data to an Excel file
    data.to_excel(excel_file, index=False)
    print(f"Converted '{csv_file}' to '{excel_file}'.")


# Example usage
csv_file = r"C:\Users\prnir\PycharmProjects\NGO_Data of State- PUDUCHERRY, from 1 to 49.csv"  # Path to your CSV file
excel_file = r"C:\Users\prnir\PycharmProjects\Puducherry-NGO.xlsx"  # Path to save the Excel file

convert_csv_to_excel(csv_file, excel_file)

# file merge

import pandas as pd

def merge_two_excel_files(file1, file2, output_file):
    # Read the two Excel files
    data1 = pd.read_excel(file1)
    data2 = pd.read_excel(file2)

    # Merge the two dataframes
    merged_data = pd.concat([data1, data2], ignore_index=True)

    # Save the merged data to a new Excel file
    merged_data.to_excel(output_file, index=False)
    print(f"Merged Excel file saved as '{output_file}'.")


# Example usage
file1 = r"C:\Users\prnir\PycharmProjects\School-2.xls"  # Update with your file path
file2 = r"C:\Users\prnir\PycharmProjects\School-1.xls"  # Update with your file path
output_file = r"C:\Users\prnir\PycharmProjects/School-Final.xlsx"  # Output file path

merge_two_excel_files(file1, file2, output_file)
