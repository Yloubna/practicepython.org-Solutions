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