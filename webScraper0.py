import bs4
import requests
from bs4 import BeautifulSoup

from csv import writer
response = requests.get('http://www.example.com/')

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title)

#posts = soup.find_all(class_="posts")
posts = soup.find_all('<div>')

#get_text()
#replace

with open('results.csv','w') as csv_file:
  csv_write = writer(csv_file)
  headers = ['title','author','affiliation','year']
  csv.writer.writerow(headers)

  

for post in posts:
  print(post)
  csv.writer.writerow(headers)

