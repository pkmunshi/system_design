# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.


#A string is a permutation of a palindrome if and only if at most one character has an odd count.
# Why?
# In a palindrome:
# Even-length strings → all characters appear an even number of times.
# Odd-length strings → only one character can appear an odd number of times (the center character); all others must be even.
# Approach:
# Ignore spaces and make everything lowercase.
# Count how many times each character appears.
# Check how many characters have an odd count.
# If more than one character has an odd count → not a palindrome permutation.

# O(n) time and O(1) space solution using a character count array assuming Standard ASCII (128 characters)
def is_palindrome_permutation(s: str) -> bool:
    s = s.replace(" ", "").lower()
    char_count = [0] * 128  # Assuming Standard ASCII (128 characters)

    for char in s:
        char_count[ord(char)] += 1

    odd_count = 0
    for count in char_count:
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False

    return True

is_palindrome_permutation("Tact Coa")     # True ("taco cat", "atco cta", etc.)
is_palindrome_permutation("racecar")      # True
is_palindrome_permutation("hello")        # False
is_palindrome_permutation("racescar")    # False


# Complexity Analysis

# Solution 1: is_palindrome_permutation() function
# Time Complexity: O(n)
#   - Single loop through string: O(n)
# Space Complexity: O(1)
#   - Uses constant space for the character count array

