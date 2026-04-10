num = int(input("Enter a number: "))
length = int(input("How far? --> "))

for loop in range(1, length + 1):
    result = num * loop
    print(num, "x", loop, "=", result)
