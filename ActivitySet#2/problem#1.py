def add(a, b):
  return(a+b)
def main():
  a = int(input("Enter 1st Number? "))
  b = int(input("Enter 2nd Number? "))
  c = add(a, b)
  print(f"Sum of {a} and {b} is {c}")
main()