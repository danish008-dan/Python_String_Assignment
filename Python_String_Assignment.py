# 1. Create a string made of the first, middle and last character
'''
WAP to create a new string made of an input string's first, middle, and last character
GIVEN - "Dnish"
OUTPUT - Dih
'''

# Solution

# Given String
s = "Dnish"

# Find first, middle, and last characters
first_char = s[0]
middle_char = s[len(s) // 2]
last_char = s[-1]

# Create new string
new_string = first_char + middle_char + last_char

print(new_string)

# 2. Create a String made of the middle three characters
'''
case 1 - input - str1 = "jhonDipPeta",  Output = Dip
case 2 - input - str2 = "jaSonAy",      output = Son
'''

# Solution

# Case 1
str1 = "jhonDipPeta"
mid1 = len(str1) // 2
result1 = str1[mid1 - 1 : mid1 + 2]
print(result1)

# Case 2
str2 = "jaSonAy"
mid2 = len(str2) // 2
result2 = str2[mid2 - 1 : mid2 + 2]
print(result2)

# 3. Append new string in the middle of a given string
'''
Given two strings, s1 and s2. WAP to create a new string s3 by appending s2 in the middle of s1.

s1 = "Ault"  length = 4 (middle index = 4 // 2 = 2)
s2 = 'Kelly'

output = AuKellylt

Logic - 

1. Find the middle index of s1
2. split s1 into two parts:
    a. from start to middle
    b. from middle to end 
3. insert s2 between them     
'''

# Solution
def append_middle(s1, s2):
    mid = len(s1) // 2
    return s1[:mid] + s2 + s1[mid:]   # String Slicing

print(append_middle("Ault", "Kelly"))

# 4. Create a new string made of the first, middle, and last characters of each input string
'''
Given two strings, s1 and s2. WAP to return a new string made of s1 and s2's first,middle, and last characters.

s1 = 'America'
s2 = 'Japan'

output = Ajrpan
'''

# Solution
def mix_strings(s1, s2):
    return (
        s1[0] + s2[0] +
        s1[len(s1)//2] + s2[len(s2)//2] +
        s1[-1] + s2[-1]
    )

print(mix_strings("America", "Japan"))

# 5. Arrange string characters such that lowercase letters should come first
'''
Given string contain a combination of the lower and upper case letters.
WAP to arrange the characters of a string so that all lowercse letters should come first

GIVEN - str1 = PyNaTive
output - yaivePNT
'''

# Solution
# 1.
def arrange_string(s):
    return "".join(c for c in s if c.islower()) + "".join(c for c in s if c.isupper())

print(arrange_string("PyNaTive"))


# 6. Count all letters, digit, and symbols from a given string
'''
Given -
str1 = 'P@#yn26at^&i5ve'

output -  chars = 8, digits = 3, symbols = 4 

Logic - 
1. For each character in the string:
    a. If isalpha() -> letter
    b. If isdigit() -> digit
    c. Else -> symbol
'''

# Solution
def count_chars_digits_symbols(s):
    chars = digits = symbols = 0
    for ch in s:
        if ch.isalpha():
            chars += 1
        elif ch.isdigit():
            digits += 1
        else:
            symbols += 1
    return chars, digits, symbols

c, d, s = count_chars_digits_symbols("P@#yn26at^&i5ve")
print(f"chars = {c}, digits = {d}, symbols = {s}")


# 7. Create a mixed String using the following rules
'''
Given two strings, s1 and s2. WAP to create a new string s3 made of the first char of s1.
Then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
Any leftover chars go at the end of the result

Given -
s1 = 'ABC' s2 = 'Xyz'
output - AzbycX

Logic - 
1. Traverse s1 from start
2. Traverse s2 from end
3. Add characters alternately
4.Append leftover characters if lengths differ
'''

# Solution
def mix_string(s1, s2):
    result = ""              # This will store the final mixed string

    s2 = s2[::-1]            # Reverse the second string (so we can take chars from the end)

    # Loop runs till the length of the shorter string
    for i in range(min(len(s1), len(s2))):
        result += s1[i]      # Add i-th character from s1 (from start)
        result += s2[i]      # Add i-th character from reversed s2 (from end)

    # Add remaining characters if any string is longer
    result += s1[len(s2):]  # Append leftover characters of s1
    result += s2[len(s1):]  # Append leftover characters of s2

    return result            # Return the final mixed string

print(mix_string("ABC", "Xyz"))  # Call the function and print the result


# 8. Sring characters balance test
'''
EX - s1 and s2 are balanced if all characters iin the s1 are present in s2.
the character's position doesn't matter.

Given -
case1: s1 = 'Yn', s2 = 'PYnative'
output - True

case2: s1 = 'Ynf', s2 = 'PYnative'
output - False
'''

# Solution
def is_balanced(s1, s2):
    for ch in s1:            # Check each character in s1
        if ch not in s2:     # If character is not present in s2
            return False     # Strings are NOT balanced
    return True              # All characters found, strings are balanced


# Test cases
print(is_balanced("Yn", "PYnative"))
print(is_balanced("Ynf", "PYnative"))


# 9. Find all occurrences of a substring in a given string by ignoring the case
'''
WAP to find all occurrences of 'USA' in a given string ignoring the case.

Given - str1 = 'Welcome to USA. usa awesome, isn't it ?'
output - The USA count is: 2
'''

# Solution
def count_usa(s):
    return s.lower().count("usa")

print("The USA count is:", count_usa("Welcome to USA. usa awesome, isn't it ?"))



# 10. Calculate the sum and average of the digits present in a string
'''
str1 = 'PYnative29@#8496'
output - sum is: 38 average is: 6.33

Logic - 
1. Traverse each character in the string
2. If the character is a digit:
      a. Convert it to integer
      b. Add it to sum
      c. Increase digit count
3. Average = sum / count
4. Round the average to 2 decimal places
'''

# Solution

# 1.
str1 = "PYnative29@#8496"

total = 0
count = 0

for ch in str1:
    if ch.isdigit():          # Check if character is a digit
        total += int(ch)      # Add digit value to total
        count += 1            # Increase digit count

average = total / count       # Calculate average

print(f"sum is: {total} average is: {average:.2f}")

# 3. Function
def sum_and_average(s):
    total = count = 0
    for ch in s:
        if ch.isdigit():
            total += int(ch)
            count += 1
    return total, total / count

s, avg = sum_and_average("PYnative29@#8496")
print(f"sum is: {s} average is: {avg:.2f}")


# 3. Advanced (list comprehension)
digits = [int(ch) for ch in str1 if ch.isdigit()]
print(f"sum is: {sum(digits)} average is: {sum(digits)/len(digits):.2f}")

# 11. WAP to count occurences of all characters within a string
'''
Given - str1 = 'Apple'
output - {'A': 1, 'P': 2, 'l': 1, 'e': 1}

Logic - 
1. Create an empty dictionary
2. Traverse each character in the string
3. If character already exists in dictionary → increase count
4. Else -> add character with count 1

hint- use dictionary get function 
'''

# Solution
def count_characters(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    return count

print(count_characters("Apple"))

# 12. Reverse a given string
'''
Given - str1 = 'Danish Khatri'
'''

# Solution
str1 = "Danish Khatri"
reversed_str = str1[::-1]   # Reverse the string using slicing
print(reversed_str)

# using function
def reverse_string(s):
    return s[::-1]
print(reverse_string("Danish Khatri"))


# 13. Find the last position of a given substring
'''
WAP to find the last position of a substring 'Danish' in a given string 
Given - str1 = 'Danish is a Machine Learning scientist who knows Python. Danish works at google. Danish is a good person'

Hint - use find () function 
'''

# Solution
position = str1.lower().rfind("danish")
print("Last position of 'Danish' is:", position)

# 14. Split a tring on hyphens
'''
str1 = 'Danish-is-a-machine-learning-scientist'
'''

# Solution
def split_on_hyphen(s):
    return s.split("-")
print(split_on_hyphen("Danish-is-a-machine-learning-scientist"))

# 15. Remove empty strings from a list of strings
'''
given - str_list = ['Emma', 'jon', '', 'Kelly', None, 'Eric', '']
output - Original list of string ['Emma', 'jon', '', 'Kelly', None, 'Eric', ''] After removing empty strings 
['Emma', 'jon', 'Kelly', 'Eric']
'''

# Solution
result = [item for item in str_list if item]
print(result)

# using function
def remove_empty_strings(lst):
    return [item for item in lst if item]
print(remove_empty_strings(['Emma', 'jon', '', 'Kelly', None, 'Eric', '']))



# 16. Remove special symbols / punctuations from a string
'''
Given: str1 = "/*jon is @developer & musician"
output - "jon is developer musician"
'''

# Solution
def remove_special_symbols(s):
    return "".join(ch for ch in s if ch.isalpha() or ch.isspace())

print(remove_special_symbols("/*jon is @developer & musician"))


# 17. Remove all characters from a string except integers
'''
Given: str1 = 'I am 20 years and 10 months old'
output - 2010
'''

# Solution
result = "".join(ch for ch in str1 if ch.isdigit())
print(result)

# Using function
def extract_digits(s):
    return "".join(ch for ch in s if ch.isdigit())

print(extract_digits("I am 20 years and 10 months old"))


# 18. Find words with both alphabets and numbers
'''
WAP to find words with both alphabets and numbers from an input string.

given - str1 = 'Danish 20 is Machine Learning scientist50 and AI Expert'
output - scientist50
'''

# Solution
def find_alpha_numeric_words(s):
    return [
        word for word in s.split()
        if any(c.isalpha() for c in word) and any(c.isdigit() for c in word)
    ]

print(find_alpha_numeric_words("Danish 20 is Machine Learning scientist50 and AI Expert"))


# 19. Replace each special symbol with # in the following string
'''
Given - str1 = '/*jon is @developer & musician!!'
output - ##jon is #developer # musician##
'''

# Solution
result = "".join(ch if ch.isalpha() or ch.isspace() else "#" for ch in str1)
print(result)

# Using function
def replace_special_symbols(s):
    return "".join(ch if ch.isalpha() or ch.isspace() else "#" for ch in s)

print(replace_special_symbols("/*jon is @developer & musician!!"))


# 20. Given a string, perform the following operations in sequence:
'''
str1 = "PyTh0n@2025 is Aw3s0me!! Python#R0cks"

Tasks - 

1. Ignore case and check how many times the word "python" occurs
2. Remove all special symbols, but keep spaces
3. Extract all digits and calculate:
         a. sum of digits
         b. average of digits (2 decimal)
4. Find all words that contain both alphabets and numbers
5. Arrange characters so that:
         a. lowercase letters come first
         b. uppercase letters next
         c. digits at the end
6. Count occurrences of each character (final processed string


output - 
Python count: 2

String after removing special symbols:
PyTh0n2025 is Aw3s0me PythonR0cks

Digits: 0 2 0 2 5 3 0 0
Sum of digits: 12
Average of digits: 1.50

Alphanumeric words:
PyTh0n2025
Aw3s0me
R0cks

Rearranged string:
yhniswsmehtPnAPTRD202530025

Character frequency:
{'y':2, 'h':2, 'n':2, ...}
'''

# Solution

# 1. Manual Method
str1 = "PyTh0n@2025 is Aw3s0me!! Python#R0cks"

# 1. Count 'python' ignoring case
python_count = str1.lower().count("python")
print("Python count:", python_count)

# 2. Remove special symbols (keep letters, digits, spaces)
clean_str = "".join(ch for ch in str1 if ch.isalnum() or ch.isspace())
print("\nString after removing special symbols:")
print(clean_str)

# 3. Extract digits, sum and average
digits = [int(ch) for ch in clean_str if ch.isdigit()]
digit_sum = sum(digits)
digit_avg = digit_sum / len(digits)

print("\nDigits:", *digits)
print("Sum of digits:", digit_sum)
print(f"Average of digits: {digit_avg:.2f}")

# 4. Find alphanumeric words
print("\nAlphanumeric words:")
for word in clean_str.split():
    if any(c.isalpha() for c in word) and any(c.isdigit() for c in word):
        print(word)

# 5. Arrange characters
lower = "".join(c for c in clean_str if c.islower())
upper = "".join(c for c in clean_str if c.isupper())
nums = "".join(c for c in clean_str if c.isdigit())

rearranged = lower + upper + nums
print("\nRearranged string:")
print(rearranged)

# 6. Character frequency
char_count = {}
for ch in rearranged:
    char_count[ch] = char_count.get(ch, 0) + 1

print("\nCharacter frequency:")
print(char_count)


# Using Function
str1 = "PyTh0n@2025 is Aw3s0me!! Python#R0cks"

# 1️. Count 'python' ignoring case
def count_word_ignore_case(s, word):
    return s.lower().count(word.lower())

# 2️. Remove special symbols (keep letters, digits, spaces)
def remove_special_symbols(s):
    return "".join(c for c in s if c.isalnum() or c.isspace())

# 3. Extract digits, calculate sum & average
def digits_sum_avg(s):
    digits = [int(c) for c in s if c.isdigit()]
    return digits, sum(digits), sum(digits)/len(digits) if digits else 0

# 4. Find words containing both letters and digits
def alphanumeric_words(s):
    return [word for word in s.split() if any(c.isalpha() for c in word) and any(c.isdigit() for c in word)]

# 5. Rearrange characters: lowercase → uppercase → digits
def rearrange_chars(s):
    return "".join(c for c in s if c.islower()) + "".join(c for c in s if c.isupper()) + "".join(c for c in s if c.isdigit())

# 6. Count character frequency
def char_frequency(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq

# ======= Execution =======
print("Python count:", count_word_ignore_case(str1, "python"))

clean_str = remove_special_symbols(str1)
print("\nString after removing special symbols:\n", clean_str)

digits, d_sum, d_avg = digits_sum_avg(clean_str)
print("\nDigits:", *digits)
print("Sum of digits:", d_sum)
print(f"Average of digits: {d_avg:.2f}")

print("\nAlphanumeric words:")
for word in alphanumeric_words(clean_str):
    print(word)

rearranged = rearrange_chars(clean_str)
print("\nRearranged string:\n", rearranged)

print("\nCharacter frequency:\n", char_frequency(rearranged))

# ============== COMPLETE =============================== 