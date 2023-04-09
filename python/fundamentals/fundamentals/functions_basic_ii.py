# Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number 
# (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
# def countdown(num):
#     newList = list(reversed(range(num)))
#     print(newList)
# countdown(6)
def countdown(num):
    values = reversed(range(num)) #start stop setp
    for i in values:
        new_list = list(values)
        return new_list

print(countdown(6))


# Print and Return - Create a function that will receive a 
# list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([11,66]))

# First Plus Length - Create a function that accepts a list and returns 
# the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

