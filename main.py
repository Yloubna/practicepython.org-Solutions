import time
import random

# exercise 1 : Character Input
print "When will I turn 100 ?"
name = input("please enter your name: ")
age = int(input("please enter your age : "))
hundred = (2018 - age)+100
msg = (name+", today You are " +str(age)+"yo, you will turn 100yo by "+str(hundred)+"\n")
print msg
repeat = input("How many times do you want to read this foolish message ? ")

# using while loop
while repeat!=0:
    print msg
    time.sleep(2)
    repeat = repeat-1

# without using loop
print (repeat*msg)

print "done !"


#exercise 2 : Odd (impair) Or Even (pair)
numb = int(input("please enter a number of your choice : "))
if (numb%4==0):
    print "this number is a multiple of 4"
elif (numb%2==0):
    print "this number is Even"
else:
    print 'this number is Odd'

check = int(input("please enter an other number : "))
if (numb%check)!=0:
    print str(numb)+" doesn't divide evenly into "+str(check)
else:
    print str(numb)+" divides evenly into "+str(check)


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


# Exercise 4 : Divisors
number = input("please enter a number : ")
# using list comprehensions 
a = [x for x in range(1,number) if number%x==0]

# using loop
i = 1
while i<number:
    if (number%i)==0:
        a.append(i)
    i +=1

print a


# Exercise 5 : List Overlap
a = random.sample(xrange(100), random.randint(1, 11))
b = random.sample(xrange(100), random.randint(1, 11))
print a
print b
c = [x for x in a if x in b]
print c


# Exercise 6 : String Lists
a = input("write a palyndrome word : ")
print a+" -->"
rvs = a[::-1]
print rvs+" <--"
if rvs != a:
    print "this is not a palyndrome word"
else:
    print "this is a palyndrome word"

