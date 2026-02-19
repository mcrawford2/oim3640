# for i in range(5):
#     print(i)

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# response = ""
# while response != "quit":
#     response = input("Enter command: ")
#     print(f"You said: {response}")

#ask AI to generate a very simple log in system using while loop
#response: Sorry, you have been rate-limited. Please wait 65 minutes before trying again.

#Example: Simple Password System

#print("\n --- Simple Password System ---")
#username = "admin"
#password = "password123"

#while True:
#    result = game_loop()
#    if result == "game over":
#        break

#break as a way to exit the loop
#words = ["hello", "world", "target", "python"]
#for w in words:
#    print('checking:', w)
    # if w == "target":
    #     print("Target found!")
    #     break

# words = ["hello", "world", "target", "python"]
# for w in words:
#     print('checking:', w)
#     if w == "target":
#         print("Target found!")
#         continue
#     print("Not the target\n")

# # continue - skip to the next iteration
# for num in range (10):
#     if num % 2 == 0:
#         continue
#     print(num) #prints odd numbers only

def f(n):
    for num in range(n):
        if num % 2 == 0:
            continue
        return num #returns the first odd number, which is one, and then exits the function
    
print(f(10))

