import moviepy.editor
from tkinter.filedialog import *
vid = askopenfile()
video = moviepy.editor.VideoFileClip("E:\css with anju bhaiya\CSS Transforms _ Scale_ Translate_ Skew and Rotate _ Web Development Course _32(720P_HD).mp4")
aud = video.audio
aud.write_audiofile("demo.mp3")
print("-----End-----")