from moviepy.editor import VideoFileClip

videoName = input("What is the video name? (include file extension) ")

video = VideoFileClip(videoName)

startOfVideo = input("Start of the video: ")
endOfVideo = input("End of the video: ")

startOfVideo = int(startOfVideo)
endOfVideo = int(endOfVideo)

video = video.subclip(startOfVideo, endOfVideo)

video.write_videofile("CLIPPED.mp4")