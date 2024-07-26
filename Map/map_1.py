from functools import reduce
def main():
    size=int(input('Enter the size :'))
    lst=[]
    print('enter values')
    for i in range(size):
        value=int(input())
        lst.append(value)
    print('User List:',lst)

    # map_list=list(map(lambda num:num**3,lst))
    # print('Map list:',map_list)
    # print()
    # #27-num1,num2=64
    # #91-num1,num2=125
    # #216-num1,num2=216
    # reduce_list=reduce((lambda num1 ,num2:num1+num2),map_list)
    # print('Reduce value:',reduce_list)

#Task2

# product_ids = ['HEM-234', 'HEM-123', 'HEM-566']
# number_ids = list(map(lambda x: int(x.split('-')[1]), product_ids))
# print(number_ids)

#Task3
students = [
    {'name': 'Shreya', 'age': 15},
    {'name': 'Pratiksha', 'age': 13},
    {'name': 'Prerna', 'age': 15}
]


sort_list = sorted(students, key=lambda con: con['age'])
print(sort_list)


if __name__=="__main__":
    main()  

    # course=['','Python','Java',';$','angu;ar','PHP']
    # filter_course=['Python','Java','PHP']

   

 #Task3
 
# def main():
   
# students = [
#     {'name': 'Shreya', 'age': 15},
#     {'name': 'Pratiksha', 'age': 13},
#     {'name': 'Prerna', 'age': 15}
# ]


# sort_list = sorted(students, key=lambda con: con['age'])
# print(sort_list)


# if __name__=="__main__":
#     main()  

    