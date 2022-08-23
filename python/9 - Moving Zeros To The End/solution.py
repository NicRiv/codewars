# Moving Zeros To The End

print('\nMoving Zeros To The End')

"""
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

[Level: 5 kyu]

Example:
    move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

# Code
def move_zeros(arr):
    sz = len(arr)
    arr = [n_zero for n_zero in arr if n_zero != 0]
    arr += [0] * (sz - len(arr))
    return arr

# Tests
test = [1, 0, 1, 2, 0, 1, 3]
solution = move_zeros(test)
print(solution)

spected = [1, 1, 2, 1, 3, 0, 0]
print(solution == spected)
