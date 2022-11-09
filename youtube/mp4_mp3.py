from moviepy.editor import *


mp4 = "チョット (2019 Remastered).mp4"
mp3 = "チョット (2019 Remastered).mp3"

videoclip = VideoFileClip(mp4)

audioclip = videoclip.audio
audioclip.write_audiofile(mp3)
