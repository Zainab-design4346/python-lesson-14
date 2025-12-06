def fun1(bill,tip):
    t = round(bill * (0.03*tip))
    print("Bill amount:",(bill+t))


b=int(input("Enter bill amount: "))
t=int(input("Enter tip amount: "))
fun1(b,t)