from __future__ import print_function

import requests
import csv

video_ids = ['2GRP1rkE4O0', 'D8t8A8E_Tqc', '9jTo6hTZmiQ']
statistics_list = []

for video_id in video_ids:
    api_key = open('API_KEY').readline()
    url = 'https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=snippet,contentDetails,statistics,status' % (
        video_id, api_key)

    print(url)

    response = requests.get(url)
    json = response.json()

    statistics = json['items'][0]['statistics']
    del statistics['likeCount']
    del statistics['dislikeCount']

    statistics['videoId'] = video_id

    statistics_list.append(statistics)

print(statistics_list)

statistics = statistics_list[0]

print("#####")
print(statistics)
fieldnames = statistics.keys()

filename = 'statistics_video_%s.csv' % 'newFile'
with open(filename, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for statistics in statistics_list:
        writer.writerow(statistics)
