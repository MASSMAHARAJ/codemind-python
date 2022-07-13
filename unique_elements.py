n=int(input())
a=list(map(int,input().split()))
m=set(a)
c=[]
for i in a:
    if i in m:
        c.append(i)
        m.remove(i)
print(*c)