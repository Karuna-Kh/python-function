"""
The map function is used when you want to execute
a functions for each item in a iterable.
"""
car = ['Mazda', 'Audi', 'Tesla', 'Lamborghini', 'Ferari']

# Using map function
res = map(lambda a: a.title(), car)

for r in res:
    print(r, end=' ')
# Mazda Audi Tesla Lamborghini Ferari