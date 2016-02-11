
import requests

# Youtube api request
# https://www.googleapis.com/youtube/v3/videos?id=2GRP1rkE4O0&key=AIzaSyCFWRngOLS2xiHN3VuiQh8XxDCMkiMwtYo&part=snippet,contentDetails,statistics,status


# url = 'https://www.googleapis.com/youtube/v3/videos?id=7lCDEYXw3mM&key=YOUR_API_KEY&part=snippet,contentDetails,statistics,status'

api_key = 'AIzaSyCFWRngOLS2xiHN3VuiQh8XxDCMkiMwtYo'
video_id = '2GRP1rkE4O0'
url = 'https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=snippet,contentDetails,statistics,status' % (video_id, api_key)

# url = 'http://naver.com'
print url

response = requests.get(url)
# print response.content
json = response.json()

# print json

description = json['items'][0]['snippet']['localized']['description']
statistics = json['items'][0]['statistics']

#print description
print statistics

# filename = 'youtube_video_%s' % video_id
#
# with open(filename, 'wb') as file:
#     file.write(description.encode('UTF-8'))
#     file.flush()
#     file.close()

import csv

filename = 'statistics_video_%s' % video_id
with open(filename, 'wb') as file:
    fieldnames = ['commentCount', 'viewCount', 'favoriteCount', 'dislikeCount', 'likeCount']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(statistics)