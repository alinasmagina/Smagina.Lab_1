import math
 
print("Введіть координати та радіус сфери")
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
r = float(input("R = "))
 
r_xy = math.sqrt(x**2 + y**2 + z**2)
 
if r_xy <= r:
	print("Точка належить сфері")
else:
	print("Точка не належить сфері")
