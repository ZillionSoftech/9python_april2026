count=0
i=1
while(i<=9):
    if i<=5:
        count+=1
    else:
        count-=1

    j=1
    while(j<=count):
        print(j,end="")
        j+=1
    print()
    i+=1