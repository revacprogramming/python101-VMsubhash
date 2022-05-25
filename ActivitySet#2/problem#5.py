def get_cs():
    return(input())
def cs_to_dict(cs):
    di={}
    x=cs.split(';')
    for a in x:
      c=a.split("=")
      di[c[0]]=c[1]
    return(di)
def dict_to_cs(d):
  s=list(d.keys())[0]+"="+list(d.values())[0]
  for a in range(1,len(d)):
    s+=";"+list(d.keys())[a]+"="+list(d.values())[a]
  return(s)
def main():
    cs = get_cs()
    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)
    cs = dict_to_cs(d)
    print(cs)
if __name__ == '__main__':
    main()
