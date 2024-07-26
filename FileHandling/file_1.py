#open() function -> filename,mode(r,w,a...)

# file_read=open('calculator.py','r')
# print(file_read.read())

import os
def CreateFile(fileName):
   # fileName=fileread.py
    if(os.path.exists(fileName)): #True
     print('File is already exists')
    else:
       file_create=open(fileName,'w')
     

def main():
    print('Enter the file name you want to create')
    file_name=input()  #calculator.py


    CreateFile(file_name)

if __name__=="__main__":
    main()

