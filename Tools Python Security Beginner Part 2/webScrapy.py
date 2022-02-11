"""
Author = Francisco Gomes
Date = 11/02/2022
Project = Create a Web Scrapy
Version = 1.0
"""
#Importing libraries
from bs4 import BeautifulSoup
import requests


#Here is search all content with method "content" in site with parameter
#Object "site" this is received content of request HTTP
site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')

#Method prettify converting content HTML for String
#And printing page
print(soup.prettify())

