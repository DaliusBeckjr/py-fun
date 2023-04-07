for i in range(151): # basic
    print(i)

for i in range(5,1005,5): #multiples of 5
    print(i)

for num in range(1,101,1):
    string = ""
    if num % 5 == 0:
        string = string + "coding"
    if num % 10 == 0:
        string = string + " dojo"
    if num % 5 != 0 and num % 10 != 0:
        string = string + str(num)
    print(string)

# woah that suckers huge
# add odd integers from 0 to 500,000 and print the final sum
sum=0
for i in range(1,500000,2):
    sum+=i
print(sum)


#count down by 4's print positive numbers starting at 2018, counting 
# down by 4

for num in range(2018,0,-4):
    print (num)

# flexible counter 
lowNum = 2
highNum= 9
mult= 3
