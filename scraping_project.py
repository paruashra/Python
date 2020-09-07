from random import choice
from csv import DictReader
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://quotes.toscrape.com"


def read_csv():
    with open("scrape.csv") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(quote_list):
    quote = choice(quote_list)
    print("Here's quote" + quote["text"])
    print(quote["author"])
    remaining_guesses = 4
    guess = ""
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        remaining_guesses -= 1
        guess = input(f"Who said this quote? Guesses remaining {remaining_guesses}\n")
        if guess.lower() == quote["author"].lower():
            print('You Got it Right')
            break
        print_hint(quote, remaining_guesses)
    play = input("Do yiu wannt to play again? y/n: ")
    if play.lower() in ['y', 'yes']:
        start_game(quote_list)
    else:
        print("Thanks for playing")


def print_hint(quote, remaining_guesses):
    if remaining_guesses == 3:
        res = requests.get(f"{BASE_URL}{quote['bio-link']}")
        soup = BeautifulSoup(res.text, 'html.parser')
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print(f"Here's is hint: The author was born on {birth_date} {birth_place}")
    elif remaining_guesses == 2:
        print(f"Here's is hint: The author first name starts with {quote['author'][0]}")
    elif remaining_guesses == 1:
        last_initial = quote['author'].split(" ")[1][0]
        print(f"Here's is hint: The author first name starts with {last_initial}")
    else:
        print(f"Sorry, you ran out off guesses: The answer was {quote['author']}")


quotes = read_csv()
print(quotes)
start_game(quotes)
