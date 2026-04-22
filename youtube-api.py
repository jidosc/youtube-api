import requests
import dotenv
import os
from datetime import datetime
import json

dotenv.load_dotenv()

youtube_link = "https://youtu.be/VIDEO_ID"
last_time_checked: datetime = datetime.fromisoformat("2026-04-18T09:00:39Z")
api_key: str = os.getenv('YOUTUBE_API_KEY')


def get_videos():
    channel_id = os.getenv("YOUTUBE_CHANNEL_ID")
    response = requests.get(f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=20")
    if response.ok:
        with open("response.json", "+wb") as file:
            # log content of response
            file.write(response.content)

        print("Request was succesful")
        # load bytes of response to json
        return json.loads(response.content.decode('utf-8'))
    
    print("Request unsuccesful")


def get_new_videos():
        videos = get_videos()
        new_videos = []
        global last_time_checked

        for video in videos.get('items'):
            video_snippet = video.get('snippet')
            video_datetime: datetime = datetime.fromisoformat(video_snippet.get('publishedAt'))
            # if video is newer than last time it was checked
            if video_datetime > last_time_checked:
                # save dictionary with id and title
                new_videos.append({"id": video.get('id').get('videoId'), 'title': video_snippet.get('title')})
        
        last_time_checked = datetime.now()

        return new_videos


def format_video_notification(video_title: str, video_id: str) -> str:
     return f"En ny video publicerades precis: **{video_title}**\n{youtube_link.replace('VIDEO_ID', video_id)}"


for new_video in get_new_videos():
     print(format_video_notification(new_video.get('title'), new_video.get('id')))