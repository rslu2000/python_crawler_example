import requests

h =''
res = requests.get('http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php')
h = res.text

import pandas
dfs = pandas.read_html(h)
print dfs[0]
