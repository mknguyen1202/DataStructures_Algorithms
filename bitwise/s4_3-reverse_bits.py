import time
'''
Write a program that takes a 64-bit unsigned integer and returns the
64-bit unsigned integer consisting of the bits of the input in
reverse order. For example,
input: 1110000000000001
output:1000000000000111
'''

# Complexity: O(n) where n is the bit length
def reverse_bits_bruteforce(x: int) -> int:
    mask = 0b1
    result = 0
    while x:
        result <<= 1
        result = result + (mask & x)
        x >>= 1

    return result



PRECOMPUTED_REVERSAL = {}
CACHE_SIZE = 2 ** 16
for i in range(CACHE_SIZE):
    PRECOMPUTED_REVERSAL[i] = reverse_bits_bruteforce(i)


# for example, the input consists of four 16-bit integers y3, y2, y1, y0
# with y3 holding the most significant bits. Then the least 16 significant bits
# in the reverse come from y3.
# Complexity: O(n/L) where L is the number of cache keys
def reverse_bits(x: int) -> int:
    mask_size = 16
    bit_mask = 0xFFFF
    # first 16 bits
    y3 = PRECOMPUTED_REVERSAL[x & bit_mask] << (3 * mask_size)

    # next 16 bits
    y2 = PRECOMPUTED_REVERSAL[(x >> mask_size) & bit_mask] << (2 * mask_size)

    # and so on
    y1 = PRECOMPUTED_REVERSAL[(x >> (2 * mask_size)) & bit_mask] << (1 * mask_size)
    y0 = PRECOMPUTED_REVERSAL[(x >> (3 * mask_size)) & bit_mask]
    
    # combine everything
    return (y3 | y2 | y1 | y0)



x = 0b1110001111111
start = time.time()
print(bin(reverse_bits_bruteforce(x)))
print("Runtime for bruteforce:", time.time() - start)

print('--------------------------')
x = 0b1110001111111
start = time.time()
print(bin(reverse_bits(x)))
print("Runtime for cache:", time.time() - start)
