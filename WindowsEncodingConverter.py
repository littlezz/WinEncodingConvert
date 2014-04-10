import sys
import os

filePath=sys.argv[1]
scriptName=sys.argv[0]
print(format('filepath:','<10'),filePath)
print(format('scriptname:','<10'),scriptName)

with open(filePath,'r',encoding="cp936") as f:
    with open('u'+os.path.basename(filePath),'w',encoding='utf-8')as nf:
        nf.write(f.read())

