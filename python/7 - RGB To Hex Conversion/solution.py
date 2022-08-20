# RGB To Hex Conversion

print('\nRGB To Hex Conversion')

"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values 
will result in a hexadecimal representation being returned. Valid decimal values 
for RGB are 0 - 255. Any values that fall out of that range must be rounded 
to the closest valid value.

[Level: 5 kyu]

Example:
    rgb(255, 255, 255) # returns FFFFFF
    rgb(255, 255, 300) # returns FFFFFF
    rgb(0,0,0) # returns 000000
    rgb(148, 0, 211) # returns 9400D3

Note: 
    Your answer should always be 6 characters long, the shorthand with 3 will not work here.
"""

# Code
def rgb(r, g, b):
    sist_hex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    # def conversion to hex
    def conversion(num):
        new_num = []
        def conver_uni(num):
            for n in range(16):
                if num == n:
                    return new_num.insert(0, sist_hex[n])
            
            for n in range(16):
                if num % 16 == n:
                    new_num.insert(0, sist_hex[n])
            
            return conver_uni(num // 16)
        
        if num > 255: return "FF"
        if num < 0: return "00"
        
        conver_uni(num)
        if len(new_num) == 1: new_num.insert(0, '0')

        return "".join(new_num)

    # add str
    str_hex = [conversion(r), conversion(g), conversion(b)]

    return "".join(str_hex)

# Tests
test_a = 257  # rgb
test_b = 23  # rgb
test_c = 0  # rgb

solution = rgb(test_a, test_b, test_c)
print(solution)