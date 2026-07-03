import time 
c=time.time()
print("The Task started at:",time.strftime("%H:%M:%S"))
a=input("Press Enter to stop the timer: ")
b=time.time()
d=b-c
min, sec = divmod(d,60)

print("The Task ended in:",int(min),":",round(sec,2))