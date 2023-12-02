#Full Tutorial at https://youtu.be/GGvdq3giiTQ?si=U_Q44F0G5fRDpYqH
#Download  piper_windows_amd64.zip  from https://github.com/rhasspy/piper/releases/ 
#Download .onnx and .json file from https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0
#pip install pyglet
copy_voice_model_path = "voice/kusal/en_US-kusal-medium.onnx"
copy_voice_config_path = "voice/kusal/en_en_US_kusal_medium_en_US-kusal-medium.onnx.json"



import os
import subprocess
import pyglet
from time import sleep
def music_play(file_name):
    music = pyglet.media.load(file_name, streaming=False)
    music.play()
    sleep(music.duration)
    # os.remove(file_name) 

def replace_path(path):
    format_path = path.replace("/", "\\")
    format_path = rf"{format_path}"
    return format_path 



voice_model_path=replace_path(copy_voice_model_path)
voice_config_path=replace_path(copy_voice_config_path)
# voice_model_path = r".{\voice\kusal\en_US-kusal-medium.onnx}"
# voice_config_path = r".\voice\kusal\en_en_US_kusal_medium_en_US-kusal-medium.onnx.json"


def tts(text, output_file):
    command = f'echo "{text}" | .\\piper.exe -m {voice_model_path} -c {voice_config_path} -f {output_file}'
    subprocess.run(command, shell=True)

output_file = "temp.wav"
while True:
    text = input("Enter text: ")
    tts(text, output_file)
    music_play(output_file)


