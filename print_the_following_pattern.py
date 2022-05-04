n=int(input())
alt=n
for i in range(1,n+1):
    alt=n
    while alt!=0:
        print(alt,end=' ')
        alt-=1
    print()