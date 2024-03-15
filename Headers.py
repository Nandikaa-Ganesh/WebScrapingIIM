from seleniumwire import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.chrome.options import Options
import csv
from collections.abc import Callable
import requests

scrape_url = "https://www.tripadvisor.in/Attraction_Review-g297685-d319858-Reviews-Ganges_River-Varanasi_Varanasi_District_Uttar_Pradesh.html"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
}

r = requests.get(scrape_url, headers=HEADERS)
html_code = r.text

#driver = webdriver.Chrome()

#driver.get(scrape_url)
soup = BeautifulSoup(html_code, 'html.parser')
reviews = soup.find_all("div", class_="_c")
print(reviews)
