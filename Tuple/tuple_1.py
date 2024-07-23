#Create a tuple

#Hemogenus

student_id=(123,124,125,126)
ice_cream=('Vannila','choco-chips','Blueberry')


#Hetrogenios

mixed_type=(123,'Hello',False,56.78)
#len()
#using index ==> Blueberry(Positive)
#using index ==> False(Negative index)
#using slicing ==> 'Hello',False

ice_cream=('Vannila')#str
print(ice_cream,type(ice_cream))
ice_cream=('Vannila')
print(ice_cream,type(ice_cream))

print("length of student id ",len(student_id))
print("length of student id ",ice_cream[2])
print("length of student id ",mixed_type[-2])
print("length of student id ",mixed_type[1:3])


#immutable (cannot modify,delete or add)
#mixed_type[0]=True
#print(mixed_type)

ice_cream=('Vannila','Choco-chips','Blueberry','Vannila')
countmethod=ice_cream.count('Vannila')
print('Count method:',countmethod)
print()
indexmethod=ice_cream.index('Vannila')
print('Index method:',indexmethod)