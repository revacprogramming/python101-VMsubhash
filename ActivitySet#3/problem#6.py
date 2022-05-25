a=[1,1,2]
def ways(x):
    if(x+1<=3):
        return(a[x])
    for i in range(2,x):
        a[0],a[1],a[2]=a[1],a[2],a[0]+a[1]+a[2]
    return(a[2])
for _ in range(int(input())):
    n=int(input())
    print(f"{n} points: {ways(n)} ways")
