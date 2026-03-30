# Quiz 3 
- Topics: lists, tuples, dicts, sets, mutability, counting pattern 

# Lists 
mutable sequences 
Examples of lists: 
stocks = ['AAPL', 'GOOG', 'MSFT', 'AMZN'] 
prices = [182.30, 141.80, 415.20, 178.50] 
mixed = ['AAPL', 182.30, True]    # can mix types 
empty = [] 
Access elements the same way as strings: 
stocks[0]          # 'AAPL' 
stocks[-1]         # 'AMZN' 
len(stocks)        # 4 
'GOOG' in stocks   # True 
Unlike strings, you can change a list in place: 
stocks = ['AAPL', 'GOOG', 'MSFT', 'AMZN'] 
stocks[2] = 'META'    # replace MSFT with META 
stocks   # ['AAPL', 'GOOG', 'META', 'AMZN']
Compare with strings (immutable): 
ticker = 'MSFT' 
ticker[0] = 'X'   # TypeError! Strings are immutable. 
List Slices, same syntax as string slices: 
stocks = ['AAPL', 'GOOG', 'META', 'AMZN'] 
stocks[1:3]    # ['GOOG', 'META'] 
stocks[:2]     # ['AAPL', 'GOOG'] 
stocks[2:]     # ['META', 'AMZN'] 
stocks[:]      # ['AAPL', 'GOOG', 'META', 'AMZN'] (copy!) 
A slice returns a new list (not an alias). 

# List Methods 
stocks = ['AAPL', 'GOOG', 'META'] 
stocks.append('TSLA')           # ['AAPL', 'GOOG', 'META', 'TSLA'] 
stocks.extend(['NVDA', 'AMZN']) # [..., 'TSLA', 'NVDA', 'AMZN'] 
stocks.pop()                    # returns 'AMZN' (removes last) 
stocks.remove('META')           # removes first 'META' 
Important: most list methods modify in place and return None! 
result = stocks.append('NFLX') 
print(result)   # None  (common trap!) 

# Lists and strings (split, join) 
Convert between lists and strings: 
list('AAPL')                          # ['A', 'A', 'P', 'L'] 
'AAPL,GOOG,META,AMZN'.split(',')     # ['AAPL', 'GOOG', 'META', 'AMZN']  
','.join(['AAPL', 'GOOG', 'META'])   # 'AAPL,GOOG,META' 
split() and join() are inverses of each other. 

# Sorting 
sorted() returns a new sorted list (original unchanged): 
stocks = ['GOOG', 'AAPL', 'META'] 
sorted(stocks)    # ['AAPL', 'GOOG', 'META'] 
stocks            # ['GOOG', 'AAPL', 'META']  (unchanged!) 
Useful trick with strings: 
''.join(sorted('listen'))   # 'eilnst' 
''.join(sorted('silent'))   # 'eilnst'  — same! They're anagrams. 

# Aliasing (important!) 
Two variables can refer to the same list: 
a = [1, 2, 3] 
b = a          # b is NOT a copy — it's the SAME list! 
b[0] = 99 
print(a)       # [99, 2, 3]  — a changed too! 
To make a copy:
b = a[:]       # slice copy 
b = list(a)    # list() copy 
This is a common source of bugs. Be careful when passing lists to functions! 

# The Accumulator Pattern with Lists 
Build up a list inside a loop: 
palindromes = [] 
for word in word_list: 
if word == word[::-1]:    # reverse the word 
palindromes.append(word) 

# Dictionaries 
Dictionaries as key-value mappings 
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'} 
Access values by key (not by index): 
eng2sp['two']        # 'dos' 
eng2sp['four']       # KeyError! 
'two' in eng2sp      # True (checks keys, not values) 
len(eng2sp)          # 3 
Keys must be immutable (strings, numbers, tuples). Values can be anything. 
Creating, accessing, and modifying dicts 
Start empty, add entries 
prices = {} prices['AAPL'] = 178.50 prices['GOOG'] = 141.80 prices['MSFT'] = 415.20 
Update an existing key 
prices['AAPL'] = 182.30 
Delete a key 
del prices['GOOG'] 
print(prices) # {'AAPL': 182.30, 'MSFT': 415.20} 
Looping over dictionaries 
prices = {'AAPL': 182.30, 'MSFT': 415.20, 'GOOG': 141.80} 
for key in prices:                # loop over keys 
print(key, prices[key]) 
for value in prices.values():     # loop over values 
print(value) 
for key, value in prices.items(): # loop over both 
print(f'{key}: ${value}') 

