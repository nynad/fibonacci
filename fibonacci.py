# the fibonacci always starts at 0 and 1. 
# you add 0+1, and get 1. so now, the sequence of numbers is 0,1,1.
# take the last 2 (1,1) and add them. 0,1,1,2 is now the sequence. now you add 1+2. and so on!

a=7

def fib(a):
    if a==2:
        return 1 
    elif a==1:
        return 0
    elif a<=0:
        print("Incorrent Input. Cannot calculate the sequence.")
    else: 
        return fib(a-1) + fib(a-2)

    
value=fib(a)
print(value)

# the number of times the fibonacci sequence repeats is a, it's also the number of splits that will occur until the sequence cannot break anymore.
# adding all the leftover ones gives us our return value, because hitting 2 will just directly give us 1 as a return value 
