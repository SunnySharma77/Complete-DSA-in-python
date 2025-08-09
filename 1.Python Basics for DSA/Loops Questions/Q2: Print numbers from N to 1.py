#Using for loop:
N = int(input("Enter N: "))
for i in range(N, 0, -1):  # Start from N down to 1
    print(i, end=" ")
  
#Using while loop:
N = int(input("Enter N: "))
while N >= 1:
    print(N, end=" ")
    N -= 1  # Decrease by 1

