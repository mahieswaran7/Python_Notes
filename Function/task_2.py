def sum_function(list1,size):
    sum=0
    for i in range(size):
        sum=sum+list1[i]
    return sum

def max_function(list1,size):
    max1=0
    for i in range(size):
        if(list1[i]>max1):
            max1=list1[i]
    return max1


def main():
    choice= int(input("enter your choice"))
    list1=[]
    size=int(input("enter the size: "))
    for i in range(size):
        value=int(input("enter the value: "))
        list1.append(value)
    while(True):
        if(choice==1):
           print(sum_function(list1,size))
           break
        elif(choice==2):
            print(max_function(list1,size))
            break
        else:
            print("you have enter the wrong choice")
            break



if __name__=="__main__":
    main()