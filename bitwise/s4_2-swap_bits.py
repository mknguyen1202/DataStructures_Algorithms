import time

# swap the bit of x in the i-th and j-th position
# Complexity: O(n) where n is the integer width
def swapbit_bruteforce(x: int, i: int, j: int) -> int:

    # extract bit
    ibit = 1 & x >> i
    jbit = 1 & x >> j
    
    if ibit == 0b0:
        x &= ~(1 << j)
    else:
        x |= (1 << j)
        
    if jbit == 0b0:
        x &= ~(1 << i)
    else:
        x |= (1 << i)
    return x

# i-th and j-th bits differ. We will swap them by flipping their values.
# select the bits to flip with bit_mask. Since x^1 = 0 when x = 1 and 
# x^1 = 1 when x = 0, we can perform the flip XOR
# Complexity: O(n)
def swapbit(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask

    return x

num = 112300

start = time.time()
print("output\t", bin(swapbit_bruteforce(num, 15, 1)))
print("Time:", time.time() - start)


print("input\t", bin(num))

start = time.time()
print("output\t", bin(swapbit(num, 15, 1)))
print("Time:", time.time() - start)