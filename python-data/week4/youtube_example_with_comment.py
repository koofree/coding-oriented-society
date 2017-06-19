from __future__ import print_function

# coding=utf-8

# 비디오 하나만 하던 것을 10개 동시에 가져오려고 할때
import requests

video_ids = ['cZPYWcAg86Q', '1qnV55LUFVM', '1CTced9CMMk']
statistics_list = []

for video_id in video_ids:
    api_key = 'AIzaSyB8ioWdPCrqV1YlI6UTe_Sw3ATeFL7vMGc'
    url = 'https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=snippet,contentDetails,statistics,status' % (
        video_id, api_key)

    response = requests.get(url)
    json = response.json()

    print(url)

    statistics = json['items'][0]['statistics']
    statistics['videoId'] = video_id
    # 이거 만으로는 어떤 비디오 데이터 인지 몰라 그래서 video id 추가해 준거 statistics['videoId'] = video_id

    statistics_list.append(statistics)

print(statistics_list)

import csv

filename = 'statistics_video.csv'
with open(filename, 'wb') as file:
    fieldnames = ['videoId', 'commentCount', 'viewCount', 'favoriteCount', 'dislikeCount', 'likeCount']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for statistics in statistics_list:
        writer.writerow(statistics)

# 이거 만으로는 어떤 비디오 데이터 인지 몰라 그래서 video id 추가해 준거 statistics['videoId'] = video_id
