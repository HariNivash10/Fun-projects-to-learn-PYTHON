import time
a=time.ctime()
print(a)
b=a[11:16]
c=(int(b[0:2]))
if c>=5 and c<=11:
    print("Good Morning Sir")
elif c>=11 and c<=16:
    print("Good Afternoon Sir")
elif c>=16 and c<=20:
    print("Good Evening Sir")
else:
    print("Good Night Sir")