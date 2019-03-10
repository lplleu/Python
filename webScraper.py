import requests
import bs4
res = requests.get('http://www.example.com')
soup = bs4.BeautifulSoup(res.text,'lxml')
type(soup)
hi = soup.Select('title')
hi[0].getText()
