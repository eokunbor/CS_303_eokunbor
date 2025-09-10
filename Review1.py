"""

name= "Elizabeth Okunbor" 
print(name)


def add_two_num(a, b):
    return a + b

print(add_two_num(3,5))

def for_loop_example(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

print(for_loop_example(5))

out_of_scope = 10

def local_scope(n):
    counter = 0
    for i in range(n):
        counter += 1
    return counter


print(local_scope(5))
print(out_of_scope)


def even_integer(list):
    counter = 0
    for i in list:  # iterate over a copy to safely remove items
        if i % 2 == 0:
            counter += 1
        else:
            continue
    return counter

integers = [1,2,3,4,5,6,7,8,9,10] 
print(even_integer(integers))

print(integers)  # Should print only odd integers

ROCK PAPER SCISSOR CODE - CS 300
import random 

def rock_paper_scissors():

    user_choice = int(input ("Enter 0 (Rock), 1 (Paper), or 2 (Scissor): "))
    computer_choice = random.randint(0, 2)

    if user_choice == computer_choice:
        print("You both picked the same option! Play again!")

    elif user_choice == 0 and computer_choice == 2:
        print("Computer chose: 2 (Scissor)")
        print("You Win!")
    
    elif user_choice == 2 and computer_choice == 1:
        print("Computer chose: 1 (Paper)")
        print("You Win!")

    elif user_choice == 1 and computer_choice == 0:
        print("Computer chose: 0 (Rock)")
        print("You Win!")
    
    elif user_choice == 2 and computer_choice == 0:
        print("Computer chose: 0 (Rock)")
        print("You lose!")

    elif user_choice == 1 and computer_choice == 2:
        print("Computer chose: 2 (Scissor)")
        print("You lose!")
    
    elif user_choice == 0 and computer_choice == 1:
        print("Computer chose: 1 (Paper)")
        print("You lose!")

rock_paper_scissors()

import numpy as np
print("For Lists:")
nums = [14, 50, 8]
print("Before: ", nums)
nums.append(2)
nums.sort()
print("After: ", nums)

print("For Numpy Arrays:")
array = np.array([67, 69, 420])
print("Before: ", array)
array = np.append(array, 2)
array.sort()
print("After: ", array)


dense = np.array([3, 4, 5, 7, 8, 9, 2, 6])

length_dense= len(dense)
print(length_dense)
"""




"""
import numpy as np

arr = np.array([20,40,3,7,8,9,6.1,69,200,46,8,])

#(1): LINEAR SEARCH
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print("Target:", x, "Index:", i)     
    return -1 # return index of x, -1 if not found

arr = np.array([20,40,3,7,8,9,6.1,69,200,46,8,])
linear_search(arr, 3) 

#(2): BINARY SEARCH
def binary_search(arr, low, high, x):

    return -1 # return index of x, -1 if not found

"""
'''
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


linear_search(arr, x) 


import numpy as np

def binary_search(arr, low, high, x):

    low = 0
    high = len(arr)-1 
    
    while low <= high:
        
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print("Index:", binary_search(arr, x))

arr = np.array([20,40,3,7,8,9,6.1,69,200,46,8,])
x = 430

    
def binary_search(arr, low, high, x):
    if low > high:                
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, low, mid - 1, x)
    else:
        return binary_search(arr, mid + 1, high, x)
    
    
'''
def linear_search_1000(arr, keys):
    k = len(keys)
    index = [-1] * k
    for i in range(k):
        index[i] = linear_search(arr, keys[i])
    return index

def binary_search_1000(arr, keys):
    arr.sort()
    k = len(keys)
    new = len(arr)
    index = [-1] * k
    for i in range(k):
        index[i] = binary_search(arr, 0, new - 1, keys[i])
    return index
