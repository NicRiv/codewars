"""
In this little assignment you are given a string of space 
separated numbers, and have to return the highest and lowest number.

[Level: 7 kyu]

input:
"1 2 3 4 5"
"1 2 -3 4 5"
"1 9 3 4 -5"

output:
"5 1"
"5 -3"
"9 -5"

Notes:
    - All numbers are valid Int32, no need to validate them.
    - There will always be at least one number in the input string.
    - Output string must be two numbers separated by a single space, and highest number is first.
"""

# Code
def high_and_low(numbers):
    new_list = []
    
    for i in numbers.split():
        new_list.append(int(i))

    hg = max(new_list)
    lw = min(new_list)

    return str(hg) + ' ' + str(lw)

# Tests
test = "1 2 3 4 5"

solution = high_and_low(test)
print(solution)
