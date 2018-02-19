
from bs4 import BeautifulSoup
import requests
import sys


url_input = sys.argv[1]
print('\n*********** PART 1 ***********')
print("Mark's page -- Alt tags\n")


html = requests.get(url_input).text
soup = BeautifulSoup(html, 'html.parser')


#print(soup.prettify())

searching_alt = soup.find_all('img')

for k in searching_alt:
    if 'alt' in k.attrs:
        print(k['alt'])
    else:
        print('No alternative text provided!')
#searching_div = soup.find(id='searching-the-tree')
#print(searching_div)


#heads = searching_div.find_all('h2')
#heads = searching_div.find_all(['h2', 'h3'])
#print(heads)
#tag_h2 = soup.find('h2')
#for h in heads:
#    if h.name == 'h3':
#        print('\t' + h.text)
#    else:
#        print(h.text)
