
from pydub import AudioSegment

from os import walk,mkdir
from os.path import join
from os import listdir
from os.path import isfile, isdir, join

# 指定要列出所有檔案的目錄
mypath = "7.1音檔/7.1U音檔"

# 遞迴列出所有檔案的絕對路徑
for root, dirs, files in walk(mypath):
    for f in files:
        if f.split(".")[-1] == "wav":
            fullpath=join(root, f)#fullpath input file path
            #print(fullpath)
            sound = AudioSegment.from_wav(fullpath)
            sound = sound.set_frame_rate(16000)
            output_path=join(mypath,"16KWav/")
            #print(output_path)
            if not isdir(output_path):
                mkdir(output_path)#做一個資料夾
            filePath=join(output_path, root.split("\\")[-1])
            if not isdir(filePath):
                mkdir(filePath)
            sound.export(join(filePath,f), format="wav")




