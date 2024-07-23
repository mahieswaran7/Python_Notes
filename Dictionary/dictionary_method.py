
watch_details={
    'Titan':8000,
    'Fasttrack':6000,
    'Omega':9000,
    'Sonata':8000
}


#get method => retruns the value of specified key

get_method=watch_details.get('Titan')
print('get method:',get_method)

#items() methods : returns a list containing a tuple for each key value pair

item_method=watch_details.items()
print('item method:',item_method)

#key method  : returns the all keys in the dictionary
key_method=watch_details.keys()
print('keys method:',key_method)

#value method :returns  all the values in the dictionary
value_method=watch_details.values()
print('value method:',value_method)

#update method insert an  item to the dictionary

watch_details.update({'Noise':3000})
print('Update method:',watch_details)

#pop method: remove element with specified key

watch_details.pop('Titan')
print('Pop method:',watch_details)