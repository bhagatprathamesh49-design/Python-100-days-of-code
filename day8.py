celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is: ", fahrenheit)
if celsius < 0:
    print("Freezing ❄")
elif celsius <= 25:
    print("Pleasant ☀")
else:
    print("Hot! ♨")
