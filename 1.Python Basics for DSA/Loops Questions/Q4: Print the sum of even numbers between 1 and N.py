#Using for loop:

N = int(input("Enter N: "))
total = 0
for i in range(2, N + 1, 2):  # Step of 2 to take only even numbers
    total += i
print("Sum of even numbers =", total)

#Using while loop:
  
N = int(input("Enter N: "))
total = 0
i = 2
while i <= N:
    total += i
    i += 2
print("Sum of even numbers =", total)
