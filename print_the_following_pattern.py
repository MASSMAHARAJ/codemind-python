n=int(input())
m=n+1
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i or j==m-i:
            print("x",end='')
        else:
            print(0,end='')
    print()