x,y,z=map(int,input().split())
if(x<=z):
    if(x+y<=z):
        print("2")
    else:
        print("1")
else:
    print("0")
