fname = input("Enter file name: ")
fh = open(fname,"r")
value=0
number=0
for i in fh:
    if(i.find("X-DSPAM-Confidence:")!=-1):
        value+=float(i[i.find("0."):])
        number+=1
print(f"Average spam confidence: {value/number}")
fh.close()