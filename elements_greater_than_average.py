n=int(input())
s=0
c=0
a=list(map(int,input().split()))
for i in range(0,len(a)):
    s+=a[i]
avg=s//n
for i in range(0,len(a)):
    if avg<=a[i]:
        c+=1
print(c)