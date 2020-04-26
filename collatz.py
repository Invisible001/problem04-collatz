# Author: Nguyen L.
# Date:   April 26th, 2020
# Collatz sequence problem
# Algorithm: if n is even, then n = n/2
#            if n is odd, then n = 3*n + 1
#            repeat until the final result is 1

#function to calculate the collatz sequence
def collatz(n):

    # empty list
    my_list = []

    # appending first value to list
    my_list.append(n)
    
    # loop
    while(n != 1):
        if n % 2 == 0:
            n = n//2
            my_list.append(n)
        else:
            n = 3*n + 1
            my_list.append(n)

    return my_list

print("Input number: ", end='')
num = int(input())
my_list = collatz(num)
print(my_list)    
