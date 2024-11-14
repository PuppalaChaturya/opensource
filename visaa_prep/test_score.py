n,x,y=map(int,input().split())
if(0<=y<=n*x):
    if(y%x==0):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
