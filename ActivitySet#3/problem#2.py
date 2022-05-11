import math
def find_fraction(l):
  den=1
  num=0
  for i in l:
    den*=i
  for i in l:
    num+=den/i
  hcf=math.gcd(int(num),int(den))
  return([num/hcf,den/hcf])
for _ in range(int(input())):
  n=int(input())
  l=list(map(int,input().split()))
  fr=find_fraction(l)
  for i in l[:-1]:
    print(f"1/{i} + ",end="")
  print(f"1/{l[n-1]} = {int(fr[0])}/{int(fr[1])}")
"""
to run code -> python ActivitySet#3/problem#2.py

sample input

3
2
2 10
1
35
4
98 1 2 12
"""
