#Scope: code reading, loops, return patterns, predict output

# CLASS REVIEW QUESTIONS

#count = 0
#for letter in 'mississippi':
#    if letter == 's':
#        count += 1
#print(count)
#1. What is the output?   4
#2. What keywords can exit a loop early? Skip to the next iteration?    to exit: break, to skip: continue

#n = 6
#while n > 0:
#    print(n)
#    n = n - 2


#3. What will be the last line of output?   2
#4. What if line 2 is changed to while n >= 0:?   0
#5. What about while n != 0:?   2
#6. What about:     negative infinity, because it skips over 0
#below bevause infinite loop
#n = 5
#while n != 0:
#    print(n)
#    n = n - 2

#def uses_any(word, letters):
#    for letter in word:
#        if letter in letters:
#            return True
#        return False
#uses_any('hello', 'aeiou')
#7. What does this function return for uses_any('hello', 'xyz')?    False
#8. What would uses_any('hello', 'aeiou') return?   True
#9. What if return False was inside the else branch of the if?    returns False immediatly, because the first letter is not a vowel, so it doesn't check the rest of the letters
    # h -> no, e ->yes, checks for all 'letters' at once but only one letter from 'word' at a time

#def version_a(word):
#    for letter in word:
#        if letter in 'aeiou':
#            print(letter)
#    print('Done')

# def version_b(word):
#     for letter in word:
#         if letter in 'aeiou':
#             return letter
#     return'None found'
# version_b('hello')

#10. What does each function do differently?
    #version a: will print the letters found in both 'aeiou' and 'word', then will print Done
    #version b: will return the letter found in both 'aeiou' and 'word' back into the function, and keep moving down the rest of the letters in the word. At the end of all the letters in 'word', it will return None found (silently)
#11. What happens when you call version_a('hello')? What about version_b('hello')?
    #version a: e, o, Done
    #version b: will return the values e, o, None found, but silently because it is not printed

#12 for or while? Which loop type is better for each task?
    #a. Print each character in a string    for
    #b. Keep rolling a die until you get a 6    while
    #c. Count the vowels in a word  for
    #d. Ask the user for input until they type "done"   while



# AI GENERATED QUESTIONS

# count = 0
# for char in 'bandana':
#     if char == 'a':
#         count += 1
# print(count)
# #1. What is the output?     3
# #2. What would the output be if 'banana' were replaced with 'bandana'?    still 3

# x = 10
# while x >= 0:
#     print(x)
#     x = x - 3
# #3. What is the last number printed?    1
# #4. What happens if the condition is changed to while x >= 0:?     still 1

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)
# #5. What is the output?     0, 1, 2, 3 XXXXXXXX answer: 0, 1, 2 , 4 because when i = 3, it skips the print statement and moves on to the next iteration of the loop, which is i = 4, so it prints 4 and then the loop ends because it has gone through all the numbers in range(5)
# #6. What would change if break were replaced with continue?     0, 1, 2, 3, 4

# n = 4
# while n != 1:
#     print(n)
#     n = n - 1
# #7. Does this loop terminate? Why or why not?   yes, when n = 2 because then n = 2-1, n=1, and 1 !=1
# #8. What is the last value printed?     2

# n = 5
# while n > 0:
#     print(n)
#     n = n + 1
#     if n > 10:
#         break
# #9. What happens when this code runs?   infinite loop of n+1 forever
# #10. How could you fix it so it stops?  add a break if n =  a certain increasing number

# def count_e(word):
#     count = 0
#     for letter in word:
#         if letter == 'e':
#             count += 1
#     return count

# count_e('cheese')
# print(count_e('cheese'))
# #11. What does this function return?    3
# #12. What would be printed if we added print(count_e('cheese'))?    3

# def find_letter(word, target):
#     for letter in word:
#         if letter == target:
#             print(True)
#             return True
#     print(False)
#     return False

# find_letter('apple', 'z')
# #13. What does find_letter('apple', 'p') return?    false, true, true, false, false OR true, true, false XXXXX answer: true, because it finds the first p and then returns true, so it doesn't check the rest of the letters in 'apple'
# #14. What about find_letter('apple', 'z')?  false, false, false, false, false OR false XXXXX answer: false, because it checks all the letters in 'apple' and doesn't find z, so it returns false at the end


# def all_vowels(word):
#     for letter in word:
#         if letter not in 'aeiou':
#             return False
#     return True

