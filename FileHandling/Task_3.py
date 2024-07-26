import os 
def append_file(name,added):
    if(os.path.exists(name)):
        to_write=open(name,'a')
        to_write.write(added)
        print("contents are written")
    else:
        print("file does not exist")


def main():
    to_be_added=input("enter the contents you want to add: ")
    file_name=input("enter the filename: ")
    append_file(file_name,to_be_added)

if __name__ =="__main__":
    main()