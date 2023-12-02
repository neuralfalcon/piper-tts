
#Full Tutorial at https://youtu.be/GGvdq3giiTQ?si=U_Q44F0G5fRDpYqH
#Download  piper_windows_amd64.zip  from https://github.com/rhasspy/piper/releases/ 
#Download .onnx and .json file from https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0
#pip install SpeechRecognition
#pip install pyglet
#pip install rich

#play the output on your laptop speaker or desktop default speaker 
#enable stereo mix on windows
# in google meet  use stereo mix as mic 
#in google meet  use extra blutooth headphone as speaker

#you can use it whatsapp desktop , zoom etc

import os

import speech_recognition as sr


from time import sleep
import pyglet
from rich.console import Console

console = Console()
console.print("""[bold green]Available Language:[/bold green]
   1.English
   2.Hindi
   3.Bengali
   4.French 
   5.Spanish 
   6.Portuguese 
   7.Chinese
   8.Japanese 
   9.Indonesian 
   10.Russian 
"""
,style="blue")

lang_code={
    1:"en",
    2:"hi",
    3:"bn",
    4:"fr",
    5:"es",
    6:"pt",
    7:"zh-CN",
    8:"ja",
    9:"id",
    10:"ru" 
}

console.print("Choose Input language: " ,style="bold red")
input_lang_code=int(input())

output_lang_code=1
input_lang = lang_code[input_lang_code]
output_lang=lang_code[output_lang_code]

from googletrans import Translator
translator = Translator()
def trans(mytext):
    result = translator.translate(mytext,dest="en")
    return str(result.text)

















####---------------------------------------


import os
import subprocess
import pyglet
from time import sleep
def music_play(file_name):
    music = pyglet.media.load(file_name, streaming=False)
    music.play()
    sleep(music.duration)
    os.remove(file_name) 

def replace_path(path):
    format_path = path.replace("/", "\\")
    format_path = rf"{format_path}"
    return format_path 


copy_voice_model_path = "voice/kusal/en_US-kusal-medium.onnx"
copy_voice_config_path = "voice/kusal/en_en_US_kusal_medium_en_US-kusal-medium.onnx.json"

voice_model_path=replace_path(copy_voice_model_path)
voice_config_path=replace_path(copy_voice_config_path)
# voice_model_path = r".{\voice\kusal\en_US-kusal-medium.onnx}"
# voice_config_path = r".\voice\kusal\en_en_US_kusal_medium_en_US-kusal-medium.onnx.json"


def tts(text, output_file):
    command = f'echo "{text}" | .\\piper.exe -m {voice_model_path} -c {voice_config_path} -f {output_file}'
    subprocess.run(command, shell=True)

output_file = "temp.wav"

##--------------------------------------





r = sr.Recognizer()
console.print("\nPlease Start talking:\n",style="bold red")  
while(1):	
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2,language=input_lang)
            MyText = MyText.lower()
            # print("Input text: "+MyText)
            console.print(f"[bold green]Input text:[/bold green] {MyText}",style="yellow")
            if input_lang!="en":
                trans_text=trans(MyText)
            else:
                trans_text=MyText
            console.print(f"[bold pink]Input text:[/bold pink] {trans_text}",style="green")
            tts(trans_text, output_file)
            music_play(output_file)		
    except sr.RequestError as e:
        pass
        
    except sr.UnknownValueError:
        pass
