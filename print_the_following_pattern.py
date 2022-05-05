n=int(input())
k=2*n-1
k1=n
k2=n
for i in range(1,n+1):
    for j in range(1,k2+1):
        if j>=k1 and j<n:
            print(m,end='')
            m-=1
        elif j>=n and j<=k2:
            print(j-n,end='')
        else:
            print(" ",end='')
    print()
    k1-=1
    k2+=1
    m=i

