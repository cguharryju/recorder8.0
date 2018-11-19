
from pydub import AudioSegment

from os import walk,mkdir
from os.path import join
from os import listdir
from os.path import isfile, isdir, join
import string
import csv

# 指定要列出所有檔案的目錄
mypath = "Speech_data"

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
        list.append(join("/"+mypath+"/",word))
#print(list[])

# 遞迴列出所有檔案的絕對路徑
filename = "mycsvfile.csv"
# opening the file with w+ mode truncates the file
f = open(filename, "w+")
f.close()

for path in list[2:]:
    print(path)
    for root, dirs, files in walk(path):
        fileNameAll=""
        userName = {}
        allNum=0

        for f in files:
            if f.split(".")[-1] =="wav" :
                allNum+=1
                if f.split("_")[0] == "TX001":
                    # print(f.split("_")[3])
                    if f.split("_")[3] in userName.keys():
                        userName[f.split("_")[3]]+=1


                    else:
                        userName[f.split("_")[3]] = 1

                else:
                    if f.split("_")[1] in userName.keys():
                        userName[f.split("_")[1]] += 1
                    else:
                        userName[f.split("_")[1]] = 1

        #print(userName)
        #print("個數:",allNum)
        with open('mycsvfile.csv', 'a',newline='') as f:  # Just use 'w' mode in 3.x
            ''''
            w = csv.DictWriter(f, userName.keys())
            w.writerow(userName.keys())
            w.writerow(userName)
            '''
            writer = csv.writer(f)

            writer.writerow(path.split("/")[-1])
            writer.writerow(userName.keys())
            writer.writerow(userName.values())
#print(fileNameAll)




