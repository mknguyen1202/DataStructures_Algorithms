import copy
import bisect
import random

# ---------------------------------
# list() comprehension
a = list(range(10))
print(a)

a.insert(3, 28)
print(a)

print()
print()


b = a
print("b = a", b)
print("type:", type(b))
print(b is a)

print()
print()

b = list(a)
print("b = list(a)", b)
print("type:", type(b))
print(b is a)

# --------------------------------
# deep copy vs shallow copy

# shallow copy: 
# Different objects but copied referenced to the original one
# if you modify the   <<mutable>>   elements like lists, 
# the changes will be reflected on the original elements.
b = a[:]
# b = a.copy() # or this

print(a)
a.append(15)
print("a:", a)
print("b:", b)

print("insert b:")
b.append(15)
print("a:", a)
print("b:", b)

print("\n--------------------")
a = [[1, 2], [2, 4]]
print("reassigned a, then b is", b)
b = a.copy()
b.append([3, 6])
print("a:", a)
print("b:", b)

print("\n--------------------")
a = [[1, 2], [2, 4]]
b = a[:] #shallow copy

b[0].append(3)
print("shallow copy:")
print("a:", a)
print("b:", b)

# List b has its own pointer, but its elements do not


# --------------------------------
# deep copy:
a = [[1, 2], [2, 4]]
b = copy.deepcopy(a) ## deep copy

b[0].append(3)  ## Edit the first element (i.e. [1, 2])

print("\n--------------------")
print("deep copy:")
print("a:", a)
print("b:", b)


# Pointers
#  you can use id() method to get the address of an object in memory.
print("\n--------------------")
print("Pointers:")
test = ['a', 'b', 'c']
print(id(test))

# --------------------------------
# key methods: binary search, min, max, reverse, sort, del
a = [random.randint(0, 15) for _ in range(10)]

print("\n--------------------")
print("list:", a)
print("binary search:")
print(bisect.bisect(a, 6))
a.sort()
print(a)

print("\n--------------------")
print("binary search left:")
print(bisect.bisect_left(a, 6))

print("\n--------------------")
print("binary search right:")
print(bisect.bisect_right(a, 6))

del a[1]
print(a)


print(a[2:] + a[:2])    # rotate a LEFT by 2
print(a[-2:] + a[:-2])    # rotate a RIGHT by 2





