import random
best_player=None
score=10000
try:
    with open("NumberGuess/game_history.txt","r") as file:
        for line in file:
            print(line,end="")
            if ":" in line:
                name, attempts = line.split(":")
                attempt= int(attempts.split()[0])
                if attempt < score:
                    best_player=name
                    score=attempt
        print("High score")
        print(f"{best_player}: {score}")
except:
    print("No high score yet")
n=random.randrange(1000,10000)
name=input("Write your name: ")
c=0
while True:
    try:
        y=int(input("Write your number: "))
    except:
        print("Enter a valid number, for eg(2345)")
        continue
    c+=1
    if y==n:
        print("Congrulations, You gussed it right")
        print("You gussed it in",c,"attempts")
        with open("NumberGuess/game_history.txt","a") as file:
            file.write(f"{name}: {c} attempts\n")
        break
    elif y>n:
        print("Your number is larger")
    elif y<n:
        print("Your number is smaller")

    