import streamlit as st

textTS = "hello, welcome to the future of metaverse"
 
from gtts import gTTS
from IPython.display import Audio
tts = gTTS(textTS)
#tts = gTTS(textTS, lang="en-US")
tts.save('1.wav')
sound_file = '1.wav'
Audio(sound_file, autoplay=True)
