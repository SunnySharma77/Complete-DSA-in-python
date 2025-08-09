#Using for loop:
N = int(input("Enter N: "))
total = 0
for i in range(1, N + 1):
    total += i  # Add i to total
print("Sum =", total)

#Using while loop:
N = int(input("Enter N: "))
total = 0
i = 1
while i <= N:
    total += i
    i += 1
print("Sum =", total)

