from pytube import YouTube
from datetime import datetime
import ffmpeg
import os

from constants.constants import storage_dir_output
 
class DownLoader:
    def __init__(self, link):
        self.__yt = YouTube(link)

    def get_title(self):
        return self.__yt.title

    def get_author(self):
        return self.__yt.author

    def get_publish_date(self):
        return self.__yt.publish_date

    def get_rating(self):
        return self.__yt.rating

    def get_views(self):
        return self.__yt.views
    
    def get_length(self):
        return self.__yt.length
    
    def get_keywords(self):
        return self.__yt.keywords
    
    def download(self,format):
        self.__yt.streams.filter(res=format,mime_type="video/mp4",progressive="True").first().download(storage_dir_output)


y = DownLoader("https://youtu.be/kFUi3ikZFvk")
print('Download has begin')
print(y.get_author())
y.download('720p')
### REDUNDANT CODE

# stream = yt.streams[4]
# print(stream)
# stream.download(storage_dir_video)
# stream = yt.streams[16]
# print(stream)
# stream.download(storage_dir_audio)
#print(datetime.now())
# yt.streams.filter(res="720p",mime_type="video/mp4",progressive="True").first().download(storage_dir) 

#print(datetime.now())
#print("finish!")

# For HD downloads
# p = os.path.join(storage_dir_audio,'test1.mp3')
# if os.path.exists(p):
#     print("ll")
# else:
#     print('ddd')
 
# input_video = ffmpeg.input(os.path.join(storage_dir_video,'test.mp4'))
 
# input_audio = ffmpeg.input(os.path.join(storage_dir_audio,'test1.mp3'))
 
# ffmpeg.concat(input_video, input_audio, v=1, a=1).output('test.mp4').run()
# print("finish")

