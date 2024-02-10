from google.cloud import speech

def transcribe_audio(audio1):
    client = speech.SpeechClient()

    with open(audio1, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,  # Replace with the sample rate of your audio
        language_code="en-US",    # Replace with the desired language code
    )

    response = client.recognize(config=config, audio=audio)

    transcripts = []
    for result in response.results:
        transcripts.append(result.alternatives[0].transcript)

    return transcripts

# Path to your audio file
audio_path = "C:/Users/samar/Downloads/output1.mp3"

# Transcribe audio to text
transcriptions = transcribe_audio(audio_path)
for transcript in transcriptions:
    print(transcript)
