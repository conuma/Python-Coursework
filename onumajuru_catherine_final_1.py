import requests
from bs4 import BeautifulSoup
import time
import pickle

url = "http://www.nuforc.org/webreports/ndxevent.html"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
links = soup.findAll('a')
nest = []
i = 1
while i < len(links):
    url2 = "http://www.nuforc.org/webreports/" + links[i]["href"]
    data = requests.get(url2)
    soup2 = BeautifulSoup(data.text, "html.parser")
    cells = soup2.findAll('tr')
    for cell in cells:
        empt = []
        data2 = cell.findAll('td')
        for m in data2:
            d = m.get_text()
            empt.append(d)
        nest.append(empt)
    time.sleep(5)
    i = i + 1

list2 = [x for x in nest if x != []]
new_list = []
for sub in list2:
    city = sub[1]
    state = sub[2]
    cs = city + ", " + state
    new_list.append(cs)
result = dict((n, new_list.count(n)) for n in new_list)
last_list = []
for key, value in result.items():
    result_1 = key + '\t' + str(value) + '\n'
    last_list.append(result_1)
f = open("onumajuru_catherine_cities.txt", 'wb')
pickle.dump(last_list, f)
f.close()
