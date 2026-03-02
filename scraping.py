import requests
import pandas as pd
from bs4 import BeautifulSoup

book_info = []

for i in range(1,51):
    web = (f"https://books.toscrape.com/catalogue/page-{i}.html")

    r = requests.get(web)
    soup = BeautifulSoup(r.content, "html.parser")
    book = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for item in book: 
        name = item.find("h3").find("a")["title"]
        price = item.find("p",class_="price_color").text.strip()
        link = item.find("h3").find("a")['href']
        star = item.find("p",class_="star-rating")["class"][1]
        stock = item.find("p",class_="instock availability").text.strip()

        all_products ={
            "name" : name,
            "price":price,
            "link":link,
            "num_of_stars":star,
            "is_available":stock
        }

        book_info.append(all_products)

        

df = pd.DataFrame(book_info)
df.to_csv("book_info.csv",index=False)  
