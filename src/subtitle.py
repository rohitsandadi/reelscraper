import os
import sys
import whisper

model = whisper.load_model("medium")
def transcribe_videos(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if (file.lower().endswith(".mp4")):
                dir = os.getcwd()
                dir = dir[:-len(file)]

                audio = file
                result = model.transcribe(audio)
                with open("transcription.txt", "a") as txt:
                    txt.write(result["text"])

directory = sys.argv[1]
transcribe_videos(directory)

