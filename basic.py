# Basic Calculator

#works on integers
def add(x,y):
    return int(x) + int(y)

print("Please enter your operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("Q Quit")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/Q): ")
    if choice.lower() == "q":
        break
    first = input("Enter first number: ")
    second = input("Enter second number: ")
    if choice == "1":
        print("Answer: " add(first,second))
    if choice == "2":
        print("Not Implemented yet")
    if choice == "3":
        print("Not Implemented yet")
    if choice == "4":
        print("Not Implemented yet")
