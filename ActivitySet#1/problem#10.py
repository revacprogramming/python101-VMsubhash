fname = input("Enter file name: ")
fh = open(fname,"r")
c=fh.readlines()
dic={}
for i in c.copy():
    if(i[:5]=="From "):
        k=i.split()
        if(k[1] in dic):
            dic[k[1]]+=1
        else:
            dic[k[1]]=1
m=max(dic.values())
print(list(dic.keys())[list(dic.values()).index(m)],m)
fh.close()

