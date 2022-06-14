class Menu:
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
m = Menu()
m["idly"] = 10
m["vada"] = 20
print(m)
