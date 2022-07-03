def operation(s1,s2,op):
  a=list(set([*s1,*s2]))
  if "u" == op:
    return(a)
  elif "n" == op:
    for i in a.copy():
        if(i not in s1):
            a.remove(i)
        elif(i not in s2):
            a.remove(i)
    return(a)

def main():
  set1=list(map(int,input("Enter Set1? ").split()))
  set2=list(map(int,input("Enter Set2? ").split()))
  q=input("Enter operation (u/n)? ")
  set3=operation(set1,set2,q)
  print("Set3:",*set3)
main()

