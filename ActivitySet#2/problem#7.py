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


class Menu:
    """fill in class definition here"""


m = Menu()
m = m + ("idly", 10) + ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)

print(m)  # should print the menu properly
