# coding= utf-8
import mechanicalsoup as mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()

list_url = 'https://www.polygon.com/videos'

res = br.get(list_url)  # request url
a_tags = res.soup.find_all('a')  # finding a tags

links = []
for a_tag in a_tags:
    url = a_tag.attrs.get('href')
    if not url:  # url 이 비어있는 주소라면
        continue

    if not 'http://www.polygon.com/' in url:
        # url 에 http://www.polygon.com/ 가 포함되어 있으면
        continue

    length = len('http://www.polygon.com/')
    year = url[length:length + 4]

    if not year.isdigit():
        continue
    #
    if 'comments' in url:
        continue

    if url in links:
        continue

    links.append(url)

youtube_ids = []

for link in links:
    ####################################################
    # Generate url address for crawling
    entire_url = link
    res = br.get(entire_url)
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
    if end is -1:
        youtube_id = youtube_string[start:]
    else:
        youtube_id = youtube_string[start:end]

    if youtube_id == '':
        continue

    if youtube_id == 'videoseries':
        continue

    youtube_ids.append(youtube_id)

print('Count of youtube ids is %s' % len(youtube_ids))

import requests

video_ids = youtube_ids
statistics_list = []

for video_id in video_ids:
    api_key = ''
    url = 'https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=snippet,contentDetails,statistics,status' % (
        video_id, api_key)

    response = requests.get(url)
    json = response.json()

    statistics = json['items'][0]['statistics']
    statistics['videoId'] = video_id
    # 이거 만으로는 어떤 비디오 데이터 인지 몰라 그래서 video id 추가해 준거 statistics['videoId'] = video_id

    statistics_list.append(statistics)

import csv

filename = 'statistics_video.csv'
with open(filename, 'wb') as file:
    fieldnames = ['videoId', 'commentCount', 'viewCount', 'favoriteCount', 'dislikeCount', 'likeCount']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for statistics in statistics_list:
        writer.writerow(statistics)

print('Save file finished!')
