
# Exercise Lab 1: Iterating Through Strings
word = input("Please enter a word: ")

result = False

for letter in word:
    if letter.isupper():
        result = True
        break

print(result)   

# Exercise Lab 2: Adding All Numbers of a List

numbers = [2, 3, 10]
sum = 0

for number in numbers:
    sum += number

print(sum)

# Exercise Lab 3: Removing Items From a List

items = ['lion', 'witch', 'wardrobe']

user_choice = input("Which item would you like to remove? ")

if user_choice in items:
    items.remove(user_choice)
    print(True)
else:
    print(False)

print(items)
