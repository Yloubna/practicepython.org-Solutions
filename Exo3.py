# Exercise 3 : List Less Than Ten
a = [1, 1, 2,65, 3,28, 5, 8, 13, 21, 34, 55, 89]
print a
b = []
number = input('enter a number : ')

# by using List Comprehensions
b = [x for x in a if x<number]
print b

# an other solution
for num in a:
    if num < number:
        b.append(num)
print b
