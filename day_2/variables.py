# EXERCISE 1
# 2
print("Day 2: 30 Days of Python Programming")
# 3
first_name = "Gia Khiem"
# 4
last_name = "Nguyen"
# 5
full_name = first_name + " " + last_name
# 6
country = "Vietnam"
# 7
city = "Ho Chi Minh City"
# 8
age = "18"
# 9
year = "2025"
# 10
is_married = False
# 11
is_true = True
# 12
is_light_on = False
# 13 delcare multiple variables in one line
name, job, live = "Alice", "Engineer", "USA"
print("First Name:", first_name)
print("Last Name:", last_name)
print("Full Name:", full_name)
print("Country:", country)
print("City:", city)
print("Age:", age)
print("Year:", year)
print("Is Married:", is_married)
print("Is True:", is_true)
print("Is Light On:", is_light_on)
# EXERCISE 2
# 1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(age))
print(type(is_married))
print(type(is_light_on))
print(type(year))
print(type(country))
print(type(city))

# 2
print(len(first_name))
print(len(last_name))
print(len(full_name))
print(len(age))
# Boolean values do not have length
print(len(year))
print(len(country))
print(len(city))

# 3
if len(first_name) > len(last_name):
    print("First name is longer than last name.")
elif len(first_name) < len(last_name):
    print("Last name is longer than first name.")
else:
    print("First name and last name are of equal length.")

# 4
num_one = 5
num_two = 4

# 5
total = num_one + num_two

# 6
diff = num_one - num_two

# 7
product = num_one * num_two

# 8
division = num_one / num_two

# 9
remainder = num_one % num_two

# 10
exp = num_one ** num_two

# 11
floor_div = num_one // num_two

# 12
R = int(input("Enter the radius of the circle: "))
PI = 3.14
area_of_circle = PI * R ** 2
circum_of_circle = 2 * PI * R

# 13
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)
print(num_one, num_two, total, diff, product, division, remainder, exp, floor_div)
print(R, PI, area_of_circle, circum_of_circle)
