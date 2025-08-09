name = input("Enter name: ")
marks = float(input("Enter marks: "))

print(f"{name} scored {marks} marks.")

#Explanation:
Uses f-string formatting for clean output 

#what is F-string
An f-string (formatted string literal) is a string in Python that's prefixed with the letter f
It provides a concise way to embed expressions inside string literals using curly braces {}
Python evaluates these expressions at runtime and inserts the results directly into the string, making it easy to create formatted output.

#Key Features
Readability: It's often more readable than older formatting methods.
Conciseness: It requires less code to achieve the same result.
Performance: F-strings are generally faster than other formatting methods.
Expression Support: You can place any valid Python expression inside the braces, including variables, function calls, and arithmetic operations.
