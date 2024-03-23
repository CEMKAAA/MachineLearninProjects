from pytube import YouTube
import subprocess
import os

def download_and_crop_video(url, save_path, start_time, end_time):
    try:
        # Download the entire YouTube video
        yt = YouTube(url)
        itag = 18  # Set the itag for the desired resolution (18 is usually 360p)

        # Get the stream with the specified itag
        stream = yt.streams.get_by_itag(itag)
        temp_video_path = os.path.join(save_path, "temp_video.mp4")
        stream.download(output_path=save_path, filename="temp_video")

        # Use ffmpeg to trim the video
        subprocess.run(["ffmpeg", "-i", temp_video_path, "-ss", str(start_time), "-to", str(end_time),
                        "-c", "copy", os.path.join(save_path, "cropped_video.mp4")])

        print("Video downloaded and cropped successfully")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    video_url = input("Please enter a YouTube URL: ")
    start_time = float(input("Please enter the start time (in seconds): "))
    end_time = float(input("Please enter the end time (in seconds): "))

    save_dir = input("Please enter the save directory: ")

    download_and_crop_video(video_url, save_dir, start_time, end_time)