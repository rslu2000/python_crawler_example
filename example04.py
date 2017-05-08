h =''
file = open ('twse.html')
h = file.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(h, "html5lib")
print soup.text
print soup.contents
print soup.select('body')[0]
print soup.select('a')[0]
print soup.select('td')
for td in soup.select('tbody'):
    print td.text

file.close()

