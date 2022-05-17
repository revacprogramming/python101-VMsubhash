import numpy as np
b2=[0,3,6,9]
for _ in range(int(input())):
    g=[]
    row=[]
    column=[]
    subma=[]
    valid=True
    for a in range(9):
        g.append(list(map(int,input().split())))
    a=np.array(g)
    if(0 not in a):
        print("complete")
    else:
        for i in range(9):
            for j in range(1,10):
                if(sum(a[i]==j)>=2):
                    row.append(i+1)
                    valid=False
        for i in range(9):
            for j in range(1,10):
                if(sum(a[:,i]==j)>=2):
                    column.append(i+1)
                    valid=False
        for i in range(1,4):
            for j in range(1,4):
                k=a[b2[i-1]:b2[i],b2[j-1]:b2[j]]
                for r in range(1,10):
                    if(sum(sum(k==r))>=2):
                        subma.append(((i-1)*3)+j)
                        valid=False
                
        if valid:
            print("incomplete but viable")
        else:
            print("non-viable\n  rows: ",end="")
            for i in row:
                print(i,end=" ")
            print("")
            print("  columns: ",end="")
            for i in column:
                print(i,end=" ")
            print("")
            print("  sub-matrices: ",end="")
            for i in subma:
                print(i,end=" ")
            print("")

                
        
    
