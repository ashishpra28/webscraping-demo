import requests
import pandas as pd
from bs4 import BeautifulSoup

all_items = []

baseurl = "https://loveandflair.com/"
url = "https://loveandflair.com/collections/activewear-1?page=1"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

product_list = soup.find_all(
    "li",
    class_=["collection-product-card", "quickview"]
)

pro_link = []

for item in product_list: 
    for link in item.find_all("a",href=True): 
        pro_link.append(baseurl+link["href"])

pro_link = list(set(pro_link))

# testlink = "https://loveandflair.com/products/lune-flare-pants-in-moss"

for links in pro_link: 
    r = requests.get(links, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")

    name = soup.find("h4",class_ = "product__title").text.strip()
    price = soup.find("span",class_ = "money").text.strip()
    stock = soup.find("span",id = "Inventory-template--17036470190311__main").text.strip()
    color = soup.select_one("label.color-swatch span.visually-hidden").text.strip()
    sizes = soup.select('input[name="Size"]:checked')
    available_sizes = [s['value'] for s in sizes]
    spans = soup.select('span._aupe.copyable-text.xkrh14z')
    # material = spans[6].text.strip()  

    product_details = {
        "name":name,
        "price":price, 
        "stock":stock, 
        "color":color, 
        "sizes":available_sizes,
        # "material":material

    }

    all_items.append(product_details)

df = pd.DataFrame(all_items)
df.to_csv("loveandfair.com/all_items.csv", index=False)