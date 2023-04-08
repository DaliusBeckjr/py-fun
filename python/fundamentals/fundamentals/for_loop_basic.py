# basic
for i in range(151): 
    print(i)

# multiples of 5
for i in range(5,1005,5): 
    print(i)

# counting the dojo way
# print int 1-100
# divisible by 5 - print coding
# divisible by 10 print coding dojo
for i in range(1, 101):
    if i % 10 == 0:
        print("coding dojo")
    elif i % 5 == 0:
        print("coding")
    else:
        print(i)

# woah that suckers huge
# add odd integers from 0 to 500,000 and print the final sum
sum=0
for i in range(1,500001,2):
    sum+=i
print(sum)


#count down by 4's print positive numbers starting at 2018, counting 
# down by 4

for num in range(2018,0,-4):
    print (num)



lowNum= 2
highNum= 9
mult= 3

for i in range(lowNum,highNum +1):
    if i % mult == 0:
        print(i)

