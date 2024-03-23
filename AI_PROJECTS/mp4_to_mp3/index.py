from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def convert_mp4_to_mp3(video_path, output_path):
    try:
        # Load video clip
        video_clip = VideoFileClip(video_path)

        # Extract audio from the video
        audio_clip = video_clip.audio

        # Write the audio to an MP3 file
        audio_clip.write_audiofile(output_path, codec='mp3')

        print(f"MP3 file saved as '{output_path}'")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
video_path = "C:/Users/Cem/Videos/youtube/Die In a Fire.mp4"
output_path = "C:/Users/Cem/Videos/youtube/dieinafire.mp3"

convert_mp4_to_mp3(video_path, output_path)
