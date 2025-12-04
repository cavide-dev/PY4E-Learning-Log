def computepay(h,r):
    if h <= 40:
        pay = h * r
    else:
        normal_pay = 40 * r
        new_rate = r * 1.5
        extra_hours = h - 40
        pay = normal_pay + (new_rate * extra_hours)
    return pay

hours = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hours)
r = float(rate)
print("Pay",computepay(h,r))
