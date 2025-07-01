# Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters, 
# and that you are given the "true" length of the string.

# O(n) time and O(n) space solution using a string method
def urlify(s: str) -> str:
    return s.replace(" ", "%20")

print(urlify("Mr John Smith    "))


# O(n) time and O(1) space solution using a character count array assuming ASCII (256 chars)
# Input: a character array with extra space at the end and an integer true_length representing the actual content length.
# Task: Replace all spaces ' ' with '%20' in-place.
# Constraint: Do not use .replace() or create a new string.

def urlify_2(char_array: list, true_length: int) -> None:
    # Count spaces, O(n) time
    space_count = 0
    for i in range(true_length):
        if char_array[i] == ' ':
            space_count += 1

    # When replacing ' ' with '%20', the string grows by 2 characters per space (1 → 3 characters).
    # New end index after replacements
    index = true_length + space_count * 2

    # Fill the array backwards, O(n) time
    for i in range(true_length - 1, -1, -1):
        if char_array[i] == ' ':
            char_array[index - 3:index] = ['%', '2', '0']
            index -= 3
        else:
            char_array[index - 1] = char_array[i]
            index -= 1


s = list("Mr John Smith    ")  # 4 extra spaces
urlify_2(s, 13)
print("".join(s))  # Output: "Mr%20John%20Smith"


# NOTES

# COMPLEXITY ANALYSIS:

# Solution 1: urlify() function
# Time Complexity: O(n)
#   - str.replace() method scans through the entire string to find and replace all spaces
#   - n is the length of the input string
# Space Complexity: O(n)
#   - Creates a new string with replacements
#   - New string can be up to 3x longer than original (if every char is a space)
#   - Uses O(n) additional space

# Solution 2: urlify_2() function
# Time Complexity: O(n)
#   - First loop (counting spaces): O(n) where n is true_length
#   - Second loop (filling array backwards): O(n) where n is true_length
#   - Total: O(n) + O(n) = O(n)
# Space Complexity: O(1)
#   - Modifies input array in-place
#   - Only uses constant additional space for variables (space_count, index, i)
#   - No new data structures created that grow with input size

# COMPARISON:
# Both solutions have O(n) time complexity, but differ in space efficiency:
# - Solution 1: O(n) space - creates new string
# - Solution 2: O(1) space - modifies array in-place
# Solution 2 is preferred when memory usage is a concern or when working with
# character arrays that need to be modified in-place.
