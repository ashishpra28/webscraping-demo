import requests
import pandas as pd
from bs4 import BeautifulSoup

quotes = []


for i in range(1,11):
    web = (f"https://quotes.toscrape.com/page/{i}/")

    r = requests.get(web)
    soup = BeautifulSoup(r.text, "html.parser")
    scrape = soup.find_all("div", class_="quote")

    for i in scrape: 
        quote = i.find("span",class_="text").text.strip()
        author = i.find("small",class_="author").text.strip()
        t = i.find_all("a", class_="tag")
        tags = [tag.text for tag in t]
        link = i.find("a")["href"]
        
        all_scraped = {
            "quote":quote,
            "author":author,
            "tags":tags,
            "link":link
        }

        quotes.append(all_scraped)


df = pd.DataFrame(quotes)
df.to_csv("quotes.csv",index=False)  
