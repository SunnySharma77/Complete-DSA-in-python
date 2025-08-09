#Using for loop:
N = int(input("Enter N: "))
total = 0
for i in range(1, N + 1, 2):  # Step of 2 to take only odd numbers
    total += i
print("Sum of odd numbers =", total)

#Using while loop:
N = int(input("Enter N: "))
total = 0
i = 1
while i <= N:
    total += i
    i += 2
print("Sum of odd numbers =", total)

