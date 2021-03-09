from pytube import YouTube
from datetime import datetime
import ffmpeg
import os
 
storage_dir_audio = "D:\\Test\\audio\\"
storage_dir_video = "D:\\Test\\video\\"
storage_dir_output = "D:\Test_Data\\output\\"
 
raw_link = "https://youtu.be/AjtX1N_VT9E"
 
try:
    #creating object
    yt = YouTube(raw_link)
 
except:
    print("connection error")
 
print(yt.title)
#print(yt.check_availability())
print(yt.author)
#print(yt.caption_tracks)
#print(yt.captions)
#st = (yt.description).encode('utf-8')
#print(st)
print(yt.keywords)
print(yt.length)
#print(yt.metadata)
print(yt.publish_date)
print(yt.rating)
#print(yt.streams)
#print(yt.thumbnail_url)
print(yt.views)
#print(help(yt))

#print(yt.streams.first().mime_type)
 
for stream in yt.streams:
    #print(help(stream))
    pass
# stream = yt.streams[4]
# print(stream)
# stream.download(storage_dir_video)
# stream = yt.streams[16]
# print(stream)
# stream.download(storage_dir_audio)
#print(datetime.now())
# yt.streams.filter(res="720p",mime_type="video/mp4",progressive="True").first().download(storage_dir) 
if os.path.exists(storage_dir_output):
    print("ll")
    print(yt.streams.filter(res="360p",mime_type="video/mp4",progressive="True").size())
    #yt.streams.filter(mime_type="video/mp4",progressive="True").first().download(storage_dir_output)
else:
    print('ddd')
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

