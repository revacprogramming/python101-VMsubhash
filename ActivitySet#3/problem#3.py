def pal(s):
    return(s==s[::-1])
for _ in range(int(input())):
    n=int(input())
    s=input()
    print(s)
    for a in range(0,n-3):
        for b in range(2,n):
            if(pal(s[a:b+1]) and len(s[a:b+1])>=3):
                    print(a+1,s[a:b+1])
    print("")