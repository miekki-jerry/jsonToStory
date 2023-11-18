# Novel Narration App from JSON

## Introduction

Welcome to the Novel Narration App from JSON! This project is a simple, yet innovative application that transforms JSON-formatted dialogue into a fully narrated audio story. It's a fun and creative way to bring written narratives to life using the power of text-to-speech (TTS) technology. 

The app is built for writers, storytellers, and anyone interested in converting their written dialogues into engaging audio formats. It's particularly exciting for those looking to add an auditory dimension to their stories without the need for professional voice actors.


## Example output
https://github.com/miekki-jerry/jsonToStory/blob/main/exmple_output.mp3

NOTE:I'm using these voices only for personal usage. They are not my property.

https://github.com/miekki-jerry/jsonToStory/blob/main/SCR-20231118-k8t.png

![SCR-20231118-k8t](https://github.com/miekki-jerry/jsonToStory/assets/100033698/1a06434b-56ef-447e-80e5-72931d40e44c)

## Features

- **JSON to TTS Conversion**: Converts dialogues from JSON files into spoken words using advanced TTS services.
- **Multiple TTS Service Support**: Integrates with both OpenAI and ElevenLabs TTS services, offering a variety of voice options.
- **Dynamic Voice Selection**: Assigns different voices to characters based on the dialogue, enhancing the storytelling experience.
- **Audio Combination**: Merges individual dialogue pieces into a single, continuous audio file.
- **Streamlit Interface**: User-friendly web interface created with Streamlit, making it easy for anyone to use the app.

## Why It's Fun

- **Bring Stories to Life**: Listen to your written dialogues as if they're being performed by a cast of characters.
- **Experiment with Voices**: Play around with different voice options to find the perfect match for each character.
- **Easy to Use**: With a simple JSON upload, transform text into a captivating audio narrative.
- **Creative Exploration**: Ideal for writers and creators looking to explore new dimensions of storytelling.

## How It Works

1. **Upload JSON**: Users upload a JSON file containing dialogue structured in a specific format.
2. **Select TTS Service**: Choose between OpenAI and ElevenLabs for voice synthesis.
3. **Audio Generation**: The app processes each dialogue entry, assigning voices and generating audio.
4. **Combine and Play**: Individual audio files are combined into one and can be played directly from the app.

## JSON Structure Example

```json
[
    {
        "name": "Karolina",
        "message": "Once upon a modern day in our bustling city..."
    },
    {
        "name": "Michael",
        "message": "Bob, my man, your journey to love is like Scranton Business Park..."
    },
    ...
]
```
## Getting Started

1. Clone the repository.
2. Install dependencies (streamlit, json, openai, pydub, elevenlabs).
3. Set up API keys for OpenAI and ElevenLabs.
4. Set up voice_id for each voices.
5. Run the Streamlit app and start transforming your stories!
   ```streamlit run app.py```

## How to create json from story?
You can use my personal GPT's 
https://chat.openai.com/g/g-LNKK6KCcR-story-teller-from-problems

This program is part of a bigger picture but it's fun so I published.

## Conclusion

This Novel Narration App from JSON is a delightful tool for storytellers, scriptwriters, and anyone interested in converting text to speech in a creative way. It's a bridge between the written word and the world of audio storytelling, opening up new possibilities for narrative expression. Enjoy bringing your characters to life with just a few clicks!
