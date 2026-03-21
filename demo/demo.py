import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text,"html.parser")

# prices = soup.find_all("span",itemprop="price")
# name = soup.find_all("a",class_ = "title")
# desc = soup.find_all("p",class_ = "description card-text")
# rev = soup.find_all("p",class_ = "review-count float-end")
# # for i in desc: 
#     print(i.text)

# pattern with re.compile
data = soup.find_all(string = re.compile("Galaxy"))

# from nested data 
d = soup.find_all("div",class_ = "col-md-4 col-xl-4 col-lg-4")[2]

for i in d: 
    name = d.find("a").text.strip()
    p = d.find("span").text
    desc = d.find("p",class_ = "description card-text").text
    r = d.find("p",class_ = "review-count float-end").text

print(name)
print(p)
print(desc)
print(r)