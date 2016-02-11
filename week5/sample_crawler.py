__author__ = 'Koo Lee'

import mechanize
import json
from bs4 import BeautifulSoup
from sets import Set
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING


def initialize_mongodb(database_uri):
    client = MongoClient(database_uri)
    db = client.crawl
    polygon = db['polygonurl']
    youtube = db['youtube']
    polygon.create_index([("url", ASCENDING)])
    return (polygon, youtube)


polygon, youtube = initialize_mongodb('mongodb://127.0.0.1:27017/')

br = mechanize.Browser()
br.set_handle_robots(False)


def finding_urls():
    root_url = "http://www.polygon.com/videos"
    page = 1

    while True:
        page += 1
        res = br.open(root_url + "/" + str(page))

        soup = BeautifulSoup(res.read(), 'html.parser')

        map = Set()
        for atag in soup.findAll('a'):
            url = atag.get('href')
            if not url:
                continue
            if not 'http://www.polygon.com/' in url:
                continue

            sub = url[len('http://www.polygon.com/'):]
            year = sub[:sub.find("/")]
            if not year.isdigit():
                continue

            if 'comments' in sub:
                continue

            map.add(sub)

        for item in map:
            exist_item = polygon.find_one({'url': item})
            if exist_item is None:
                polygon.insert_one({'url': item}).inserted_id
            finding_youtube(item)


def finding_youtube(url):
    minus_year = url[url.find('/') + 1:]
    minus_month = minus_year[minus_year.find('/') + 1:]
    minus_day = minus_month[minus_month.find('/') + 1:]
    polygon_id = minus_day[:minus_day.find('/')]

    entire_url = "http://www.polygon.com/" + url
    res = br.open(entire_url)
    soup = BeautifulSoup(res.read(), 'html.parser')

    published_time = str()
    author = str()
    for meta in soup.head.findAll('meta'):
        meta_property = meta.attrs.get('property')
        meta_name = meta.attrs.get('name')
        if meta_property == 'article:published_time':
            published_time = meta.attrs.get('content')
        if meta_name == 'author':
            author = meta.attrs.get('content')

    youtube_string = str()
    for iframe in soup.findAll('iframe'):
        src_string = iframe.get('src')
        if 'youtube' in src_string:
            youtube_string = src_string

    entry__title = soup.find(class_='m-entry__title')
    entry_id = entry__title.attrs.get('data-remote-admin-entry-id')

    comment_url = 'http://www.polygon.com/comments/load_comments/' + str(entry_id)
    comment_res = br.open(comment_url)
    comment_json = json.loads(comment_res.read())

    data = {
        '_id': entire_url,
        'published_time': published_time,
        'author': author,
        'comment_len': len(comment_json['comments']),
        'youtube_url': youtube_string
    }

    # youtube.update({'_id': data['_id']}, data, True)

    print data


finding_urls()
