from __future__ import print_function

import requests
import urllib

# Youtube api request


api_key = open('API_KEY').readline()
video_id = '2GRP1rkE4O0'
url = 'https://www.googleapis.com/youtube/v3/videos'

encoded_params = urllib.parse.urlencode({
    'id': video_id,
    'key': api_key,
    'part': 'snippet,contentDetails,statistics,status'
})

url = url + '?' + encoded_params
print(url)

response = requests.get(url)
json = response.json()

# print json

description = json['items'][0]['snippet']['localized']['description']
statistics = json['items'][0]['statistics']

print(description)
print(statistics)

filename = 'youtube_video_%s' % video_id

with open(filename, 'wb') as file:
    file.write(description.encode('UTF-8'))
    file.flush()
    file.close()

import csv

filename = 'statistics_video_%s.csv' % video_id
with open(filename, 'w') as file:
    fieldnames = ['commentCount', 'viewCount', 'favoriteCount', 'dislikeCount', 'likeCount']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(statistics)
