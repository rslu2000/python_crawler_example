s =''
file = open ('hello_world.html')
s = file.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(s, "html5lib")
print soup.text
print soup.contents
print soup.select('body')[0]
print soup.select('a')[0]
file.close()
