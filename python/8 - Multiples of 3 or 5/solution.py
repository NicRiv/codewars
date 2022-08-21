# Multiples of 3 or 5

print('\nMultiples of 3 or 5')

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number 
passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

[Level: 6 kyu]

Note:
    If the number is a multiple of both 3 and 5, only count it once.

(Courtesy of projecteuler.net (Problem 1))
"""

# Code
def sum_of_multiples(num):    
    if (num > 0):
        sum = 0
        for m in range(1, num):
            if (m % 3 == 0) or (m % 5 == 0):
                sum += m
        return sum
    return 0

# Tests
test = 10
solution = sum_of_multiples(test)
print(solution)

spected = 23
print(f"Passed: {str((solution == spected)).upper()}")