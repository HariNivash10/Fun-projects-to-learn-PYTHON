import time
print("Pomodoro Timer")
enter=input("Press Enter to start the timer...")
for i in range(4):
    a=1500
    b=300
    print("Pomodoro cycles Done:", i)
    print("Work for 25 minutes")
    while a>0:
        a-=1
        mins, sec=divmod(a,60)
        print("Time left:", mins, ":",sec, end="\r", flush=True)
        time.sleep(1)
    print("Take a break for 5 minutes")
    while b>0:
        b-=1
        mins, sec=divmod(b,60)
        print("Break left:", mins, ":",sec, end="\r", flush=True)
        time.sleep(1)
