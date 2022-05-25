def get_cs():
    return(input())
def cs_to_lot(cs):
    c=cs.split(";")
    l=[]
    for i in c:
      k=i.split("=")
      l.append((k[0],k[1]))
    return(l)
def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)
if __name__ == '__main__':
    main()
