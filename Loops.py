from demo.List import x

__author__ = 'Administrator'
animals = ['cat','dog','monkey']
for animal in animals:
    print(animal)


animals = ['cat','dog','monkey']
for idx,animal in enumerate(animals):
    print('#%d: %s' %(idx + 1, animals))

print()

# for
d = {'person':2,'cat':4,'spider':8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' %(animal,legs))

# iteritems
d = {'person':2,'cat':4,'spider':8}
for animal,legs in d.iteritems():
    print('A %s has %d legs' % (animal,legs))


nums = [0,1,2,3,4]
even_num_to_square = {x: x**2 for x in nums if x % 2 ==0}
print(even_num_to_square)
