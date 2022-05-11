def computepay(h, r):
    return h*r if h<40 else (40*rate)+((h-40)*1.5*rate)

hrs = float(input("Enter Hours:"))
rate=float(input("Enter rate:"))
p = computepay(hrs, rate)
print("Pay", p)