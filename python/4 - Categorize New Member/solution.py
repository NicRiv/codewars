# Categorize New Member

"""
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. 
They would like your help with an application form that will tell prospective members 
which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

[Level: 7 kyu]

input:
    [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]

output:
    ["Open", "Open", "Senior", "Open", "Open", "Senior"]

NOTES:
    Input will consist of a list of pairs. Each pair contains information for a single 
    potential member. Information consists of an integer for the person's age and an 
    integer for the person's handicap.

    Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether 
    the respective member is to be placed in the senior or open category.

"""

# Code
def categories_of_members(member_information): # def open_or_senior(data):
    categories = []

    for member in member_information:
        if member[0] >= 55 and member[1] > 7:
            categories.append('Senior')
        else:
            categories.append('Open')

    return categories

# Tests
test = [
    [18, 20], 
    [45, 2], 
    [61, 12], 
    [37, 6], 
    [21, 21], 
    [78, 9]
]

solution = categories_of_members(test)
print(solution)

spec = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
print(solution == spec)
