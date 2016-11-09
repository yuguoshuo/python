__author__ = 'Administrator'
# for
nums = [0,1,2,3,4]
squares = []
for x in nums:
    squares.append(x**2)
    print(squares)

print()

# list comprehension
nums = [0,1,2,3,4]
squares = [x**2 for x in nums]
print(squares)

print()

nums = [0,1,2,3,4]
even_squares = [x**2 for x in nums if x % 2 == 0]
print(even_squares)