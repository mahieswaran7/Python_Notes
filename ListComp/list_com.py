
#using list comprehension creating a list of square numbers

#new_list=[expression for member in itrable]

#new_list=[expression for member in iterable if(optional)]

new_list= [i for i in range(1,11)]
print('List Comprehension:',new_list)

new_list=[i for i in range(1,11)if(i%2==0)]
print('List Comprehension:',new_list)

#vowel from name

vowels="aeiou"
name="eswaran"
new_list= [i for i in name if  i in vowels]
print(new_list)
