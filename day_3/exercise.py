# 1 
age = 18

# 2
height = 1.82

# 3
complex_num = 3 + 4j   

# 4
base = int(input("Enter base of the triangle: "))
height_of_triangle = int(input("Enter height of the triangle: "))
area_of_triangle = 0.5 * base * height_of_triangle
print("Area of the triangle is:", area_of_triangle)

# 5
side_a = int(input("Enter side a of the triangle: "))
side_b = int(input("Enter side b of the triangle: "))   
side_c = int(input("Enter side c of the triangle: "))
perimeter_of_triangle = side_a + side_b + side_c
print("Perimeter of the triangle is:", perimeter_of_triangle)

# 6
length = int(input("Enter length of the rectangle: "))
width = int(input("Enter width of the rectangle: "))
area_of_triangle = length * width
perimeter_of_triangle = 2 * (length + width)
print("Area of the rectangle is:", area_of_triangle)
print("Perimeter of the rectangle is:", perimeter_of_triangle)
 
# 7
r = int(input("Enter radius of the circle: "))
PI = 3.14
area_of_circle  = PI * r ** 2
circum_of_circle = 2 * PI * r
print("Area of the circle is:", area_of_circle)
print("Circumference of the circle is:", circum_of_circle)
 
# 8
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
print("Slope of the line is:", slope)

# 9
dx = x2 - x1
dy = y2 - y1
euclidean_distance = (dx ** 2 + dy ** 2) ** 0.5
print("Euclidean distance is:", euclidean_distance)

# 18
a = 7/3
b = 2.7
if a == b:
    print("The value of a and b are equal.", a, b)
else:
    print("The value of a and b are not equal.", a, b)

# 19
a = '10'
b = 10
if type(a) == type(b):
    print("The variable a and b are of the same type.", type(a), type(b))
else:
    print("The variable a and b are of different types.", type(a), type(b))
    
# 20
n = int(input("Enter a number: "))
h = float(input("Enter a number: "))
if n == h:
    print("The number", n, "is equal to", h)
else:
    print("The number", n, "is not equal to", h)
    
# 21
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
weekly_earnings = hours * rate_per_hour
print("Weekly earnings are:", weekly_earnings)

# 22
number_of_years = int(input("Enter number of years you have lived: "))
seconds_in_a_year = 365 * 24 * 60 * 60
age_in_seconds = number_of_years * seconds_in_a_year
print("Your age in seconds is:", age_in_seconds, "seconds.")

# 23
a = 1
b = 2
c = 3
d = 4
e = 5
f = 8
g = 9
h = 16
i = 25
j = 27
k = 64
l = 125
print(a, '', a, '', a, '', a, '', a)
print(b, '', a, '', b, '', d, '', f)
print(c, '', a, '', c, '', g, '', j)
print(d, '', a, '', d, '', h, '', k)
print(e, '', a, '', e, '', i, '', l)



























