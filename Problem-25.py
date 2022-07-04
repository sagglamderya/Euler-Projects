a1=1
a2=2
index=3
while True:
    a3=a1+a2
    index+=1
    if len(str(a3))==1000:
        print(index)
        break
    a1=a2
    a2=a3
