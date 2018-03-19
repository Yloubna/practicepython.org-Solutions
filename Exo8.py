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
