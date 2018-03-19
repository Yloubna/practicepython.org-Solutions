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

