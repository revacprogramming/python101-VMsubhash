class marks:
  def __init__(self,name):
    self.name=name
    self.marks=[]
    return(None)
  def __add__(self,m):
    self.marks.append(m)
    return(self)
  def __str__(self):
    return(f"Total marks = {sum(self.marks)}\nseperate marks = {self.marks}\navearge = {sum(self.marks)/len(self.marks)}")
a=marks("subash")
a+10+10+15+15+14+14
print(a.name)
print(a)
"""
                       output
subash
Total marks = 78
seperate marks = [10, 10, 15, 15, 14, 14]
avearge = 13.0
"""