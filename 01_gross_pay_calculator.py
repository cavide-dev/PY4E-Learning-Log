hours = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hours)
r = float(rate)

if h <= 40 :
    pay = h * r

else :
    normal_pay = 40 * r
    higher_rate = r * 1.5
    extra_hours = h - 40
    pay = normal_pay + (higher_rate * extra_hours)


print(pay)

# For hours : 45 , rate : 10.50