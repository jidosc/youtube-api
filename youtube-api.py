import requests
import dotenv
import os
import datetime
import json

youtube_link = "https://youtu.be/VIDEO_ID"
published_after = datetime.datetime.fromisoformat("2026-04-18T09:00:39Z")

def get_videos():
    dotenv.load_dotenv()
    key = os.getenv("YOUTUBE_API_KEY")
    channel_id = os.getenv("YOUTUBE_CHANNEL_ID")

    response = requests.get(f"https://www.googleapis.com/youtube/v3/search?key={key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=20")

    if response.ok:
        with open("response.json", "+wb") as file:
            file.write(response.content)

        content = json.loads(response.content.decode('utf-8'))
        new_matches = []

        for match in content.get('items'):
            published_at: datetime.datetime = datetime.datetime.fromisoformat(match.get('snippet').get('publishedAt'))
            if published_at > published_after:
                new_matches.append(match.get('snippet').get('title'))
                print(f"You should watch this new video: {youtube_link.replace('VIDEO_ID', match.get('id').get('videoId'))}")

        print("Request was succesful")
    else:
        print("Request was unsuccessful")


get_videos()