import os
import sys
import whisper
import subprocess
import shlex

model = whisper.load_model("medium")
def transcribe_videos(directory):
    if not(os.path.exists("/Users/rohitsandadi/PycharmProjects/reelsscraper/transcriptions")):
        os.mkdir("/Users/rohitsandadi/PycharmProjects/reelsscraper/transcriptions")
        print("transcription folder created --> transcriptions will be in here")
    for root, dirs, files in os.walk(directory):
        count = 1
        old_path = ""
        for file in files:
            if (file.lower().endswith(".mp4")):
                audio_path = os.path.join(root, file)
                output_path = audio_path[(len(directory)+1):]
                output_path = output_path[:(output_path.find(file)-1)]
                print(output_path)
                if not (old_path == output_path):
                    count=1
                if(os.path.exists("./transcriptions/"+output_path+"_"+ str(count)+".txt")): #seeing if the file was already subtitled
                    continue
                old_path = output_path
                command = f"python audiototext.py {audio_path} --model small --output_formats txt --output_dir transcriptions"
                args = shlex.split(command)
                subprocess.run(args)
                original = "./transcriptions/"+file[:(file.find(".mp4"))]+".txt"
                new = "./transcriptions/"+output_path+"_"+str(count)+".txt"
                print(new)
                os.rename(original, new)

                count = count+1

directory = sys.argv[1]
transcribe_videos(directory)

