n_times = int(input("How many numbers? "))
total = 0
largest = None
smallest = None

for loop in range(1, n_times + 1):
    num = float(input("Enter number " + str(loop) + ": "))
    total = total + num

    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

average = total/n_times

print("Sum: ", total)
print("Average: ", average)
print("Largest: ", largest)
print("Smallest: ", smallest)
