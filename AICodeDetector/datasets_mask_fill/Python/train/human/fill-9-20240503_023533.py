fruit1 = input('Enter the name of the first fruit: \n')
fruit2 = input('Enter the name of the second fruit:\n')

if fruit1 < fruit2:
    print(fruit1 + " comes prior to " + fruit2 + " in the dictionary.")
elif fruit1 > fruit2:
    print(fruit1 + " comes after " + fruit2 + " in the dictionary.")
else:   print(fruit1 + " and " + fruit2 + " are the same.")