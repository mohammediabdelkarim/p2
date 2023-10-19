import requests
from bs4 import BeautifulSoup

def get_book_data(url):

    response = requests.get(url)
    soup = BeautifulSoup (response.content, "html.parser")


    data = {}

    return data

book_data = get_book_data("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")

print(book_data)

