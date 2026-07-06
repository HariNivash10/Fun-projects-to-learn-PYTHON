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
        break
    elif y>n:
        print("Your number is larger")
    elif y<n:
        print("Your number is smaller")

with open("NumberGuess/game_history.txt","r") as file:
    for line in file:
        if ":" in line:
            names, score = line.split(":")
            attempts = int(score.split()[0])
            scores[names.strip()] = attempts

if name in scores and c < scores[name]:    
    scores[name] = c
elif name not in scores:
    scores[name] = c
with open("NumberGuess/game_history.txt","w") as file:
    for names,attempts in scores.items():
        file.write(f"{names}: {attempts} attempts\n")
    