n=int(input())
k=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n or j==k:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
    k+=1