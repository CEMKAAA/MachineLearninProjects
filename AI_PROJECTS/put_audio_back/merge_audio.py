from pydub import AudioSegment

def overlay_audio_files(background_file, foreground_file, output_file):
    # Load the background and foreground audio files
    background_audio = AudioSegment.from_file(background_file)
    foreground_audio = AudioSegment.from_file(foreground_file)

    # Ensure both audio files have the same number of channels (stereo/mono)
    if background_audio.channels != foreground_audio.channels:
        foreground_audio = foreground_audio.set_channels(background_audio.channels)

    # Ensure both audio files have the same frame rate (sample rate)
    if background_audio.frame_rate != foreground_audio.frame_rate:
        foreground_audio = foreground_audio.set_frame_rate(background_audio.frame_rate)

    # Overlay the foreground audio on the background audio
    mixed_audio = background_audio.overlay(foreground_audio)

    # Export the mixed audio to the output file
    mixed_audio.export(output_file, format="mp3")  # Change format as needed

# Example usage
background_file = "C:/Users/Cem/Videos/youtube/1_dieinafire_(Instrumental).wav"
foreground_file = "C:/Users/Cem/Downloads/audio (1).wav"
output_file = "C:/Users/Cem/Videos/youtube/ihopeyou3.wav"

overlay_audio_files(background_file, foreground_file, output_file)

