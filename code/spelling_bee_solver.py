def uses_only(word, allowed):
    """Returns True if all letters in word are in allowed"""
    for letter in word:
        if letter not in allowed:
            return False
    return True

# print(uses_only('cake', 'kcboela'))
# print(uses_only('babson', 'kcboela'))

def must_use (word, required):
    """Returns True if word uses the required letter"""
    for letter in word:
        if letter == required:
            return True
    return False

# print(must_use('cake', 'a'))
# print(must_use('clock', 'a'))

def is_valid(word, required, allowed):
    """Returns True if word is valid for the Spelling Bee puzzle"""
    return uses_only(word, allowed) and must_use(word, required) and len(word) >= 4

# print(is_valid('cake', 'a', 'kcboela'))
# print(is_valid('bake', 'a', 'kcboela'))
# print(is_valid('clock', 'a', 'kcboela'))
# print(is_valid('babson', 'a', 'kcboela'))

def find_words(required, allowed):
    """Prints all words that are valid for the Spelling Bee puzzle"""
    wordlist = open('data/words.txt')
    count = 0
    for line in wordlist:
        word = line.strip()
        if is_valid(word, required, allowed):
            print(word)
            count += 1
    print('Total possible words:', count)

def main():
    find_words('a', 'kcboela')

if __name__ == '__main__':    main()


