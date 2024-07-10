import cairosvg
from moviepy.editor import ImageSequenceClip

# Convert SVG to PNG
cairosvg.svg2png(url="image1.svg", write_to="frame1.png")
cairosvg.svg2png(url="image2.svg", write_to="frame2.png")

# Create a list of frames
frames = ["frame1.png", "frame2.png"]

# Create a video from the frames
clip = ImageSequenceClip(frames, fps=1)  # Adjust fps to control the speed of the video
clip.write_videofile("output_video.mp4", codec="libx264")