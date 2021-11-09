# https://www.apollopharmacy.in/shop-by-category/cold-cough



import requests
from bs4 import BeautifulSoup
import re
import pandas as pd



endpoints = []

for j in range(0,6):
    url = "https://www.apollopharmacy.in/shop-by-category/cold-cough" + str(j)
    res = requests.get(url).content
    soup = BeautifulSoup(res, "html.parser")


    for link in soup.find_all('a',href =True,attrs={'class':'heILj'}):

       result = (link.get('href'))

       endpoints.append(result)
print(endpoints)
append_str="https://www.apollopharmacy.in"
final_link=[append_str + sub for sub in endpoints]
print(final_link)
df = pd.DataFrame (final_link)
print (df)
df.to_csv(r'C:\Akhil\cold.csv')
