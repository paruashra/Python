import requests
from bs4 import BeautifulSoup
from csv import DictWriter

BASE_URL = "http://quotes.toscrape.com"


def scrap_quotes():
    quote_list = []
    url = "/page/1/"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.select(".quote")
        for quote in quotes:
            quote_list.append({
                "text":quote.find(class_="text").get_text(),
                "author":quote.find(class_="author").get_text(),
                "bio-link":quote.find("a")["href"],
                })

        nxt = soup.find(class_="next")
        url = nxt.find("a")["href"] if nxt else None
    return quote_list


def write_quotes(quotes):
    with open("scrape.csv" , "w") as file:
        headers = ['text', 'author', 'bio-link'] 
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)


quotes = scrap_quotes()
write_quotes(quotes)
