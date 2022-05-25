def get_cs():
    return(input())
def cs_to_lot(cs):
  lt=[]
  x=cs.split(';')
  for i in x:
    y=i.split('=')
    lt.append((y[0],y[1]))
  return(lt)
def lot_to_cs(lot):
    l=[]
    for a in lot:
      l.append("=".join(a))
    return(";".join(l))
def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
