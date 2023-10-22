from typing import List

import requests
from bs4 import BeautifulSoup


def get_book_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = dict()

    title = soup.select_one('title').get_text()
    #price_including_tax = soup.select_one('p.price_color').get_text()
    product_page_url = soup.select_one('script').get_text()
    #img = soup.select_one('div.sub-header,p').get_text()
    upc = soup.select_one('table.table-striped').get_text()
    div = soup.find('div', {'class': 'product_main'})
    h1 = div.find('h1')
    data['title'] = h1.text
    description = soup.find('p', class_='').text
    liens_categorie = soup.find_all('a')
    categorie = liens_categorie[3].text
    image_base = soup.find('img')
    image_lien = image_base['src']
    image = 'http://books.toscrape.com' + image_lien[5:]

    #version = liste_td[6].text

    #price_including_tax =
    #data['price_including_tax']

    #div = soup.find('tr', {'th': 'td'})
    #td = div.find('tr')
    #data['td'] = td.text
    #print(title)
    #print(price_including_tax)
    print(upc)
    print(product_page_url)
    print(description)
    print(categorie)
    print(image)
    #print(img)
    #print(data)
    return data



book_data = get_book_data('https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
print(book_data)


#product_page_url

#● category

#● image_url