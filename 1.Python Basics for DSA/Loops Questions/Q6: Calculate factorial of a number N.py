#Using for loop:
N = int(input("Enter N: "))
fact = 1
for i in range(1, N + 1):
    fact *= i  # Multiply fact by i
print("Factorial =", fact)

#Explanation:
Start fact = 1 because multiplying by 0 will always be 0
Multiply fact by each number from 1 to N

#Using while loop:
N = int(input("Enter N: "))
fact = 1
i = 1
while i <= N:
    fact *= i
    i += 1
print("Factorial =", fact)

