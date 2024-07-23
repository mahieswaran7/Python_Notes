menu_card=['Panneer','Dal','rice']
print('Available Items in menu card:',menu_card)

#append()--> Adds an element at the end of the list


menu_card.append('Kofta')
print('After using append method:',menu_card)

#'Dal Tadka','Biriyani'

#extend()--> Add the elements of a list(or iterable)
#to the end of the list

menu_card.extend(['Dal Tadka','Biriyani'])
print('Using Extend method:',menu_card)

#insert --> Adds an element at the specified position

menu_card.insert(1,'Veg Biriyani')
print('Using Insert method:',menu_card)

#remove() method -> will remove specified value

menu_card.remove('Dal Tadka')
print('Using Remove method:',menu_card)

#pop() method --> removes  element  of specified position

menu_card.pop(2)
print('Using pop method:',menu_card)


menu_card = ['Panneer','Dal','Rice','Panneer'] #allow duplicates

#index method

index_method=menu_card.index('Rice')
print('It will give position:',index_method)

index_method = menu_card.index('Panneer')
print('It will give the position : ',index_method)

#sort method 

menu_card.sort()
print('Using Sort method :',menu_card)
