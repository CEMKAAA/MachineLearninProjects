from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import random

def get_random_30_seconds(input_video, output_video):
    try:
        # Load the video clip
        video_clip = VideoFileClip(input_video)

        # Get the duration of the video in seconds
        total_duration = video_clip.duration

        # Ensure that the video is at least 30 seconds long
        if total_duration < 10:
            raise ValueError("Video duration is less than 30 seconds.")

        # Generate a random start time within the valid range
        start_time = random.uniform(0, total_duration - 30)

        # Extract a 30-second segment starting from the random time
        ffmpeg_extract_subclip(input_video, start_time, start_time + 10, targetname=output_video)

        print(f"Random 30-second video saved as '{output_video}'")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
input_video_path = "C:/Users/Cem/Videos/youtube/AH.mp4"
output_video_path = "C:/Users/Cem/Videos/youtube/ahcorped.mp4"

get_random_30_seconds(input_video_path, output_video_path)
