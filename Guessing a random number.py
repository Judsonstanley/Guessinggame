import random
print("enter a range greater than 0")
j = int(input("enter lowest range"))
n = int(input("Enter highest range"))
c=range(j,n)    #gets the range and assigns it to c
a = int(random.randint(j,n))    #chooses a random no.from the range and assigns it to a
print("you have 3 chances")
for i in range(3):
    b = int(input("your guess"))
    if (b!=a):
        print('Incorrect guess')
        continue;
    else:
        print("correct guess")
        break;
print("Game Over")
