"""
The zip function combines elements of two or more
iterables into one object.
"""

name = ['Tola', 'Makara', 'Minea', 'Mesa', 'Kompeak']
year = ['2002', '2006', '2003', '2004', '2007']

# Using zip function
obj = zip(name, year)

for info in obj:
    # convert object to dictionary
    # info = dict(obj)
    print(info, end=' ')
# ('Tola', '2002') ('Makara', '2006') ('Minea', '2003') ('Mesa', '2004') ('Kompeak', '2007')
