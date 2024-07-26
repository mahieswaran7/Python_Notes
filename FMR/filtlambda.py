#write a program whuch will check the number is greater and equal to 
#70 and less than and equal to 90


def main():
    size=int(input('Enter the size:'))
    lst=[]
    print("Enter the values:")
    for i in range(size):
        value=int(input())
        lst.append(value)
    print('User List :',lst)
    filter_list=list(filter(lambda number: number>70 and number <80 ,lst))
    print("filtered list is :",filter_list)


if __name__=='__main__':
    main()   