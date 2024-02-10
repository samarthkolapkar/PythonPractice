from moviepy.editor import VideoFileClip
from google.cloud import speech

def extract_audio(video_path, output_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_path)

def transcribe_audio(audio_path):
    client = speech.SpeechClient()

    with open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    transcripts = []
    for result in response.results:
        transcripts.append(result.alternatives[0].transcript)

    return transcripts

# Paths to video and audio files
video_path = "C:/Users/samar/Downloads/17. DataFrame Functions_ Limit in Databricks _ Databricks Tutorial for Beginners _ Azure Databricks.mp4"
audio_path = "C:/Users/samar/Downloads/output1.mp3"

# Convert video to audio
extract_audio(video_path, audio_path)

# Transcribe audio to text
transcriptions = transcribe_audio(audio_path)
for transcript in transcriptions:
    print(transcript)
