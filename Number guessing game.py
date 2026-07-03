import random
n=random.randrange(1000,10000)
c=0
while True:
    y=int(input("Write your number: "))
    c+=1
    if y==n:
        print("Congrulations, You gussed it right")
        print("You gussed it in",c,"attempts")
        break
    elif y>n:
        print("Your number is larger")
    elif y<n:
        print("Your number is smaller")