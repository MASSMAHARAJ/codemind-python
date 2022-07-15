x,y=map(int,input().split())
if (x+y*2)%2!=0:
    print("NO")
elif x==0 and y%2==1:
    print("NO")
else:
    print("YES")