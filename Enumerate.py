'''
Enumerate function helps you to keep
track of your iterable elements index.
'''

laptop = ['Asus', 'lenovo', 'MSI', 'Razer', 'Mac Book', 'Acer']

# # Using tradition way
# for i in range(len(laptop)):
#     print(i, laptop[i])

# Using enumerate function
for idx, name in enumerate(laptop):
    print(f'{idx}.', name)