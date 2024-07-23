def main():
  String=input("enter the string: ")
  for i in range(len(String)-1):
    count=1
    for j in range(i+1,len(String)):
        if(String[i]==String[j]):
           count+=1
    print(f'{String[i]} is repeated {count}')





if __name__=="__main__":
    main()