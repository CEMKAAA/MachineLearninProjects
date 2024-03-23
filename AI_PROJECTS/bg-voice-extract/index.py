from pydub import AudioSegment
from pydub.playback import play

def extract_audio(input_video_path, output_audio_path):
    # Load video and extract audio
    video = AudioSegment.from_file(input_video_path)

    # Save audio as WAV
    video.export(output_audio_path, format="wav")

if __name__ == "__main__":
    input_video_path = "C:/Users/Cem/Videos/youtube/ahcorped.mp4"
    output_audio_path = "C:/Users/Cem/Videos/youtube/WAV/AH.wav"

    extract_audio(input_video_path, output_audio_path)
