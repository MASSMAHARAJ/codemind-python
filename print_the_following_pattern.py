n=int(input())#4
k=2*n-1       #7
for i in range(0,k):
    if i>=n-1:
        print('*',end='')
    else:
        print(" ",end='')
print()
for i in range(0,n-2):#0,1
    k-=1#6
    for j in range(0,k):#0-5
        if j==k-n or j==k-1:
            print("*",end='')
        else:
            print(' ',end='')
    print()
for i in range(0,n):
    print('*',end='')
'''
0123456
   ****
  *  *
 *  *
****


'''
