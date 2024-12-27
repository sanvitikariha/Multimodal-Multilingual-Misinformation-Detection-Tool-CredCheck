# audio_to_text.py
import speech_recognition as sr
from pydub import AudioSegment
import os

def convert_to_wav(audio_file):
    file_extension = os.path.splitext(audio_file)[1].lower()
    if file_extension != '.wav':
        audio = AudioSegment.from_file(audio_file)
        wav_file = os.path.splitext(audio_file)[0] + '.wav'
        audio.export(wav_file, format='wav')
        return wav_file
    return audio_file

def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    wav_file = convert_to_wav(audio_file)
    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"