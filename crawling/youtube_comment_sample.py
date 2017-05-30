from __future__ import print_function

from apiclient.discovery import build

# coding=utf-8
# !/usr/bin/python

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_comment(video_id, next_page_token=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    if next_page_token:
        results = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults="10",
            pageToken=next_page_token
        ).execute()
    else:
        results = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults="10"
        ).execute()

    for item in results["items"]:
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        text = comment["snippet"]["textDisplay"]
        date = comment["snippet"]["publishedAt"]
        print("[%s] Comment by %s: %s" % (date, author, text))

    return results["nextPageToken"]


next_page_token = youtube_comment("xVk12W1PA8g")
next_page_token = youtube_comment("xVk12W1PA8g", next_page_token)
next_page_token = youtube_comment("xVk12W1PA8g", next_page_token)
next_page_token = youtube_comment("xVk12W1PA8g", next_page_token)

# queries = ['화장', '메이크업', '음악']
# for query in queries:
#     try:
#         youtube_search(query, 30)
#     except HttpError, e:
#         print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
