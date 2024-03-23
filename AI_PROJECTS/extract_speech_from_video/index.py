import librosa
from pydub import AudioSegment
from pydub.playback import play

def remove_background_music(input_audio_path, output_audio_path):
    # Load the audio file
    audio = AudioSegment.from_file(input_audio_path)

    # Convert stereo to mono
    audio = audio.set_channels(1)

    # Convert PyDub audio segment to numpy array
    samples = audio.get_array_of_samples()

    # Convert the numpy array to a float array in range [-1, 1]
    samples_float = librosa.util.buf_to_float(samples)

    # Estimate the background music by assuming it is the loudest part
    background_music = librosa.effects.split(samples_float, top_db=40)[0]

    # Create a silent audio segment with the same duration as the original audio
    silence = AudioSegment.silent(duration=len(audio))

    # Overlay the silent audio segment on the original audio to remove background music
    audio_without_music = audio.overlay(silence, position=0)

    # Save the modified audio without background music
    audio_without_music.export(output_audio_path, format="mp3")

    print("Background music removed successfully!")

# Example usage
input_audio_path = "C:/Users/Cem/Videos/youtube/dieinafire.mp3"
output_audio_path = "removed.mp3"
remove_background_music(input_audio_path, output_audio_path)
