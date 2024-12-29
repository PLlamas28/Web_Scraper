# put code here
from bs4 import BeautifulSoup
import requests
import random

num1 = random.randint(0,10)
page_to_scrape = requests.get(f"http://quotes.toscrape.com/page/{num1}")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.find_all("span", attrs = {"class":"text"})
authors = soup.findAll("small", attrs = {"class":"author"})

num = random.randint(0,10)

print(f"Quote: {quotes[num].text}\nBy: {authors[num].text}")
