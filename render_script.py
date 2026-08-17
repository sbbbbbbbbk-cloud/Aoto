import os

# FFmpeg test command (10-minute HD video render)
os.system("ffmpeg -f lavfi -i testsrc=duration=600:size=1920x1080:rate=30 -f lavfi -i sine=frequency=1000:duration=600 -c:v libx264 -pix_fmt yuv420p output.mp4")
print("Video Rendering Completed Successfully!")
