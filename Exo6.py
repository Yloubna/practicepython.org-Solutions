# Exercise 6 : String Lists
a = input("write a palyndrome word : ")
print a+" -->"
rvs = a[::-1]
print rvs+" <--"
if rvs != a:
    print "this is not a palyndrome word"
else:
    print "this is a palyndrome word"
