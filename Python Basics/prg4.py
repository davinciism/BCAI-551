#Program to swap two numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before Swapping: ")
print("a = ", a, ", b = ", b)

temp = a
a = b
b = temp

print("After Swapping: ")
print(f"a = {a}, b = {b}")