# put code here
from bs4 import BeautifulSoup
import requests

def getInfo(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept-Language": "en",
    }

    page_to_scrape = requests.get(url, headers=headers)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")

    rawPrice = soup.find('span',class_="priceToPay")
    price = rawPrice.getText().strip()

    rawTitle = soup.find('span', id="productTitle")
    title = rawTitle.getText().strip()
    return price, title




#x = requests.get(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})

url = "https://www.amazon.com/Anker-Portable-Compatible-Charging-Included/dp/B0BYP2F3SG/ref=sr_1_2_sspa?crid=11I7P2HT01MQ&dib=eyJ2IjoiMSJ9.E11hzKfTe92--H7Z-o8kWeTnQfg0_Tn2XkQFx-hVGWyWX7p4NuCAITCbceV8v-n02noegmABTzlUPT72uPPQO-aKXyVMitDkF_RsPbnxmihG6K7K2ruk5hbeKzSWJKihaq8RCiQjakdes3RVQT3hEdECrgtMbeml6AjhWKU0D6ddeWZ6SzcrsscaA1GNZBWEVB6DFZ1KJyWHqLnB_QNragjxa2URpzMTw2iM0tD-AJc._wP-jPpuiVxa18Qjl42fFTHsPeT5gC2ywksqwVRj97U&dib_tag=se&keywords=anker&qid=1735493245&sprefix=ank%2Caps%2C139&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

print("--------------------")
print(getInfo(url))
#print(soup.find_all('span', class_='a-offscreen')[2].getText())