# all_vowels('aeiou')
# #15. What does all_vowels('aeiou') return?    true
# #16. What does all_vowels('audio') return?    false, because it checks the first letter a, then u, then d, which is not a vowel, so it returns false immediately without checking the rest of the letters in 'audio'
# #17. What does all_vowels('face') return?    false

# def mystery(word):
#     for letter in word:
#         if letter == 'a':
#             return letter
#         print(letter)
#     print('Done')

# mystery('cat')
# mystery('dog')
# #18. What is printed when mystery('cat') is called?     a, done XXXXX answer: c, done because it checks the first letter c, which is not a, so it prints c and moves on to the next letter a, which is a, so it returns a and does not print done at the end of the function because return exits the function immediately
# #19. What is printed when mystery('dog') is called?     done XXXXX answer: d, o, g, done because it checks the first letter d, which is not a, so it prints d and moves on to the next letter o, which is not a, so it prints o and moves on to the next letter g, which is not a, so it prints g and then prints done at the end of the function

# #20. For or while?
# #a. Repeatedly ask a user to guess a number until they guess correctly  while
# # b. Print every number from 1 to 100   for
# # c. Scan a word to see if it contains a vowel  for
# # d. Keep subtracting 5 from a number until it becomes negative while



# AI GENERATION BASED ON THE QUESTIONS I ANSWERED INCORRECTLY

# def mystery1(word):
#     for letter in word:
#         if letter == 'e':
#             return letter
#         print(letter)
#     print('Done')

# mystery1('pen')
#Q1: What is printed to the screen?     p, done
#Q2: What value (if any) is returned?   e

# def mystery2(word):
#     for letter in word:
#         if letter == 'x':
#             return letter
#         print(letter)
#     print('Done')

# mystery2('cat')
#Q3: What is printed?   c, a, t, done
#Q4: What does the function return?     nothing

# def all_digits(text):
#     for char in text:
#         if char not in '0123456789':
#             print(False)
#             return False
#     print(True)
#     return True
    

# all_digits('1234')
# all_digits('12a4')
# #Q5: What does all_digits('1234') return?    true
# #Q6: What does all_digits('12a4') return? Why?    false because a triggers a return response

# for i in range(6):
#     if i % 2 == 0:
#         continue
#     print(i)
# # #Q7: What numbers are printed?     1, 3, 5

# def has_vowel(word):
#     for letter in word:
#         if letter in 'aeiou':
#             print(True)
#             return True
#         print(False)
#         return False

# has_vowel('cat')
# #Q8: What does this return?    true #####: answer: false because the return function is inside the for loop
# #Q9: Why does it not check every letter?    return immediately exits the function

# AI GENERATED QUESTIONS BASED ON ORIGINAL QUESTIONS, BUT HARDER

# def count_vowels(word):
#     count = 0
#     for letter in word:
#         if letter in 'aeiou':
#             count += 1
#         else:
#             return count
#     return count

# count_vowels('audio')
#Q1: What does this return?     2
#Q2: Why does it stop when it does?     return forces the function to exit immediately after a and e are counted

# n = 7
# while n > 0:
#     if n % 3 == 0:
#         n -= 1
#         continue
#     print(n)
#     n -= 2
# #Q3: What is printed?    7, 5, 2
# #Q4: Does this loop terminate? Why? it terminates when n=0, n!>0

# def mystery(word):
#     for letter in word:
#         print(letter)
#         if letter == 'o':
#             return 'found'
#     print('Done')

# mystery('hello')
# #Q5: What is printed?   h, e, l, l, 0
# #Q6: What is returned?    found, but after all the letters, and done is not printed because it's after found

# n = 5
# while n != 0:
#     print(n)
#     if n < 0:
#         break
#     n -= 2
# #Q7: What numbers are printed?    5, 3, 1, -1
# #Q8: Does the loop end naturally or by break? by break because subtracting by two makes it skip over 0

# def all_even(nums):
#     for n in nums:
#         if n % 2 != 0:
#             print(False)
#             return False
#     print(True)
#     return True

# all_even([2, 4, 6, 3, 8])
# #Q9: What is printed?   true XXXXX answer: false because print(True) and return(True) and not inside the loop, so it only prints true if all the numbers are even, but 3 is not even and returns false to immediately end the function
# #Q10: What is returned?   true XXXXX answer: false
# #Q11: Which element causes the function to stop?   return True XXXXX answer: return False at 3