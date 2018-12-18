import os

os.chdir(r'C:\Users\student\cham\SSAFY지원자') # 해당 폴더로 이동함. r=raw

for filename in os.listdir("."): # . = 현재 폴더
     after_name = filename.replace("Samsung", "SSAFY")
     os.rename(filename, after_name) # os.rename
