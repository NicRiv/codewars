"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

        16  -->  1 + 6 = 7
       942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
    132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
"""

# Code
def digital_root(n):
    if len(str(n)) != 1:
        str_num = str(n)
        new_num = 0
        for num in str_num:
            new_num += int(num)
        return digital_root(new_num)
    else:
        return n

# Tests
test = 16
solution = digital_root(test)
print(solution)