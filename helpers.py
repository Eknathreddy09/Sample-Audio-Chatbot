import os
import base64
import tempfile
import streamlit as st
from openai import OpenAI

# ----------------------------------
# OpenAI client (API key via env var)
# ----------------------------------
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# ----------------------------------
# Speech → Text (Whisper)
# ----------------------------------
def speech_to_text(audio_file_path: str) -> str:
    try:
        with open(audio_file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )

        return transcription.text

    except Exception as e:
        st.error(f"Speech-to-text failed: {e}")
        return ""


# ----------------------------------
# Text → Speech (TTS)
# ----------------------------------
def text_to_speech(text: str) -> str:
    try:
        # Create temp audio file
        tmp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")

        # OpenAI TTS call (IMPORTANT PART)
        response = client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=text
        )

        # ✅ Correct way to write audio
        audio_bytes = response.read()
        tmp_audio.write(audio_bytes)
        tmp_audio.close()

        return tmp_audio.name

    except Exception as e:
        st.error(f"Text-to-speech failed: {e}")
        return ""


# ----------------------------------
# Autoplay audio in Streamlit
# ----------------------------------
def autoplay_audio(audio_path: str):
    if not audio_path:
        return

    with open(audio_path, "rb") as f:
        audio_bytes = f.read()

    b64 = base64.b64encode(audio_bytes).decode()

    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    st.markdown(audio_html, unsafe_allow_html=True)

