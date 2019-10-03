import requests
from bs4 import BeautifulSoup as bs
from tabulate import tabulate

base_url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="
request = input("Enter product: ").replace(" ", "+")
url_sep = "&_sacat=0&_pgn="
page_num = 1
totalPrice = 0
itemArray = []
groupedList = []

url = base_url + request + url_sep + str(page_num)
html = requests.get(url).text
soup = bs(html, "html.parser")


def scrapeData():
    for post in soup.find_all("li", {"class": "s-item"}):
        try:
            findPrice = post.find("span", {"class": "s-item__price"}).text
            if findPrice != 'Tap item to see current priceSee Price':
                name = post.find("h3", {"class": "s-item__title"}).text
                condition = post.find("span", {"class": "SECONDARY_INFO"}).text
                price = post.find("span", {"class": "s-item__price"}).text

            name = name.replace("New Listing", "")
        except AttributeError:
            price = condition = name = ""

        itemArray.extend([name, condition, price])


def groupData():
    i = 3  # Start at 3 to avoid empty list
    scrapeData()
    while i < len(itemArray):
        groupedList.append(itemArray[i:i + 3])
        i += 3


def convertDataToTable():
    groupData()
    print(tabulate(groupedList, headers=['Product', 'Condition', 'Price']))


convertDataToTable()
