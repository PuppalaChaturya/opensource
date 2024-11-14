x,y=input().split()
if((x=="R" and y=="P") or (x=="P" and y=="S") or (x=="S" and y=="R")):
    print("Charan")
elif ((x=="P" and y=="R") or (x=="S" and y=="P") or (x=="R" and y=="S")):
    print("Vignesh")
else:
    print("NULL")
