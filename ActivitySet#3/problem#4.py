def decod(l,n):
    d=[]
    while len(l)!=0:
        if(l[0]!=0):
            d.append(l[0])
            l.remove(l[0])
        elif(l[0]==0 and l[1]==0):
            d.append(0)
            l.remove(0)
            l.remove(0)
        else:
            for i in range(l[1]):
                d.append(l[2])
            l.remove(l[0])
            l.remove(l[0])
            l.remove(l[0])
    return(d)
            
    
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d=decod(l.copy(),n)
    for a in l:
        print(a,end=" ")
    print("")
    for a in d:
        print(a,end=" ")
    print("\n")
