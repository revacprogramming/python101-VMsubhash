# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname,"r")
c=fh.readlines()
value=0
number=0
for i in c:
    if(i.find("X-DSPAM-Confidence:")!=-1):
        value+=float(i[i.find("0."):])
        number+=1
print(f"Average spam confidence: {value/number}")
fh.close()