def area(f):
  a=f[0]*(f[3]-f[5])
  b=f[2]*(f[5]-f[1])
  c=f[4]*(f[1]-f[3])
  return(abs(a+b+c))
  
for _ in range(int(input())):
  l=list(map(float,input().split()))
  print(f"Area of rectangle with vertices ({l[0]},{l[1]}),({l[2]},{l[3]}),({l[4]},{l[5]}) is {area(l)}")
