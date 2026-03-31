num = 100
try:
    a = float(input("Enter a number to divide by: "))
    print(num / a)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid number.")
finally:
    print("We still want to print this.")

print("Let's move on to the next part of the code.")

names = ["Alice", "Bob", "Charlie"]

for name in names:
    try:
        print(name.upper())
    except AttributeError:
        print(f"Error: Name '{name}' is not a string and cannot be converted to uppercase.")

print("Uppercase names:", [name.upper() for name in names])

print("Let's move on to the next part of the code.")
