class Menu(dict):
  def __init__(self):
    self.foods={}
  def __getitem__(self, key):
      return self.foods[key]
  def __setitem__(self, key, value):
      if(key in self.foods):
        self.foods[key]+=value
      else:
        self.foods[key]=value
  def __str__(self):
    k=""
    for a in self.foods:
      k+=(f"{a} => {self.foods[a]}\n")
    return(k[:-1])
class Order:
    def __init__(self,Menu):
      self.ord={}
      self.foods=Menu.foods
      return(None)
    def __setitem__(self, key,quant):
      if (self.foods[key]-quant)>=0:
        self.ord[key]=quant
      else:
        print("the request is over the quantity")
    def __str__(self):
      k=""
      for a in self.ord:
        k+=(f"{a} => {self.ord[a]}\n")
      return(k[:-1])
class Bill:
    """fill in class definition here"""


m = Menu()
m["idly"] = 20
m["vada"] = 20

o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2

except KeyError as e:
    print(str"e"+" is not available")
print(o)
'''
b = Bill(m, o)
print(b)'''
