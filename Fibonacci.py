# Create a list of fibonacci numbers using python

a = 0
b = 1
f = [a, b]
count = 0
n = int(input("Input an integer between 2 and 50 here: "))

if(n>50):
    print('This number is too high, try again')
elif(n<2):
    print('This number is too low, try again')
elif(n<0):
    print('This is a negative, try again')
else:
    while(count<=n-3):
    #while(f[-1]<=100):
        c = a + b
        f.append(c)
        a = b
        b = c
        count+=1

    #print(a)
    #print(b)
    n = str(n)
    print("The first " + str(n) + " numbers in the fibonacci sequence are: ")
    print(f)
    #print('The 6th fibonacci number is: ')
    #print(f[5])




















