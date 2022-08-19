# Mumbling

print('\nMumbling')

"""
This time no story, no theory. The examples below show you how to write function accum:

[Level: 7 kyu]

input:
    'abcd'
    'RqaEzty'
    'cwAt'

output:
    'A-Bb-Ccc-Dddd'
    'R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy'
    'C-Ww-Aaa-Tttt'

Note:
    The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

# Code
def accum(word):  
  word = word.lower()
  word = " ".join(word).split()

  for letter in word:
    pos = word.index(letter) 
    word[pos] = (letter * (pos + 1)).title()

  word = "-".join(word)
  
  return word

# Tests
test = 'RqaEzty'
solution = accum(test)
print(solution)

spected = 'R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy'
print(solution == spected)