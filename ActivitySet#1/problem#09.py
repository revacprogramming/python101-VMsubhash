# Lists
fname = input("Enter file name: ")
fh = open(fname,"r")
words=[]
c=fh.readlines()
for i in c:
    for j in i.split():
        if(j not in words):
            words.append(j)
words.sort()
print(words)
fh.close()