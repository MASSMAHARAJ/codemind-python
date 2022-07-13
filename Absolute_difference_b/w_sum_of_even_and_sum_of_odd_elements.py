n=int(input())
a=list(map(int,input().split()))
se=0
so=0
for i in a:
    if(i%2==0):
        se+=i
    else:
        so+=i
if so>se:
    d=so-se
else:
    d=se-so
print(d)