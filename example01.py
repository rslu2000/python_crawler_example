from bs4 import BeautifulSoup
html_sample = ' \
<html> \
<body> \
<h1 id="title">Hello World</h1> \
<a href="#" class="link">This is link</a> \
<a href="# link2" class="link">This is link2</a> \
</body> \
</html>'
soup = BeautifulSoup(html_sample, "html5lib")
print soup.text 
print soup.contents
