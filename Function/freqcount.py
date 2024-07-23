def count_num(lst,number):

    count = 0
    for i in lst:
        if(i==number):
            count += 1
    return count 


#dynamic input


def main():
    print('Enter the size of the list ')
    size = int(input())
    data_input=[]
    print('Enter the values:')
    for i in range(size):#4
        value = int(input())
        data_input.append(value)
    print('User List:',data_input)

    SearchNum= int(input('Enter element to be checked list:'))
    print(SearchNum,"is repeating ",count_num(data_input,SearchNum),"times")
    
if __name__ =="__main__":
    main()