import requests
import json
import configparser as cfg
from googleapiclient.discovery import build


class youtubeSearch():

    def __init__(self):
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.credentials = "YOUR YOUTUBE CREDS"
        self.message = ""
        self.description = ""


    #method for starting a youtube search
    def main(self, query):

        # Get credentials and create an API client
        youtube = build(self.api_service_name, self.api_version, developerKey= self.credentials)

        request = youtube.search().list(
            part="snippet",
            maxResults=1,
            order="relevance",
            q = query,
            type="video"
        ).execute()

        # extracting the results from search response 
        results = request.get("items", []) 
    
        # empty list to store video
        videos = []
        
        # extracting required info from each result object 
        for result in results: 
            # video result object 
            info = []
            videos.append([
                result["id"]["videoId"], 
                result["snippet"]["title"], 
                result['snippet']['description'], 
                result['snippet']['thumbnails']['default']['url']])
        
        videos.append(info) 
        videoID = videos[0][0]
        _videoID = videos[0][1]
        self.message = "https://www.youtube.com/watch?v={}".format(videoID)
        self.description = _videoID
        print(_videoID)