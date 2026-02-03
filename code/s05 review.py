# to make sure input is an integer
a = input("enter an integer:")
a = int(a)
print(type(a))

# check odd or even
if a % 2 == 0:
    print('even')
else:
    print("odd")