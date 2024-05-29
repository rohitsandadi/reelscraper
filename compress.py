import os
import sys
import subprocess

def compress_videos(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            #print(not file.lower().endswith(".mp4"))
            if (file.lower().endswith(".mp4")):
                file_path = os.path.join(root, file)
                new_file_path = os.path.splitext(file_path)[0] + "compressed"+ '.mp4'
                #output_path = os.path.join(file_path, f'compressed_{file}' )
                #ffmpeg_cmd = f'ffmpeg -i {file_path} -c:v libx264 -c:a copy -crf 35 {new_file_path}'
                #ffmpeg_cmd = f'ffmpeg -i {file_path} -c:v libx264  -pix_fmt yuv420p -crf 28 -preset fast -tune zerolatency -c:a aac {new_file_path}'
                ffmpeg_cmd = f'ffmpeg -i {file_path} -c:v libx264 -pix_fmt yuv420p -crf 35 -vf scale=-1:720 {new_file_path}'
                subprocess.run(ffmpeg_cmd, shell=True)

directory = sys.argv[1]
compress_videos(directory)