# The counting pattern (histogram) 
Count how many times each item appears: 
def histogram(s): 
    d = {} 
    for c in s: 
        if c not in d: 
            d[c] = 1 
        else: 
            d[c] += 1 
    return d 
histogram('brontosaurus') → {'b': 1, 'r': 2, 'o': 2, ...} 

# Common dict methods 
d = {'a': 1, 'b': 2, 'c': 3} 
d.get('a', 0)     # 1 (key exists) 
d.get('z', 0)     # 0 (key missing, returns default) 
list(d.keys())     # ['a', 'b', 'c'] 
list(d.values())   # [1, 2, 3] 
list(d.items())    # [('a', 1), ('b', 2), ('c', 3)] 
get() avoids KeyError - very useful in the counting pattern: 
d[c] = d.get(c, 0) + 1    # shorter version of if/else counting 

# Tuples 
Tuples as immutable sequences 
t = ('a', 'b', 'c', 'd') 
t[0]       # 'a' 
t[1:3]     # ('b', 'c') 
len(t)     # 4 
But you cannot modify them:  
t[0] = 'X'   # TypeError! Tuples are immutable. 
Like strings, unlike lists. 
Tuple assignment and unpacking 

# Swap two variables without a temp 
a, b = b, a 

# Unpack a tuple into variables 
point = (3, 4
x, y = point    # x = 3, y = 4 
Works great with dict.items(): 
for key, value in prices.items(): 
    print(f'{key}: ${value}') 

Returning Multiple Values 
Tuples let functions return more than one value: 
def min_max(numbers): 
    return min(numbers), max(numbers) 
lowest, highest = min_max([3, 1, 4, 1, 5]) 
# lowest = 1, highest = 5 
The return creates a tuple; unpacking assigns both at once. 
Tuples as dictionary keys 
You want to track prices by ticker and date: 
# Try a list key? 
prices = {['AAPL', '2026-03-24']: 229}  # TypeError! 
# String key? Works, but messy... 
prices = {'AAPL(2026-03-24)': 229} 
# Tuple key ✓ clean and natural! 
prices = {('AAPL', '2026-03-24'): 229} 
zip() for combining sequences 
names = ['AAPL', 'GOOG', 'MSFT'] 
prices = [182.30, 141.80, 415.20] 
for name, price in zip(names, prices): 
    print(f'{name}: ${price}') 
Create a dict from two lists: 
stock_prices = dict(zip(names, prices)) 
# {'AAPL': 182.30, 'GOOG': 141.80, 'MSFT': 415.20} 

# Sets: Unique Collections 
A set holds unique items only, unordered: 
fruits = {'apple', 'banana', 'apple', 'cherry'} 
print(fruits)   # {'apple', 'banana', 'cherry'} 
len(fruits)     # 3 
Useful for removing duplicates:  
nums = [1, 2, 2, 3, 3, 3] 
unique = set(nums)       # {1, 2, 3} 
len(set(nums))           # 3 unique values 
Set Operations 
a = {1, 2, 3, 4} 
b = {3, 4, 5, 6} 
a & b    # {3, 4}       intersection 
a | b    # {1, 2, 3, 4, 5, 6}  union 
a - b    # {1, 2}       difference 
Check membership (very fast!): 
3 in a   # True 
Sets are great when you need fast lookup or uniqueness. 
Good for speed! 
Choosing Data Structures 
Type	Mutable?	Ordered?	Access by	Duplicates? 
str	No		Yes		index		Yes 
list	Yes		Yes		index		Yes 
tuple	No		Yes		index		Yes 
dict	Yes		Yes*		key		Keys: No 
set	Yes		No		membership	No 

# When to Use What? 
list: ordered collection, may have duplicates 
Student grades, stock ticker history 
tuple: fixed data that shouldn't change 
GPS coordinates, function returning multiple values
dict: look up values by a meaningful key 
Stock prices by ticker, word frequency counts 
set: unique items, fast membership testing 
Unique words in a document, valid usernames 

# Review Questions 
# S12 Checks 

Q1: git commit saves changes locally. git push uploads commits to the remote (GitHub). 

Q2: What happens when you call has_vowel('python')? 
def has_vowel(s): 
    i = 0 
    while i < len(s): 
        if s[i] in 'aeiou': 
            i += 1 
            return True 
    return False 

True 

Q3: has_digit 
def has_digit(s): 
    for c in s: 
        if c.isdigit(): 
            return True 
        else: 
            return False 
print(has_digit('iPhone15'))   # ?		False 
print(has_digit('4ever'))      # ?		True 
print(has_digit('hello'))      # ?		False 

Q4: has_lower 
def has_lower(s): 
    for c in s: 
        if 'c'.islower(): 
            return True 
        else: 
            return False 
print(has_lower('NASA'))     # ?		False 
print(has_lower('Python'))   # ?		False 
print(has_lower('copilot'))      # ?		True 

Q5: check_vowel 
def check_vowel(s): 
    for c in s: 
        result = (c in 'aeiou') 
    return result 
print(check_vowel('orange'))   # ?		e 
print(check_vowel('lemon'))    # ?		o 
print(check_vowel('kiwi'))     # ?		i 
What does this function actually check? 

Checks for the last vowel in the given word 

Q6: any_vowel 
def any_vowel(s): 
    flag = False 
    for c in s: 
        flag = flag or (c in 'aeiou') 
    return flag 
print(any_vowel('rhythm'))   # ?		False		 
print(any_vowel('cafe'))     # ?		e 
print(any_vowel('sky'))      # ?			False 

Q7: all_alpha 
def all_alpha(s): 
    flag = True 
    for c in s: 
        flag = flag and c.isalpha() 
    return flag 
print(all_alpha('Babson'))    # ?		False (turn with lower) 
print(all_alpha('OIM3640'))   # ?		False (turns with numbers) 
print(all_alpha('hello!'))    # ?		False (always) 

Q8: has_space 
def has_space(s): 
    for c in s: 
        if c == ' ': 
            break 
            return True 
    return False 
print(has_space('ice cream'))   # ?		False (would be true if no break) 
print(has_space(' hello'))      # ?		False 
print(has_space('pizza'))       # ?		False 

Q9: all_digit 
def all_digit(s): 
    for c in s: 
        if not c.isdigit(): 
            return False 
    return True 
print(all_digit('911'))      # ?		True 
print(all_digit('3.14'))     # ?		False 
print(all_digit('OIM3640'))  # ?	False 
Is this function correct? How does it work? 

It checks if there is any character in the string that is not a digit.  


TRUE AND FALSE = FALSE 
TRUE OR FALSE = TRUE 

S13 Strings 
stocks = 'AAPL,MSFT,GOOG,AMZN' 

Q1: What is stocks[0]? stocks[-1]?		stocks[0] = AAPL, stocks[-1] = AMZN XXXXXXX indexing a string means stocks[0] = A and stocks[-1] = N 
Q2: How do you make it become 'AAPL,MSFT,GOOG,AMZN,TSLA'?	stocks.append(‘TSLA’) XXXXXXXX strings use concatenation: stocks += ‘, TSLA’ 
Q3: What is 'GOOG' in stocks? 'AA' in stocks?		True and True, both appear 
Q4: What is stocks.lower()?		‘aapl, msft, goog, amzn’ 
Q5: What is stocks.find('MSFT')?		True XXXXXXXX find returns integer position, so stocks.find(‘MSFT’)= 5 because M is in the 5th position 
Q6: Sort stocks in reverse?			(how) = sorted(stocks.split(','), reverse=True) 
Q7: What is stocks.strip('A')?		‘APL, MSFT, GOOG, AMZN’ (removes leading and trailing A’s. 

Loop Patterns 
Q8: What does this print? 
 def count_vowels(s): 
    count = 0 
    for c in s: 
        if c in 'aeiou': 
            count += 1 
            return count 
    return count 
print(count_vowels('apple'))			2XXXXXXX returns 1 immediately after a in apple 
print(count_vowels('sky'))			0 
 
S14 Strings vs Lists 
Q1: What common operations work on both strings and lists?		indexing([0]), slicing ([1:3]), operations (+ and *), len, in 
Q2: Are strings mutable? Are lists mutable?	Strings are immutable, lists are mutable (changeability without creating new) 
Q3: How do you add to the end of a string? To the end of a list?		String: string += ‘new’, list= list.append(new) 
Q4: How do you sort a list in-place? (sort() or sorted()?)		.sort() sorts in-place (modifies the original list). sorted() returns a new sorted list and leaves the original unchanged.
Q5: How do you make a copy of a string? A copy of a list?		String: just assign it — b = a is fine since strings are immutable, aliasing is safe. 
List: use b = a[:] or b = a.copy() to make a true copy. 

Copying vs Aliasing 
Q6: What does this print?  
a = [1, 2, 3] 
b = a 
b.append(4) 
print(a)		1,2,3,4 
print(a is b)		True, b is a (aliased) 

Q7: What about this? 
a = [1, 2, 3] 
b = a[:] 
b.append(4) 
print(a)		1,2,3 
print(a is b)		False, a is not b (copied) 

Split  
Q8: What does each produce? 
'a  b  c'.split()       # ?		‘a’ ‘b’ ‘c’ 
'a  b  c'.split(' ')    # ?		‘a’ ‘ ‘ ‘b’ ‘ ‘‘c’ 
split() treats consecutive whitespace as one separator		 
split(' ') splits on each single space (empty strings!) 
When reading a file, why is line.strip() important?		makes the file easier to read and maintain by removing extra white spaces 
More importantly it removes the newline character (\n) at the end of each line when reading a file, which is critical for clean processing 

S15 Dictionaries 
prices = {'AAPL': 260.81, 'NVDA': 186.00, 'MSFT': 404.88, 'GOOG': 308.42} 
Q1: How do you get the price of 'AAPL'? 		prices['AAPL'] → 260.81 or prices.get('AAPL') → 260.81 
Q2: What happens if you do prices['TSLA']?		error, no TSLA 
Q3: How would you find the stock with the highest price?		? 
Q4: How would you get a list of all stocks priced above $200?		? 
Q5: If all prices go up 10%, how do you update all values?		prices[ticker] *= 1.10 

Q6: When to Use What? (list, tuple, dictionary, set) 
Student grades, stock ticker history			list 
GPS coordinates, function returning multiple values	tuple 
Stock prices by ticker, word frequency counts		dictionary 
Unique words in a document, valid usernames		set 

S16  
info = yf.Ticker('AAPL').info 
# 'shortName', 'city', 'longBusinessSummary', 
# 'sector', 'fullTimeEmployees', ... 
Q1: What does info['longBusinessSummary'].split() give you?		list of only longBusinessSummary names 
Q2: What does 'iPhone' in info['longBusinessSummary'] return?	True or False, depending on if it is there 
Q3: Can you do info['city'][0] = 'c'? Why not?	immutability 
Q4: What does len(info) tell you?			the length of entries in the list XXXXXX len(info) gives the number of keys in the dictionary, not a list 
tickers = ['AAPL', 'NVDA', 'MSFT'] 
prices = {} 
for t in tickers: 
    prices[t] = yf.Ticker(t).info['currentPrice'] 
Q5: What does sorted(tickers) return? Does it change tickers?		alphabetically organized AAPL, NVDA, MSFT XXXXXXX sorted(tickers) returns ['AAPL', 'MSFT', 'NVDA'] (alphabetical), and it does not change tickers — it returns a new list. Also NVDA comes after MSFT alphabetically. 
Q6: How do you get the total value of all 3 stocks?		sum(prices.values()) 
Q7: What does 'TSLA' in prices return?				False 
Q8: How would you add 'GOOG' to both tickers and prices?	Tickers += ‘GOOG’ XXXXXXX tickers.append('GOOG') 
prices['GOOG'] = yf.Ticker('GOOG').info['currentPrice'] 

Q9: Which Data Structure? 
You're building a music app: 
Your favorites playlist (add, remove, reorder)			list 
All artists a user has ever listened to (no repeats)			set 
Song title → number of times played				dictionary 
A single song record: ('Bohemian Rhapsody', 'Queen', 1975)	tuple 