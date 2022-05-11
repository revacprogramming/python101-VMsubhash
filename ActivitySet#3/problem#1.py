def area(f):
  a=f[0]*(f[3]-f[5])
  b=f[2]*(f[5]-f[1])
  c=f[4]*(f[1]-f[3])
  return(abs(a+b+c))
  
for _ in range(int(input())):
  l=list(map(float,input().split()))
  print(f"Area of rectangle with vertices ({l[0]},{l[1]}),({l[2]},{l[3]}),({l[4]},{l[5]}) is {area(l)}")
"""
to run code -> python ActivitySet#3/problem#1.py

sample input

3
0.0 0.0 0.0 1.0 1.0 0.0
-1.0 2.0 3.0 5.0 1.0 1.0
5.0 9.0 -0.5 0.0 7.5 5.0
"""