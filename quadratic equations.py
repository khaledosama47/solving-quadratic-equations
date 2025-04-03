import math  
a = float(input("Enter the value of a (coefficient of x²): "))
b = float(input("Enter the value of b (coefficient of x): "))
c = float(input("Enter the value of c (constant term): "))
d = b**2 - 4*a*c
if d > 0:  
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print(f"The two real roots are: x1 = {x1}, x2 = {x2}")
elif d == 0:  
    x = -b / (2*a)
    print(f"The single real root is: x = {x}")
else: 
    real_part = -b / (2*a)
    imag_part = math.sqrt(-d) / (2*a)
    print(f"The two imaginary roots are: x1 = {real_part} + {imag_part}i, x2 = {real_part} - {imag_part}i")