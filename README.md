# GenAI Conversational Voice Chatbot

This repo contains a simple voice-based conversational chatbot built using **Streamlit** and **OpenAI APIs**.

The idea is straightforward:
- speak into the browser
- convert speech to text
- generate a response using an LLM
- convert the response back to speech
- play it automatically

---

## What this app does

- Records voice input from the browser
- Uses OpenAI Whisper for speech-to-text
- Sends the conversation to an OpenAI chat model
- Converts the response to audio using OpenAI TTS
- Plays the audio response automatically in the UI
- Maintains chat history for the session

Nothing fancy, but enough to demonstrate end-to-end voice interaction.


export OPENAI_API_KEY=sk-xxxx

git clone https://github.com/Eknathreddy09/Sample-Audio-Chatbot && cd Sample-Audio-Chatbot

cf push 

cf set-env genai-voice-chatbot OPENAI_API_KEY sk-xxxx

cf restart genai-voice-chatbot

