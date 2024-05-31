import os
import sys


# removes any files that dont end with .mp4 and .txt
#effectivly gets rid of anything that is not the reel itself, its caption, and its comments
def clean(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            #print(not file.lower().endswith(".mp4"))
            if not (file.lower().endswith(".mp4") or file.lower().endswith(".py")):
                   # or file.lower().endswith(".txt") or file.lower().endswith(".py")):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f'Deleted {file_path}')

directory = sys.argv[1]
clean(directory)
#     #if len(sys.argv) == 0:
#         print("Usage: python cleaner.py <directory> <extension>")
#     print("Example: python cleaner.py ./images .jpg")
# else:
