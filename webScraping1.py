#webscrapper
#10_March_2019
#jedenfalls

from bs4 import BeautifulSoup

mook = '<!doctype html><html><head><title>Example Domain</title><meta charset="utf-8" /><meta http-equiv="Content-type" content="text/html; charset=utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1" /><style type="text/css">body{background-color:#f0f0f2;margin:0;padding:0;font-family:"Open Sans","Helvetica Neue",Helvetica,Arial,sans-serif}div{width:600px;margin:5em auto;padding:50px;background-color:#fff;border-radius:1em}a:link,a:visited{color:#38488f;text-decoration:none}@media (max-width: 700px){body{background-color:#fff}div{width:auto;margin:0 auto;border-radius:0;padding:1em}}</style></head><body><div><h1>Example Domain</h1><p>This domain is established to be used for illustrative examples in documents. You may use this domain in examples without prior coordination or asking for permission.</p><p><a href="http://www.iana.org/domains/example">More information...</a></p></div></body></html>'

soup = BeautifulSoup(mook, 'html.parser')

#print(soup.body)

#print(soup.title)

#print(soup.head.title)

#find()  >> only gives the first one it finds
el = soup.find('div')  

#print(el)

#find_all or findAll  >> finds all occurences item
el2= soup.findAll('div')

# or el3 = soup.findAll('div')[2] for the third instance of div

print(el2)

#for IDs 
el4 = soup.find(id='section-1') #or class_ (with an underscore) instead of id, attrs for attributes

el5 = soup.select('sek')

el6 = get_text

el7 = soup.find('dkadf').get_text() # no tags

#next_sibling
#find_next_sibling
#previous_sibling

from csv import writer


