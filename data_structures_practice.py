"""
Data Structures Practice
Covers: Lists, Tuples, Dictionaries, Sets
Author: Lovepreet Singh
"""
#---------Lists---------
#Create a list of 5 numbers and print the sum.
print('Lists P1')
numbers = [2,6,2,7,5]
print(sum(numbers))

#Replace the 3rd element with "watermelon".
print('\nLists P2')
fruits = ["apple", "banana", "mango"]
fruits[2] = 'watermelon'
print(fruits[2])

#Loop through a list and print all elements in uppercase.
print('\nLists P3')
for elements in fruits:
    print(elements.upper())

#Reverse a list without using reverse().
print('\nLists P4')
x = len(fruits) - 1

while x >= 0:
    print(fruits[x])
    x -= 1

#---------Tuples---------
#Store 3D coordinates in a tuple and print the z-value.
print('\nTuples P1')
coordinates = (10, 20, 30)
print(coordinates[2])

x, y, z = coordinates
coordinates = y,z,x

#Swap two variables using tuple unpacking.
print('\nTuples P2')
print(coordinates[2])

#---------Dictionaries---------
#Count character frequency in a string using a dictionary.
print('\nDict P1')
word = 'banana'
freq = {}

for char in word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)

#---------Sets---------
#Remove duplicates from [1,2,2,3,4,4,5] using a set.
print('\nSets P1')
numbers_list = [1,2,2,3,4,4,5]
unique_numbers = set()

for char in numbers_list:
    if char not in unique_numbers:
        unique_numbers.add(char)
print (unique_numbers)

#Find common elements between {1,2,3} and {2,3,4}.
print('\nSets P2')
num_list_1 = {1,2,3}
num_list_2 = {2,3,4}

common = num_list_1.intersection(num_list_2)
print(common)