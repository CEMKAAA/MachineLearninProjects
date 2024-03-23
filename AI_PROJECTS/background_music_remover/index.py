from moviepy.editor import VideoFileClip

def mute_background_audio(video_path, output_path):
    try:
        # Load video clip
        video_clip = VideoFileClip(video_path)

        # Mute the audio
        video_clip = video_clip.set_audio(None)

        # Write the result to a new video file
        video_clip.write_videofile(output_path, codec='libx264')

        print(f"Background audio muted and video saved as '{output_path}'")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
video_path = "C:/Users/Cem/Videos/youtube/output.mp4"
output_path = "C:/Users/Cem/Videos/youtube/output_without_background.mp4"

mute_background_audio(video_path, output_path)

