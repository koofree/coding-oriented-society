
import mechanize
import requests
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)

def request(list_url):
    res = br.open(list_url) # request url
    html = res.read() # html
    soup = BeautifulSoup(html, 'html.parser') # soup
    return soup

def request_json(url):
    res = requests.get(url)
    return res.json()

