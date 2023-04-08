#just a def practice using f string 
def say_hello(f_name, l_name): # store the values in def function
    return(f"hello my name is {f_name} {l_name}") #returning the statemnt
greeting = say_hello("Dalius", "Beck") #calling the def function

print(greeting)

#note: print() is to debug
# 'return()' will exit a code immediately even if there is more to be done

# def multiply(num_list, num): #don't go inside the function until the function is called
#     print(num_list, num) # output [2,4,10,16] 5
#     for x in num_list:
#         print(x) # output '2' '4' '10' '16'
#         x *= num
#         #print(x) # [2] * 5 = 10 then [4] * 5 = 20... 
#         print(num_list) # repeating a with the same amount in the arr
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5) # now our function executes; what is a function call equal to?
# print(b) # and the resulting value is printed


# we can either enumerate or use range 
# def multiply(num_list, num):
#     for x, item in enumerate(num_list):
#         num_list[x] *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)

def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b) # output [10,20,50,80]






