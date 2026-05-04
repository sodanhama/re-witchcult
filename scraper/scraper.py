import requests
from bs4 import BeautifulSoup
import os
import json

url = "https://witchculttranslation.com/table-of-content/"

response = requests.get(url)

text = response.text

contents = BeautifulSoup(text, "html.parser")

print(contents.prettify())