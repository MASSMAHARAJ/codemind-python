n=int(input())
a=list(map(int,input().split()))
k,l=map(int,input().split())
b=[]
for i in range(len(a)):
    if a[i]>=k and a[i]<=l:
        continue
    else:
        b.append(a[i])
if len(b)==0:
    print("-1")
else:
    print(max(b))
        