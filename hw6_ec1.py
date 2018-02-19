# 507/206 Homework 6 Part 2
import requests
from bs4 import BeautifulSoup
import sys

#### Part 2 ####
#print('\n*********** PART 2 ***********')
#print('Michigan Daily -- MOST READ\n')

### Your Part 2 solution goes here


html = requests.get('https://www.michigandaily.com/').text
soup = BeautifulSoup(html, 'html.parser')

searching = soup.find_all('div', class_='view view-front-page view-id-front_page view-display-id-panel_pane_2 view-dom-id-dc758981511ef0b427e9dac31b760c1e')
print(searching)

#narrow = searching[0].find_all('class="field-content"')
#for k in narrow:
#    print(k.string)
