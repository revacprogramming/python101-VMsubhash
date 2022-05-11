hrs = float(input("Enter Hours:"))
rate= float(input("Enter rate:"))
pay=hrs*rate if hrs<40 else (40*rate)+(1.5*(hrs-40)*rate)
print(pay)