students = [
    {
        'f_name' : 'Ronald',
        'l_name' : 'don',
        'age' : 45,
        'dob' : 'january 22'
    },
    {
        'f_name' : 'todd',
        'l_name' : 'germo',
        'age' : 27,
        'dob' : 'november 16'
    },
    {
        'f_name' : 'tony',
        'l_name' : 'dents',
        'age' : 32,
        'dob' : 'october 8'
    },
    {
        'f_name' : 'andrea',
        'l_name' : 'waters',
        'age' : 32,
        'dob' : 'october 8'
}

]
# output prints all the key: value of each dictionary
# for one_student in students:
#     print(one_student)

#for one_student in students:
    #print(one_student['f_name'])
#outputs ronald, todd, tony, andrea

# make a program that list out first name, last name, dob, age of every one 
# of them 
# for one_student in students:
#     for key, value in one_student.items():
#         print(key, value)

# make a function that pulls all of the values from a single student
# print(students[1]) # we took all info from tod 

# # if you wanted only todd's info 
# for key, value in students[1].items():
#     print(key, value)

# how do we get them on the same line hint: did this in OH
for one_student in students:
    output = ''
    for key, value in one_student.items():
        output += f'{key} - {value}, '
    print(output)