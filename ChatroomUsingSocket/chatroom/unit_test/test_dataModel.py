import sys
sys.path.append('D:\Code\LearnPython\socket\chatroom')
import dataModel
import time

print(time.time())
data = dataModel.TransData('小明')
print(data.toString())