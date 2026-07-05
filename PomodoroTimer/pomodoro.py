import time
print("Pomodoro Timer")
enter=input("Press Enter to start the timer...")
for i in range(1,5):
    a=1500
    b=300
    print("Work for 25 minutes")
    while a>0:
        mins, sec=divmod(a,60)
        print(f"Time left: {mins:02d}:{sec:02d}", end="\r", flush=True)
        time.sleep(1)
        a-=1
    print("Take a break for 5 minutes")
    while b>0:
        mins, sec=divmod(b,60)
        print(f"Break left:{mins:02d}:{sec:02d}", end="\r", flush=True)
        time.sleep(1)
        b-=1
    print("Pomodoro cycles Done:", i)
print("Awesome, Task finished")
