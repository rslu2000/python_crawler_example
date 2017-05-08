import requests

h =''
res = requests.get('http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php')
h = res.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(h, "html5lib")
print soup.text
print soup.contents
print soup.select('body')[0]
print soup.select('a')[0]
print soup.select('td')
for td in soup.select('tbody'):
    print td.text

