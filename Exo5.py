# Exercise 5 : List Overlap
a = random.sample(xrange(100), random.randint(1, 11))
b = random.sample(xrange(100), random.randint(1, 18))
print a
print b
c = [x for x in a if x in b]
print c
