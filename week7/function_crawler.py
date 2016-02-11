# coding= utf-8

import mechanize
import requests
import csv
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)

def finding_web_links(list_url):
    res = br.open(list_url) # request url
    html = res.read() # html
    soup = BeautifulSoup(html, 'html.parser') # soup
    a_tags = soup.find_all('a') # finding a tags
    links = []
    for a_tag in a_tags:
        url = a_tag.attrs.get('href')
        if not url: # url 이 비어있는 주소라면
            continue
        if not 'http://www.polygon.com/' in url:
            # url 에 http://www.polygon.com/ 가 포함되어 있으면
            continue
        length = len('http://www.polygon.com/')
        year = url[length:length+4]
        if not year.isdigit():
            continue
        if 'comments' in url:
            continue
        if url in links:
            continue
        links.append(url)
    return links

def finding_youtube_id(link_url):
    ####################################################
    # Generate url address for crawling
    res = br.open(link_url)
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
        return None
    if youtube_id == 'videoseries':
        return None
    return youtube_id

def youtube_statistics(youtube_id):
    api_key = 'AIzaSyB8ioWdPCrqV1YlI6UTe_Sw3ATeFL7vMGc'
    url = 'https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=snippet,contentDetails,statistics,status' \
          % (youtube_id, api_key)

    response = requests.get(url)
    json = response.json()

    statistics = json['items'][0]['statistics']
    statistics['videoId'] = youtube_id
    # 이거 만으로는 어떤 비디오 데이터 인지 몰라 그래서 video id 추가해 준거 statistics['videoId'] = video_id
    return statistics

def save_statistics(statistics_list, filename):
    with open(filename, 'wb') as file:
        fieldnames = ['videoId', 'commentCount', 'viewCount', 'favoriteCount', 'dislikeCount', 'likeCount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for statistics in statistics_list:
            writer.writerow(statistics)

    print 'Save file finished!'

##############

links_result = []
for page_number in range(1, 10):
    print 'Start crawling %s page.' % page_number
    url = 'http://www.polygon.com/videos/%s' % page_number
    links_result.extend(finding_web_links(url))

youtube_ids = []
for link in links_result:
    print 'Request youtube api [%s]' % link
    youtube_id = finding_youtube_id(link)
    if youtube_id:
        youtube_ids.append(youtube_id)

print 'Count of youtube ids is %s' % len(youtube_ids)

statistics_result = []
for youtube_id in youtube_ids:
    statistics = youtube_statistics(youtube_id)
    statistics_result.append(statistics)

save_statistics(statistics_result, 'statistics_video.csv')
















