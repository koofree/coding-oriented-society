from __future__ import print_function

import mechanize
import json
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)  # ignore crawler setting information

####################################################
# Generate url address for crawling
entire_url = "http://www.polygon.com/2016/1/12/10755490/ea-sports-ufc-2-gameplay-trailer-features"
res = br.open(entire_url)
html = res.read()
soup = BeautifulSoup(html, 'html.parser')

####################################################
# Finding article meta information
published_time = str()
author = str()
for meta in soup.head.findAll('meta'):
    meta_property = meta.attrs.get('property')
    meta_name = meta.attrs.get('name')
    if meta_property == 'article:published_time':
        published_time = meta.attrs.get('content')
    if meta_name == 'author':
        author = meta.attrs.get('content')

print(soup.find(id='comments'))

####################################################
# Finding youtube video ids
youtube_string = str()

for iframe in soup.findAll('iframe'):
    # taking iframe
    src_string = iframe.get('src')
    if 'youtube' in src_string:
        youtube_string = src_string

print(youtube_string)
print(youtube_string[30:41])
start = youtube_string.rfind('/') + 1
end = youtube_string.rfind('?')

if end is '-1':
    print(youtube_string[start:])
else:
    print(youtube_string[start:end])

####################################################
entry__title = soup.find(class_='m-entry__title')
entry_id = entry__title.attrs.get('data-remote-admin-entry-id')

comment_url = 'http://www.polygon.com/comments/load_comments/' + str(entry_id)
comment_res = br.open(comment_url)
comment_json = json.loads(comment_res.read())

####################################################
data = {
    '_id': entire_url,
    'published_time': published_time,
    'author': author,
    'comment_len': len(comment_json['comments']),
    'youtube_url': youtube_string
}

# print data
