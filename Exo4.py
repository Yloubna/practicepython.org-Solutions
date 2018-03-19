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