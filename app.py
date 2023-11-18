## simple app for json -> TTS with combining possibility
# Import necessary libraries
import streamlit as st
import json
import openai
from openai import OpenAI
from pydub import AudioSegment
from pathlib import Path
from elevenlabs import generate, stream, set_api_key, Voice, VoiceSettings


# Load OpenAI API Key
OPENAI_API_KEY = "api-key"
set_api_key("eleven-labs-api-key")

client = OpenAI(api_key=OPENAI_API_KEY)

johnny="voice_id"
michael="voice_id"
karolina="voice_id"
narrator="voice_id"

def parse_json(file_content):
    """Parse the uploaded JSON file and extract dialogues."""
    try:
        data = json.loads(file_content)
        return [(item["name"], item["message"]) for item in data]
    except json.JSONDecodeError:
        st.error("Invalid JSON file.")
        return []

def voice_selector(name, tts_service):
    """Select a voice based on character name and TTS service."""
    if tts_service == 'openai':
        voices = {'Johnny': 'onyx', 'Michael': 'alloy', 'Karolina': 'nova', 'Narrator': 'echo'}
        return voices.get(name, 'nova')  # Fallback to 'nova' if name not found
    elif tts_service == 'elevenlabs':
        voices = {'Johnny': johnny, 'Michael': michael, 'Karolina': karolina, 'Narrator': narrator}
        return voices.get(name, '[default_voice_id]')  # Default voice for Eleven Labs
    else:
        return None

def text_to_audio(dialogues, tts_service):
    """Convert text to audio using selected TTS service."""
    audio_file_paths = []
    for character, dialogue in dialogues:
        voice_id = voice_selector(character, tts_service)

        if tts_service == 'openai':
            response = client.audio.speech.create(
                model="tts-1",
                voice=voice_id,
                input=dialogue
            )
            audio_file_path = Path(f"{character}_speech_{len(audio_file_paths)}.mp3")
            response.stream_to_file(audio_file_path)
        elif tts_service == 'elevenlabs':
            audio_generator = generate(
                text=dialogue,
                model="eleven_multilingual_v2",
                stream=True,
                voice=Voice(
                    voice_id=voice_id,
                    settings=VoiceSettings(stability=0.37, similarity_boost=0.73, style=0.0, use_speaker_boost=True)
                )
            )
            audio_file_path = Path(f"{character}_speech_{len(audio_file_paths)}.mp3")
            with open(audio_file_path, 'wb') as file:
                for chunk in audio_generator:
                    file.write(chunk)
        
        audio_file_paths.append(audio_file_path)
    return audio_file_paths

def combine_audio_files(file_paths):
    """Combine multiple audio files into one."""
    combined = AudioSegment.empty()
    for file_path in file_paths:
        audio = AudioSegment.from_mp3(file_path)
        combined += audio
    return combined

st.title("Novel Narration App from JSON")

tts_service = st.radio("Select TTS Service", ('openai', 'elevenlabs'))
uploaded_file = st.file_uploader("Upload a JSON file", type=["json"])
if uploaded_file is not None:
    content = uploaded_file.getvalue().decode("utf-8")
    dialogues = parse_json(content)

    if dialogues:
        st.write("Generating audio...")
        audio_file_paths = text_to_audio(dialogues, tts_service)
        combined_audio = combine_audio_files(audio_file_paths)

        # Save and display the combined audio
        combined_audio_path = "combined_audio.mp3"
        combined_audio.export(combined_audio_path, format="mp3")
        st.audio(combined_audio_path, format="audio/mp3")

st.text("Here is JSON structure which is acceptable:")
st.code("""[
    {
        "name": "Karolina",
        "message": "Once upon a modern day in our bustling city, there was a man named Bob, a dear friend of mine, known for his gentle heart and shy smile. However, despite his many qualities, Bob faced a dilemma that many brave souls encounter: the quest for love."
    },
    {
        "name": "Karolina",
        "message": "I, Karolina, decided to rally the troops – our diverse group of friends – to aid Bob in this noble pursuit. Among us were Michael, with his quirky wisdom, and Johnny, a man whose advice always sounded like it was straight out of a cyberpunk novel."
    },
    {
        "name": "Michael",
        "message": "Bob, my man, your journey to love is like Scranton Business Park, but instead of businesses, it's all about love and attraction."
    },
...
]""")