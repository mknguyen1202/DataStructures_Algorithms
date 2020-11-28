'''
define Weight: of a nonnegative integer x to be the number of bits that are
set to 1 in its binary representation. For example, 92 --bin--> 1011100
weight is 4.
----
input x and output y so that |y-x| is as small as possible and have same weight.
Program:
input: 6 --bin--> 110
output: 5 --bin--> 101 (closest and also has two 1's in bins)
'''

def closest_int_same_bit_count_bf(x: int) -> int:
    left = x + 1
    right = x - 1

    inputweight = 0
    while x:
        x = x & (x-1)
        inputweight += 1

    while True:
        weight = 0
        while left:
            left = left & (left - 1)
            weight += 1

        if weight ==  inputweight:
            return weight
        
        if right > 0:
            weight = 0
            while right:
                right = right & (right - 1)
                weight += 1

            if weight == inputweight:
                return weight

        left += 1
        right -= 1


def closest_int_same_bit_count(x: int) -> int:
    # TODO
    

