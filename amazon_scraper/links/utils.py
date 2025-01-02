from bs4 import BeautifulSoup
import requests

def getInfo(url):

    headers = {
        "User-Agent": "", # Your info here
        "Accept-Language": "en",
    }

    page_to_scrape = requests.get(url, headers=headers)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")

    rawTitle = soup.find('span', id="productTitle")
    title = rawTitle.getText().strip()

    rawPrice = soup.find('span',class_="priceToPay")
    strPrice = rawPrice.getText().strip()
    price = float(strPrice.strip("$"))


    
    return title, price