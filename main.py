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
b = random.sample(xrange(100), random.randint(1, 18))
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


# Exercise 7 : List Comprehension
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if x%2==0]
print a
print b


# Exercise 8 : Rock Paper Scissors
print "Welcome to Rock Paper Scissors game \n play R for Rock, S for Scissors and P for Paper"
gameover = 1
while gameover!=0:
    player1 = input("Player1 your turn : ")
    player2 = input("Player2 your turn : ")
    if player1=="R":
        if player2=="S":
            print "Player1 wins !"
        elif player2=="P":
            print "Player2 wins !"
        else:
            print "match nul"
    elif player1=="S":
        if player2=="R":
            print "Player2 wins !"
        elif player2=="P":
            print "Player1 wins!"
        else:
            print "match nul"
    elif player1=="P":
        if player2=="R":
            print "Player1 wins !"
        elif player2=="S":
            print "Player2 wins !"
        else:
            print "match nul"
    else:
        "You must enter R or S or P"
    gameover = int(input("enter 0 to quit or anything other integer to continue : "))

# Exercise 9 : Guessing Game One
while True:
    the_number = random.randint(1,9)
    userinput = input("Guess a new number between 1 and 9 : ")
    if userinput==the_number:
        print "You guessed exactly right ! congratulations !"
    elif userinput>the_number:
        print "Too hight"
        print "the number was "+str(the_number)
    else:
        print "Too low"
        print "the number was "+str(the_number)

# Exercise 10 : go back to Exercise 5
