#Create a list of furits
fruits = ["apple", "banana", "cherry"]
first_fruit = fruits[0]
print(first_fruit)
# Output: apple

fruits[1] = "blackberry"
print(fruits)
# Output: ['apple', 'blackberry', 'cherry']
fruits.append("dates")
print(fruits)
# Output: ['apple', 'blackberry', 'cherry', 'dates']
fruits.insert(1, "blueberry")
print(fruits)
# Output: ['apple', 'blueberry', 'blackberry', 'cherry', 'dates']
fruits.remove("blueberry")
print(fruits)
# Output: ['apple', 'blackberry', 'cherry', 'dates']
fruits.pop()
print(fruits)
# Output: ['apple', 'blackberry', 'cherry']
fruits.pop(1)
print(fruits)
# Output: ['apple', 'cherry']
fruits.clear()
print(fruits)
# Output: []
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)
# Output: ['cherry', 'banana', 'apple']
fruits.sort()
print(fruits)
# Output: ['apple', 'banana', 'cherry']
fruits.sort(reverse=True)
print(fruits)
# Output: ['cherry', 'banana', 'apple']
fruits = ["apple", "banana", "cherry"]
new_fruits = fruits.copy()
print(new_fruits)
# Output: ['apple', 'banana', 'cherry']
new_fruits = list(fruits)
print(new_fruits)
# Output: ['apple', 'banana', 'cherry']
new_fruits = fruits[:]
print(new_fruits)
# Output: ['apple', 'banana', 'cherry']
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])
# Output:
# apple
# banana
# cherry
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
# Output:
# apple
# banana
# cherry
fruits = ["apple", "banana", "cherry"]
[print(fruit) for fruit in fruits]
# Output:
# apple
# banana
# cherry
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

# Output: []
fruits = ["apple", "banana", "cherry"]
del fruits
# print(fruits)
# Output: NameError: name 'fruits' is not defined
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
# Output: ['apple', 'cherry']
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)
# Output: ['apple', 'cherry']
