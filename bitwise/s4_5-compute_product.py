'''
Compute product without arithmetical operators.
The only operators allowed are:
    1) assignment
    2) bitwise: >>, <<, |, &, ~, ^
    3) equality checks and Boolean combinations thereof
'''


def multiply_bf(x: int, y: int) -> int:
    # TODO

def multiply(x: int, y: int) -> int:
    def add(a, b):
        return a if b == 0 else add (a ^ b, (a & b) << 1)
    
    # TODO


