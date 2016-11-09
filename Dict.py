__author__ = 'Administrator'

d = {'cat':'cute','dog':'furry'}
print(d['cat'])
print('cat' in d)
d['fish'] = 'wet'
print(d['fish'])
print(d.get('mokey','N/A'))
print(d.get('fish','N/A'))
del d ['fish']
print(d.get('fish','N/A'))