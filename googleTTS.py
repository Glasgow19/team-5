from google.cloud import texttospeech
import base64
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'CS317-GroupProject-d32ac6832124.json'
# Instantiates a client
client = texttospeech.TextToSpeechClient()
def tts(str):
    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=str)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US-Wavenet-F',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    print(response)
    response = base64.b64encode(response.audio_content)
    return response
