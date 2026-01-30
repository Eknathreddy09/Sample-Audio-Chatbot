# GenAI Conversational Voice Chatbot

This repo contains a simple voice-based conversational chatbot built using **Streamlit** and **OpenAI APIs**.

The idea is straightforward:
- speak into the browser
- convert speech to text
- generate a response using an LLM
- convert the response back to speech
- play it automatically

This was put together mainly as a **POC / demo app** to test voice-based GenAI workflows and see how well they work on platforms like Cloud Foundry.

---

## What this app does

- Records voice input from the browser
- Uses OpenAI Whisper for speech-to-text
- Sends the conversation to an OpenAI chat model
- Converts the response to audio using OpenAI TTS
- Plays the audio response automatically in the UI
- Maintains chat history for the session

Nothing fancy, but enough to demonstrate end-to-end voice interaction.

---

## Tech stack

- Python 3.x
- Streamlit
- OpenAI Python SDK
- audio-recorder-streamlit

---



