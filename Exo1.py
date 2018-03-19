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
