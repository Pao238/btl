import requests
import sys
from bs4 import BeautifulSoup
from csv import writer

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#print(page.text)      
# h2-Job-class:title is-5 /h3-Company class:subtitle is-6 company 
# /p-class:location-Location /time-datetime:2021-04-08-Date

soup = BeautifulSoup(page.content, "html5lib")
lists = soup.find_all('div',class_='card-content')

with open("review.csv","w",encoding='utf-8',newline='') as f:
    viet = writer(f)
    tieude = ['Job','Company','Location','Time']
    viet.writerow(tieude)
    for list in lists:
        job = list.find('h2',class_='title is-5').text.replace('\n',"")
        company = list.find('h3',class_='company').text.replace('\n',"")
        location = list.find('p',class_='location').text.replace('\n',"").strip()
        time = list.find('time',datetime='2021-04-08').text.replace('\n',"").strip()

        tt = [job,company,location,time]
        viet.writerow(tt)
        