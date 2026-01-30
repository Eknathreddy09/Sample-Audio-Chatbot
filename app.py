import streamlit as st
import os

from helpers import text_to_speech, autoplay_audio, speech_to_text
from generate_answer import base_model_chatbot
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *

def main():
    float_init()

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! How may I assist you today?"}
        ]

    st.title("A Simple Audio Chatbot :) ")

    # Footer mic
    footer_container = st.container()
    with footer_container:
        audio_bytes = audio_recorder()

    # Chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Voice input
    if audio_bytes:
        with st.spinner("Transcribing..."):
            audio_file = "temp_input_audio.wav"
            with open(audio_file, "wb") as f:
                f.write(audio_bytes)

            transcript = speech_to_text(audio_file)
            os.remove(audio_file)

            if transcript:
                st.session_state.messages.append(
                    {"role": "user", "content": transcript}
                )
                with st.chat_message("user"):
                    st.write(transcript)

    # LLM response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking 🤔"):
                response = base_model_chatbot(st.session_state.messages)

            with st.spinner("Generating audio 🔊"):
                audio_path = text_to_speech(response)
                autoplay_audio(audio_path)
                os.remove(audio_path)

            st.write(response)
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )

    footer_container.float("bottom: 0rem;")

if __name__ == "__main__":
    main()

