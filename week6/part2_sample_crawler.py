import mechanize
import json
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False) # ignore crawler setting information

####################################################
# Generate url address for crawling
entire_url = "http://www.polygon.com/2016/1/12/10755490/ea-sports-ufc-2-gameplay-trailer-features"
res = br.open(entire_url)
html = res.read()
soup = BeautifulSoup(html, 'html.parser')

####################################################
# Finding youtube video ids
youtube_string = str()

for iframe in soup.findAll('iframe'):
    # taking iframe
    src_string = iframe.get('src')
    if 'youtube' in src_string:
        youtube_string = src_string

start = youtube_string.rfind('/') + 1
end = youtube_string.rfind('?')

youtube_id = str()
if end is '-1':
    youtube_id = youtube_string[start:]
else:
    youtube_id = youtube_string[start:end]

print youtube_id
