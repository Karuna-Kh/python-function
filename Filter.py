"""
The filter function is used to filter any kind of data based on
a given condition from a iterable.
"""

fruit = ['Apple', 'Grapes', 'Orange', 'Cherry', 'Kiwi', 'Mango']

# Using filter function
res = filter(lambda x: len(x) < 5, fruit)

for data in res:
    print(data)
# Kiwi
