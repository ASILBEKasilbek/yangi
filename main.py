import requests
from bs4 import BeautifulSoup


# url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
# response = requests.get(url)
# # print(response)
# soup = BeautifulSoup(response.text, 'lxml')

# quotes = soup.find_all('div',class_= 'w-full rounded border')
# for i in quotes:
#     print(i)
#     title = i.find('h4')
#     price = i.find('h5')
#     print(title.text,price.text)
#     # print(quote.text)


url = 'https://www.olx.uz/transport/legkovye-avtomobili/'

response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')

quotes = soup.find_all('div',class_= 'css-1apmciz')

for i in quotes:
    # print(i)
    name = i.find('div')
    price = i.find('h6',)
    print(name.text in range(3),price.text in range(3))