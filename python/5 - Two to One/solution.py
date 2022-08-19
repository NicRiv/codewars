# Two to One

print('\nTwo to One')

"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, 
the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

[Level: 7 kyu]

input: 
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
output:
    "abcdefklmopqwxy"
"""

# Code
def longest(s1, s2):
  set_s1 = set(s1)
  set_s2 = set(s2)
  
  set_longest = set_s1 | set_s2

  sorted_set_longest = sorted(set_longest)
  two_to_one = "".join(sorted_set_longest)
  
  return two_to_one

# Tests
test_a = 'xyaabbbccccdefww'
test_b = 'xxxxyyyyabklmopq'

solution = longest(test_a, test_b)
print(solution)

spected = 'abcdefklmopqwxy'
print(solution == spected)