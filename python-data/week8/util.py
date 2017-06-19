from __future__ import print_function

import mechanicalsoup as mechanize
import requests
from bs4 import BeautifulSoup

br = mechanize.Browser()


def request(list_url):
    res = br.get(list_url)  # request url
    html = res.read()  # html
    soup = BeautifulSoup(html, 'html.parser')  # soup
    return soup


def request_json(url):
    res = requests.get(url)
    return res.json()
