"""
Implement the function unique_in_order which takes as argument a sequence and returns 
a list of items without any elements with the same value next to each other and preserving 
the original order of elements.

Example:
    'AAAABBBCCDAABBB' = ['A', 'B', 'C', 'D', 'A', 'B']
            'ABBCcAD' = ['A', 'B', 'C', 'c', 'A', 'D']
          [1,2,2,3,3] = [1,2,3]
"""

# Code
def unique_in_order(iterable):
  new_list = []

  for l in iterable:
    state = True
    last_item = 0
    
    if len(new_list) > 0:
      last_item = new_list[len(new_list) - 1]
    
    if l == last_item:
      state = False
    
    if state:    
      new_list.append(l)
  
  return new_list

# Tests
test = 'AAAABBBCCDAABBB'
test_2 = [1,2,2,3,3]

solution = unique_in_order(test)
print(solution)
