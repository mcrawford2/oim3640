#1

#if score >= 60:
#    print("Pass")
#elif score >= 90:
#    print("A")
#else:
#    print("Fail")

#score = 95, but will print "Pass" instead of "A" because the condition for "Pass" is checked first
#to fix this, we should check for the highest score first:

#if score >= 90:
#    print("A")
#elif score >= 60:
#    print("Pass")
#else:
#    print("Fail")

#score = 95, will now print "A" because the condition for "A" is checked first
#if you get rid of the "elif" and just use "if" statements, it will check all conditions and print both "A" and "Pass" for a score of 95, which is not what we want.

#function
#def evaluate_score(score):
#    if score >= 90:
#        return("A")
#    elif score >= 60:
#        return("Pass")
#    else:
#        return("Fail")
    
#score = int(input("Enter your score: ")) 
#result = evaluate_score(score)
#print(result)

#score = 95, will print "A" because the function returns "A" for scores >= 90
#two ifs and prints, will print both. two ifs and return, will only return first. 

#2

#def mystery(x):
#    if x > 0:
#        return "Positive"
#    print("done")

#result = mystery(5)
#print(result)

#will print "Positive" and then "done" because the function returns "Positive" for x > 0, but it also prints "done" after the return statement, which is executed regardless of the return value

#3

#x = 15
#y = x > 10 and x < 20
#print(type(y))
#print(y)

#will print
#<class 'bool'>
#True

#def is_leap_year(year):
#    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#        return True
#    return False

#print(is_leap_year(2026))
#print(is_leap_year(2027))

#5

#def check(n):
#    if n % 2 == 0:
#        if n % 3 == 0:
#            print ("A")
#        else:
#            print ("B")
#    else:
#        print ("C")

#check(8) #prints B

#check(6) #prints A

#nested conditional, change to using elif to simplify

def check(n):
    if n % 2 == 0 and n % 3 == 0:
        print ("A")
    elif n % 2 == 0:
        print ("B")
    else:
        print ("C")






