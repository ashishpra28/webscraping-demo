import requests
import pandas as pd
from bs4 import BeautifulSoup



url = "https://www.flipkart.com/search?q=phone%20under%2050000&marketplace=FLIPKART&as-show=on"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url,headers=headers)

soup = BeautifulSoup(r.text,"html.parser")

next = soup.find("span",string="Next")
but = next.find_parent("a")["href"]

link = "https://www.flipkart.com"+but

print(link)