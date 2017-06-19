from __future__ import print_function

import requests
import urllib

# requests 모듈을 사용

# youtube api requests

api_key = open('API_KEY').readline()
# api키는 https://developers.google.com/youtube/ 생성
video_id = 'cZPYWcAg86Q'
# videoid는 임의의 유튜브 동영상주소에서 뒷 부분
url = 'https://www.googleapis.com/youtube/v3/videos'

encoded_params = urllib.parse.urlencode({
    'id': video_id,
    'key': api_key,
    'part': 'snippet,contentDetails,statistics,status'
})

url = url + '?' + encoded_params

# 캡쳐부분, 중간 id와 key 부분은 계속 변경되는 것이기 때문에 변수로 지정(%s) 하고 %s 변수는 위에서 지정해놓은 video_id, api_key에 해당되는 것이라고 써준다.


response = requests.get(url)
# response라는 객체(변수)는 requests.get 함수를 이용해 위에서 지정한 url로 데이터를 가져오도록 요청하는 것
json = response.json()
# json은 이 response라는 객체를 리스트,딕션어리 형태로 정리된 데이터로 변환할 수 있도록 해주는 함수 ( 왜냐면 기존의 데이터는 string, 즉 문자열의 형태로만 되어있어)

print(json)
# or
print(url)
# 이대로 출력하면 해당 동영상의 데이터를 지정한 url로 요청해서 가져온 결과 값을 확인할 수 있다.

description = json['items'][0]['snippet']['localized']['description']
print(description)

statistics = json['items'][0]['statistics']
print(statistics)

# json형태의 파일의 일부분을 csv파일로 저장하려고....

import csv

filename = 'statistics_video_%s' % video_id
with open(filename, 'wb') as file:
    fieldnames = ['commentCount', 'viewCount', 'favoriteCount', 'dislikeCount', 'likeCount']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    # 저장을 딕션어리로 할거기 때문에 필드네임을 제일 먼저 입력해 줍니다.
    writer.writerow(statistics)

# dit 로 된 파일을 csv 파일로, 우리가 가져온 유튜브데이터는 딕션어리 형태로 되어있어
# 필드네임은 딕션어리 중에서 이름으로 들어갈 부분


# filename = 'youtube_video_%s' % video_id
# 항목 지우고 출력하고 싶을때는 del statistics['항목이름']
