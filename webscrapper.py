# Reading tables from a url
# import pandas as pd
# articles = pd.read_html("https://en.wikipedia.org/wiki/Fortnite")
# print(articles[1])

# Reading from a static webpage
from bs4 import BeautifulSoup
import requests

soup = requests.get("https://www.samhirsch.dev")
soup = BeautifulSoup(soup.text, 'html.parser')

# webpage title
print(soup.title.string)

# display first 4 links on webpage
links = soup.find_all('a')
i = 4
for a in links:
    if (i <= 0):
        break;

    print(a.name)
    i-=1

# 