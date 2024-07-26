import os
import filecmp
def comparefiles(file_01,file_02):
    if(not os.path.exists(file_01)):
        print(file_01,'File Not Exists')
    elif(not os.path.exists(file_02)):
        print(file_02,"File Not Exists") 
    else:
        compare = filecmp.cmp(file_01,file_02)       
        if compare==True:
            print('Success-> The files are same')
        else:
            print('Failure -> The files are different')


def main():
    file_01=input("Enter the first file :")
    file_02=input("Enter the second file :")

    comparefiles(file_01,file_02)


if __name__=='__main__':
    main()
    #Welcome to the Python session by Kasturi Mam