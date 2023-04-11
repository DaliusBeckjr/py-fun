some_list = [1,3,4,6,9]
some_list[2] = "ananas"
#print(some_list)

# for i in range(0, len(some_list), 1):
#     print(some_list[i])1

# for item in some_list:
#     print(item)

Dallas = {
    'f_name' : 'Dallas', # {key : value}
    'l_name' :'Beck',
    'age' : 23,
}

# is this key of 'dob' is in Dallas, if it is
# if 'dob' in Dallas:
#     print(Dallas['dob'])
# else:
#       Dallas['dob'] = 'august 15' 

# can we simplify this any further?
# we can use a key word 'not' - as long as it's not in dallas
# I want you to create it
# other example ' if this is false do this' 
if 'dob' not in Dallas:
    Dallas['dob'] = 'august 15' 

#Dallas['f_name'] = 'clark' # change the name value for this key
# print(Dallas['age']) #output 23 
print(Dallas)

# for key in Dallas:
#     print(key) # output 'f-name' 'l_name' 'age' 'dob'

# for key in Dallas:
#     if Dallas[key] == 'clark': # pulled only this specific key 
#         print[key] # output 'f_name'

# prefer way to loop through a dictionary, very clean
# for key, value in Dallas.items():
#     print(key, value) 
# output 'f_name Dallas' 'l_name Beck' 'age 23' 'dob august 15'

# what if i didn't have '.items()'
for key in Dallas:
    print(key, Dallas[key])


