#for i in range (1, 4):
#    print("Interation:", i)
#    print("Square:", i * i)

#for i in range(1, 6, 2):
#    print(i)

#name = 'Miranda'
#print(type(name))
#print(name[0])
#print(name[3])

#s = [1,2,3]
#print(s)
#s.append(4) #adds 4 to the end of the list, original list is mutable
#print(s)

#draw a square
"""
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
"""

#def draw_square(size):
#    for i in range(size):
#        #print('🧱🧱🧱🧱')
#        for j in range(size):
#            print('🧱', end='')
#        print()  # Move to the next line after each row

#draw_square(4)

#draw a triangle
"""
🧱              1   =0+1
🧱🧱            2   =1+1
🧱🧱🧱          3   =2+1
🧱🧱🧱🧱        4   =3+1

in row i, how many bricks are there? i + 1
"""

#def draw_triangle(rows):
#    for i in range(rows):
#        print('🧱' * (i+1))

#draw_triangle(4)

#draw a right-aligned triangle

    #    4 spaces + 1 # = 5      5-0-1=4
   ##    3 spaces + 2 # = 5      5-1-1=3
  ###    2 spaces + 3 # = 5      5-2-1=2
 ####    1 space + 4 # = 5       5-3-1=1
#####

#for i in range(size):
#    in row i, how many spaces are there? size - i - 1



#def right_triangle(size):
#    for i in range(size):
#        print(' '*(size-i-1)+'#'* (i+1))

#right_triangle(4)

#create a function to drae a pyramid

   #        3 spaces + 1 # = 4     4-0+1=5
  ###       2 spaces + 3 # = 5     5-1+2=6
 #####      1 space + 5 #  = 6     6-1+2=7
#######

#for i in range(size):
#   in row i, how many spaces are there? size - i + 1
#   in row i, how many #s are there? i + 2


def center_triangle(size):
    for i in range(size):
        print(' '*(size-i-1)+'#'*(i*2+1))

center_triangle(4)