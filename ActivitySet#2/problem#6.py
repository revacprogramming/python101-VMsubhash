class Menu:
    def __init__(self):
      return None
    def add(self,id,value):
      if id in self.foods:
        self.foods[id]+=value
      else:
        self.foods[id]=value
      return None
    def show(self):
      c=list(self.foods().copy())
      for i in c:
        print(i[0],i[1])
m = Menu()
m.add("idly", 10)
m.add("vada". 20)
m.show()
