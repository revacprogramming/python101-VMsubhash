j=[]
while True:
    c=input("enter the number")
    if(c=="done"):
        break
    try:
        j.append(int(c))
    except:
        print("Invalid input")
print(f"Maximum is {max(j)}\nMinimum is {min(j)}")
