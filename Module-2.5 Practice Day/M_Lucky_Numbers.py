found = False
a,b = map(int,input("").split())
for i in range(a,b+1,1):
    if all(ch in '47' for ch in str(i)):
        print(i,end=' ')
        found= True
    

else:
    print(-1)
        


