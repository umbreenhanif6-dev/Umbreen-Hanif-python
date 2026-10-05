name = "Umbreen"
age = 40
height = 5.5
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

name = input("What is your name? ")
name1 = name.capitalize()
year = input("What year were you born? ")
age = int(2026 - int(year))
print(f"Hi, {name}! You are approximately {age} years old.")


# Add to your script: use input() to ask for the user's name and the year they
# were born. Compute their approximate age and print a sentence.
# The example below shows the format — your greeting will use the name
# and birth year the user types:Hi, Jordan! You are approximately 24 years old.

# Add to your script: ask the user to enter two numbers (as separate inputs).
# Convert both to float, multiply them, and print the result using an f-string.
# The example below shows the format — your two numbers and their product
# will differ: 12.5 × 4.0 = 50.0

length = float(input("Length: "))
width = float(input("Width: "))
area = length * width
print(f"{length} × {width} = {area}")
#
#
#Add to your script: using only variables and print()
#— no input() — print a formatted receipt.
#Store the item name, price, and quantity in variables,
#and compute the total from those variables:

#Add to your script: using only variables and print()
#— no input() — print a formatted receipt.
#Store the item name, price, and quantity in variables,
#and compute the total from those variables:


item = "Fundamentals of Calculus"
price = 54.00
quantity = 10
total = price * quantity

print("================================")
print("             RECEIPT            ")
print("================================")
print(f"Item:     {item}")
print(f"Price:    ${price}")
print(f"Quantity: {quantity}")
print(f"Total:    ${total:.2f}")
print("================================")

#Finally, tie it all together. Use input() to ask the user for:
#Their name
#Their hometown
#Their favorite hobby
#One fun fact about themselves
#The year they were born

fname = input("What is your first name? ")
lname = input("What is your last name? ")
name = fname.capitalize() + " " + lname.capitalize()
city = input("Which city were you born in? ")
state = input("Which state were you born in? ")
city1 = city.capitalize()
state1 = state.upper()
hometown = city1 + "," + " " + state1
hobby = input("What is your favorite hobby? ")
hobby1 = hobby.capitalize()
fun_fact = input("What is a fun fact about yourself? ")
fun_fact1 = fun_fact.capitalize()
year = input("What year were you born? ")
age = int(2026 - int(year))

print("=========================================")
print(f"         PROFILE: {name}                ")
print("=========================================")
print(f"Hometown:    {hometown}")
print(f"Hobby:       {hobby1}")
print(f"Fun Fact:    {fun_fact1}")
print(f"Age:         {age}")
