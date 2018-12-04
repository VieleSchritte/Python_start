#The function takes dictionary 'd' and values 'key' and 'value'
# If the key named 'key' :) is in the 'd', then we add 'value' in the list that stores in the dictionary on this key
# If there is no such key, than we add 'value' into the list on the key '2*key'
# If there is no key '2*key', we create such key and give it a list with the value

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif 2*key in d:
        d[2*key].append(value)
    else:
        d[2*key] = []
        d[2*key].append(value)

dictionary = {}
update_dictionary(dictionary, 1, -1)
print(dictionary)
update_dictionary(dictionary, 2, -2)
print(dictionary)
update_dictionary(dictionary, 1, -3)
print(dictionary)