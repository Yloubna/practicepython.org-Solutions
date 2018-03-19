def get_number(help_text):
    return input(help_text)

def check(num):
    a = [x for x in range(1,num) if num%x==0]
    if len(a)>1:
        print "this is not a prime number"
    else:
        print "this number is prime"
    
number = get_number("please enter a number : ")
check(number)
