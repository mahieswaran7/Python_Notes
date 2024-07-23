#Creating a List
#creating same data type:

course=['Python','Java','PHP'] #string
rollno=[123,124,432] #integer

#creating mixed type/hetrogenous

mixed_type=['Rohit',123,True,67.80]
print('Hetrogenus:',mixed_type)
print('Length:',len(mixed_type))

#Positive Index
print('Access value of Rohit:',mixed_type[0])
print('Access value of 123:',mixed_type[1])
print('Access value of True:',mixed_type[2])
print('Access value of 67.80:',mixed_type[3])

#Negative index -> 123
print("accessing the values; ", mixed_type[-1])
print("accessing the values; ", mixed_type[-2])
print("accessing the values; ", mixed_type[-3])

#Slicing:[start:stop(excluded)]
mixed_type=['Boga',44,55,'senidgood']
print('Slicing Positive',mixed_type[1:3])
print('Slicing Negative:',mixed_type[-4:-1])

#Mutable(can change,add and delete)

fruits=['Mango','Banana','Grapes','WaterMelon']
fruits[1]='Kiwi'
print('Using index banana replaced by kiwi',fruits)

del fruits[3]
print('removing watermelon:',fruits)

#slicing replaced Kiwi,Grapes -> ['Mango','Banana',Orange']

fruits[1:3]=["apple","pineapp"]
print('replace using slice',fruits)
