def computepay(h,r):
    pay=0.0

    if(h<=40):
        pay=h*r
    if(h>40):
        pay=(40*r)+((h-40)*r*1.5)
        
    return pay

hrs = input("Enter Hours:")
rate = input("Enter rate:")
h = float(hrs)
r = float(rate)

p = computepay(h,r)
print("Pay",p)