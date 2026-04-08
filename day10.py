name = input("Enter your name: ")
age = int(input("Enter your age: "))

city = input("Enter your city: ")


birth_year = 2026 - age

letters = len(name)
if letters % 2==0:
    odd_even = "is Even"
else:
    odd_even = "is Odd"


if age < 13:
    greeting = "You're a kid!"
elif age <= 17:
    greeting = "Teenager alert!"
elif age <= 60:
    greeting = "Welcome, Adult"
else:
    greeting = "Respect, elder!"


print("============================")
print("        PROFILE CARD")
print("============================")
print("Name      :", name.upper())
print("Age       :", age)
print("City      :", city)
print("Letters   :", letters, "(" + odd_even + ")")
print("Birth Year:", birth_year)
print("Greeting  :", greeting)
print("============================")
