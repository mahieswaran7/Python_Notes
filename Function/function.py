
#function

#def Addition():
# print('Inside Addition') 
#Addition()


# def Addition(value_01,value_02):    #value_01=12,value_02=13
#     print('Inside Addition')
#     print('Argument:',value_01)  #1 parameter 1 argument
#     print('Argument:',value_02)
#     Add=value_01+value_02
#     return Add
# Result =Addition(12,13)
# print('Addition of the Numbers:',Result)

def Addition(value_01,value_02):
    print('inside Additon')
    print('Argument 1:',value_01)
    print('Argument 2:',value_02)
    Add =value_01+value_02
    Sub=value_02-value_01
    return Add,Sub
    
    print(f'{value_01} and {value_02} addition is :',value_01 + value_02)
add,sub = Addition(10,20)
print('Adddtion of nos is ',add)
print('Subraction of nos is ',sub)
print()


