from moviepy.editor import VideoFileClip, AudioFileClip, vfx
from pydub import AudioSegment

def overlay_audio(video_path, audio_path, output_path, audio_volume=1.0):
    try:
        # Load video clip
        video_clip = VideoFileClip(video_path)

        # Load audio clip
        audio_clip = AudioFileClip(audio_path)

        # Set the volume level of the audio clip
        adjusted_audio = audio_clip.volumex(audio_volume)

        # Make the video as long as the audio
        video_duration = video_clip.duration
        audio_duration = audio_clip.duration

        # If video is shorter than audio, loop the video
        if video_duration < audio_duration:
            video_clip = video_clip.fx(vfx.loop, duration=audio_duration)

        # If audio is shorter than video, trim the video
        elif video_duration > audio_duration:
            video_clip = video_clip.subclip(0, audio_duration)

        # Overlay the audio on the video
        video_clip = video_clip.set_audio(adjusted_audio)

        # Write the result to a new video file
        video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

        print(f"Audio overlaid and video saved as '{output_path}'")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
video_path = "C:/Users/Cem/Download/audio.wav"
audio_path = "C:/Users/Cem/Videos/youtube/ballin.mp3"
output_path = "C:/Users/Cem/Videos/youtube/ballin_mine_with_audio.mp4"
audio_volume = 0.6  # Adjust the volume level (0.0 to 1.0)

overlay_audio(video_path, audio_path, output_path, audio_volume)

