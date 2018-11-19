from  label_wav_dir import label_wav
from os import mkdir
from pydub import AudioSegment
from os.path import isdir, join
import string
import time
import os

acc=[]
fileIndex=input("輸入要篩選的檔案位置(會將其下之子目錄篩選Ex.Speech_data):")
fileDir=[]
fp = open('conv_labels.txt', "r",encoding = 'utf8')
lines = fp.readlines()
fp.close()
list = []
labels=[]
for i in range(0, len(lines), 1):  # (开始/左边界, 结束/右边界, 步长)
      ## 空列表, 将第i行数据存入list中
    for word in lines[i].split():
        word = word.strip(string.whitespace)
        labels.append(word)
        list.append(join("/"+fileIndex+"/",word))
#print(list)
countLabel=2

for FD in list[2:]:
    #print(FD)
    acc.extend(label_wav(FD, "conv_labels.txt", "/tmp/my_frozen_graph.pb", 'wav_data:0',
                             'labels_softmax:0', 3))
    for f in acc:
        #print(f.split('\\')[-1])
        fullpath= join(FD,(f.split('\\')[-1]))#fullpath input file path
        #print(fullpath)
        sound = AudioSegment.from_wav(fullpath)
        sound = sound.set_frame_rate(16000)
        output_path="/"+fileIndex+"/WavOK/"+labels[countLabel]
        #print(output_path)
        if not isdir("/"+fileIndex+"/WavOK/"):
            mkdir("/"+fileIndex+"/WavOK/")
        if not isdir(output_path):
            mkdir(output_path)#做一個資料夾
            sound.export(join(output_path,f.split('\\')[-1]), format="wav")
        else:
            sound.export(join(output_path, f.split('\\')[-1]), format="wav")
    acc.clear()
    countLabel+=1

#wav_dir, labels, graph, input_name, output_name, how_many_labels