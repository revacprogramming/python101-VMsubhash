# Tuples
fname = "dataset/mbox-short.txt"
fh = open(fname,"r")
c=fh.readlines()
dic={}
for i in c.copy():
    if(i[:5]=="From "):
        k=i.split()
        if(k[5][:2] in dic):
            dic[k[5][:2]]+=1
        else:
            dic[k[5][:2]]=1
tup=[]
keys=list(dic.keys())
values=list(dic.values())
for a in range(len(dic)):
    tup.append((keys[a],values[a]))
tup.sort()
for a in tup:
    print(a[0],a[1])
fh.close()