import time

'''
the parity of a word is 1 if the number of 1s in the word is odd; otherwise, it is 0. 
For example, the parity of 1011 is 1, an th parity of 10001000 is 0. 
Parity checks are used to detect single bit errors in data storage and communication
It is fairly straightforward to write code that computes the parity of a 
single 64-bit word.
'''

def printbin(string, *args) -> bin:
    print(string, end=" ")
    for i in args:
        print(bin(i), end=" ")
    print()

# brute force: check each bit then shift one bit
def parity_bruteforce(x: int) -> int:
    result = 0
    while x:
        # printbin("FIRST:", x, result)
        result ^= x & 1 # check each bit
        # printbin("AFTER result:", x, result)
        x >>= 1
        # printbin("AFTER   x >>:", x, result)
    return result

'''
### better time complexity: O(k) where k is the number of bits set to 1 in a particular word
x&(x-1) = x with its lowest set bit erased. -> better time complexity (erase bit faster shifting bit)
For example, x = 00101100 => x - 1 = 00101011
x&(x-1) = 00101100 & (00101100 - 1) = 00101000
'''
print("\n\n\n")
def parity(x: int) -> int:
    result = 0
    while x:
        # printbin("FIRST:", x, result)
        result ^= 1 # flip flop to count
        # printbin("AFTER result:", x, x - 1, result)
        x &= x - 1 # clear the first 1 from the right
        # printbin("AFTER   x >>:", x, result)
        # print()
    return result
    
#################
# precompute the values for cache
PRECOMPUTED_PARITY = {}
CACHE_SIZE = 2 ** 16
for i in range(CACHE_SIZE):
    PRECOMPUTED_PARITY[i] = parity(i)


print(PRECOMPUTED_PARITY)
PRECOMPUTED_PARITY.setdefault(0)
# runtime complexity: O(log n) Where n is the word size
# the parity of (11010111) is the same as the parity of 1101 XORed with 0111
# EXAMPLE:
# 11010100
# 11 -> shift by 3
# 01 -> shift by 2
# 01 -> shift by 1
# 00 -> no shift
# mask size = 16 because 64 = 16 x 4, and 64bit cache is too expensive
# mask_size could be 8, but then the table will only have 2^8 values -> more computation needed
# if number > 2^64, might need other mask size, for example, if input number supported
# with 2^128  or 128 bits -> 128 = 32 x 4 -> mask size = 32 
def parity_cache(x: int) -> int:
    # support 64-bit input only
    mask_size = 16
    bit_mask = 0xFFFF  
    # shifting bit fundamentally similar to the example above
    return (PRECOMPUTED_PARITY[x >> (3 * mask_size)] ^
            PRECOMPUTED_PARITY[(x >> (2 * mask_size)) & bit_mask] ^
            PRECOMPUTED_PARITY[(x >> mask_size) & bit_mask] ^
            PRECOMPUTED_PARITY[x & bit_mask])
    

x = 112300
start = time.time()
pb = parity_bruteforce(x)
print(time.time() - start)


start = time.time()
p = parity(x)
print(time.time() - start)
print(pb == p)


start = time.time()
p = parity_cache(x)
print(time.time() - start)
print(pb == p)