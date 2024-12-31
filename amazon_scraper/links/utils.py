from bs4 import BeautifulSoup
import requests

def getInfo(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
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