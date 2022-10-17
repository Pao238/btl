import requests
import sys
from bs4 import BeautifulSoup
from csv import writer

URL = "https://topdev.vn/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
lists = soup.find_all('li',class_='open')

with open("review.csv","w",encoding='utf-8',newline='') as f:
    viet = writer(f)
    tieude = ['Name','Location','Address']
    viet.writerow(tieude)
    for list in lists:
        name = list.find('a','img')
        loca = list.find('h3',class_='mt-2').text
        add = list.find('p',class_='address').text
        tt = [name,loca,add]
        viet.writerow(tt)
        