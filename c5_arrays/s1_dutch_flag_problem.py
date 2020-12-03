import random
from typing import List
'''
page 41
THe quicksort algorithm for sorting array proceeds recursivel -  it selets an element(the "pivot")
reorders the array to make all the elements less than or equal to the pivot appear first, followed
by all the elements greater than the pivot. The two subarrays are then sorted recursively.

Implemented naively, quicksort has large run times and deep function call stacks on arrays with many
duplicates because the subarrays may differ greatly in size. One solution is to reorder the array
so that all elements less than the pivot appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot. This is known as Dutch national flag partitioning 
because the Dutch national flag consists of three horizonl bands, each in a different color.

'''

def printl(a, index):
    print("[", end="")
    for i in range(len(a)):
        if index == i:
            print("_", a[i], "_", end="", sep="")
            if i != len(a) - 1:
                print(", ", end="")
        else:
            print(a[i], end="")
            if i != len(a) - 1:
                print(", ", end="")
    print("]")

RED, WHITE, BLUE = range(3)


# Form three lists, namely, elements less than pivot, elements equal to the pivot, and 
# elements greater than the pivot
# Space complexity: O(n) where n is the length of A
# Time complexity: O(n)
def dutch_flag_partition_trivial(pivot_index: int, A: List[int]) -> None:
    smaller = []
    equal = []
    greater = []
    
    pivot = A[pivot_index]
    for i in A:
        if i < pivot:
            smaller.append(i)

        elif i == pivot:
            equal.append(i)
        
        else:
            greater.append(i)

    temp = smaller + equal + greater
    for i in range(len(temp)):
        A[i] = temp[i]
        



    



# We can avoid O(n) additional space at the cost of increased time complexity as follows
# In the first stage, we iterate through a starting from index 0, then index 1, etc.
# In each iteration, we seek an element smaller than the pivot - as soon as we fin it, we move it to
# the subarray of smaller elements via an exchange. This moves all the elements less than the pivot
# to the start of the array. The second is similar to the first one, the difference being that we move elments
# greater than the pivot to the end of the array. 
# Space complexity: O(1)
# Time complexity: O(n^2)
def dutch_flag_partition_time_complexity(pivot_index: int, A: List[int]) -> None:
    # TODO
    # do something

    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    for i in range(len(A)):
        print("Outer:", i, " || ", A)
        # Look for a smaller element
        for j in range(i + 1, len(A)):
            print(A, A[j], pivot)
            if A[j] < pivot:
                print("LESS THAN")
                A[i], A[j] = A[j], A[i]
                break
    
    print("\n----------------------\n")
    # Second pass: group elements larger than pivot
    for i in reversed(range(len(A))):
        print("Outer:", i, " || ", A)
        # Look for a larger element. Stop when we reach an element less than 
        # pivot, since first pass has moved them to the start of A.
        for j in reversed(range(i)):
            print(j, A[j], pivot)
            printl(A, j)
            if A[j] > pivot:
                print("GREATER THAN")
                A[i], A[j] = A[j], A[i]
                break





# To improve time comlexity, we make a single pass and move all the elements less
# than the pivot to the beinning. In the second pass we move the larger elements to the
# end. It is easy to perform each pass in a single iteration, moving out-of-place
# elements as soon as they are discovered.
# Time complexity: O(n)
# Space complexity: O(1)
def dutch_flag_partition_time_improved(pivot_index: int, A: List[int]) -> None:
    #TODO
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    # Second pass: group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

        

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    # keep the following invariants during partitioning:
    # bottom group: A[:smaller]
    # middle group: A[smaller:equal]
    # unclassified group: A[equal:larger]
    # top group: A[larger:]

    smaller, equal, larger = 0, 0, len(A)
    # keep iterating as long as there is an unclassified element
    while equal < larger:
        # A[equal] is the incoming unclassified element
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        
        elif A[equal] == pivot:
            equal += 1

        else: # A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]



A = [random.choice([RED, WHITE, BLUE]) for _ in range(10)]

# print(A)
# dutch_flag_partition_trivial(3, A)
# print(A)


print(A)
dutch_flag_partition(3, A)
print(A)

