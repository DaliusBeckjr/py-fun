# write a program that can print all numbers from 1-255

def ananas():
    for i in range(1,256):
        print(i)
#ananas()

# write a program that would print all the odd numbers from 1 - 255
def oddNumbers():
    for i in range(1,256,2):
        print(i)
# oddNumbers()

# or (this was during office hour)
def iterate_odd():
    for i in range(1,256):
        if i % 2 != 0:
            print(i)
# iterate_odd()

# print the sum of all numbers from 1 - 255

def final_sum():
    sum = 0
    for i in range(1,256):
        sum += i
    print(sum)

#final_sum()

# Given an array [1,3,5,7,9,13] write a function that would iterate
# through each member of the array and print each value 

arr = [1,3,5,7,9,13]

def iterate_array(array):
    for i in array:
        #print(array[i])
        print(i)

iterate_array(arr)

# write a function that takes any array and prints the Maximum value in the array




# write a function that takes an array and prints the AVERAGE of the values
# in the array for example for an array [2, 10, 3] your program should
# print an average of 5 
# array = [2, 10, 3]



# write a function that creates an array that contains all of the even numbers
# between 1 - 255


# write a function that takes an array and a number 'y' and returns the values in
# the array that are greater than a given 'y' 