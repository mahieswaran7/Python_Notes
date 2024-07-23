
country=['india','south Korea','iran','japan','turkey','iraq']

#print(country[0])
#print(country[1])
#print(country[2])
#print(country[3])

for name in country:
    print(f'{name.title()}, these are the list of countries')


    author_name=('j k rowling','rachel aaron','virat kohli','rohit sharma')

# index = 1
# for trash in range(len(author_name)):
#     print(f'{index} : {author_name[trash]}')
#     index+=1


# for name in author_name:
#   print(name)
#   print(f'{name.title()}')

for auth_name in range(len(author_name)): #for author_name in range(4):
    print(auth_name)
    print()

for auth_name in range(len(author_name)): #for auth_name in range(4):
    print(author_name[auth_name],'----',auth_name) #author_name[0] #author_name[1]....[3]


    #iterate over a string using for loop

    time_update="it's 4.15 pm"

    for time in range(len(time_update)):
        print(time_update)
