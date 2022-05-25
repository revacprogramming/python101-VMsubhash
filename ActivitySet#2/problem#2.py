def add(a, b):
    return(a+b)
def output(a, b, sum):
    print(f"{a}+{b} is {sum}")
def main():
    a, b = map(int,input("input? ").split())
    sum = add(a, b)
    output(a, b, sum)
if __name__ == '__main__':
    main()
