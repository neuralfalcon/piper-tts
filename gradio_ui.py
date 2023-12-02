#Full Tutorial at https://youtu.be/GGvdq3giiTQ?si=U_Q44F0G5fRDpYqH
#Download  piper_windows_amd64.zip  from https://github.com/rhasspy/piper/releases/ 
#Download .onnx and .json file from https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0
#pip install pyglet
#pip install gradio


copy_voice_model_path = "voice/kusal/en_US-kusal-medium.onnx"
copy_voice_config_path = "voice/kusal/en_en_US_kusal_medium_en_US-kusal-medium.onnx.json"


import os
import subprocess


def replace_path(path):
    format_path = path.replace("/", "\\")
    format_path = rf"{format_path}"
    return format_path 



voice_model_path=replace_path(copy_voice_model_path)
voice_config_path=replace_path(copy_voice_config_path)
# voice_model_path = r".{\voice\kusal\en_US-kusal-medium.onnx}"
# voice_config_path = r".\voice\kusal\en_en_US_kusal_medium_en_US-kusal-medium.onnx.json"
if os.path.exists("audio"):
    print("audio folder already exists")
else:
    os.mkdir("audio")

import uuid
import re

def format_name(text):
    if text.endswith("."):
        text = text[:-1]

    text = text.lower()
    text = text.strip()

    # Replace non-alphabetic characters with a single underscore
    text = re.sub('[^a-z]+', '_', text)

    return text


def tts_file_name(text):
    text = format_name(text)
    truncated_text = text[:25] if len(text) > 25 else text if len(text) > 0 else "empty"
    random_string = uuid.uuid4().hex[:8].upper()
    file_name = f"audio/{truncated_text}_{random_string}.wav"
    return file_name

def tts(text):
    output_file=tts_file_name(text)
    command = f'echo "{text}" | .\\piper.exe -m {voice_model_path} -c {voice_config_path} -f {output_file}'
    result =subprocess.run(command, shell=True)
    if result.returncode == 0:
        print("Command executed successfully!")
        return output_file
    else:
        print(f"Command failed with return code {result.returncode}")
        return None

    

import pyglet
from time import sleep
def music_play(file_name):
    music = pyglet.media.load(file_name, streaming=False)
    music.play()
    sleep(music.duration)
    # os.remove(file_name) 
    


# text = "hi guys welcome to my channel"
# output_file=tts_file_name(text)
# tts(text, output_file)
# music_play(output_file)


import gradio as gr
import os
iface = gr.Interface(fn = tts,
                     inputs = 'text',
                     outputs = 'audio', 
                     verbose = True,
                     title = 'Text to speech',
                    )

iface.launch()
