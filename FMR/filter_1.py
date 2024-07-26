#write a program whuch will check the number is greater and equal to 
#70 and less than and equal to 90

def Check_number(Number):
    if(Number>=70 and Number<=90):
        return Number

def main():
    size=int(input('Enter the size :'))
    lst=[]
    print('enter values')
    for i in range(size):
        value=int(input())
        lst.append(value)
    print('User List:',lst)

    filter_list=list(filter(Check_number,lst))
    print('Filter list:',filter_list)

if __name__=="__main__":
    main()    

