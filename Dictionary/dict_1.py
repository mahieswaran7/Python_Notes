# watch_details={
#     'Titan':8000,
#     'Fasttrack':6000,
#     'Omega':9000,
#     'Titan':12000    #Titan considered as latest key
# }

# print(len(watch_details))  #Key must be unique
# print(type(watch_details))
# print('Using Key',watch_details['Titan'])
# print('Using Key',watch_details['Titan'])


# watch_details={
#     'Titan':8000,
#     'Fasttrack':6000,
#     'Omega':9000,
#     'Sonata':8000
# }

# print(len(watch_details)) #Values can be repeated
# print(type(watch_details))
# print('Using Key',watch_details['Titan'])
# print('Using Key',watch_details['Sonata'])

# watch_details['Omega']=4000
# print('After modifying:',watch_details)
# watch_details['Fire-bolt']=7500
# print('Adding New Watch:',watch_details)

#Create a dictionary and price

spicy_food={
    'Biriyani':200,
    'Prawn Fry':250,
    'EggMasala':100,
    'Chicken65':150
}

print(len(spicy_food)) 
print(type(spicy_food))
spicy_food['Biriyani']=500
print('After Modifying',spicy_food)
spicy_food['Grill Chicken']=300
print('Adding New Food:',spicy_food)