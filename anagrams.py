# check if two words are anagrams
# Example:
# find_anagrams ("Hello", "check") --> False
# find_anagrams ("Below", "elbow") --> True
# complete the function. It should accept two strings and determine if they are anagrams


def find_anagrams(string1, string2):
    while len(string1) == len(string2):
        if sorted(string1) == sorted(string2):
            return True
            return False
    #[assignment] Add your code here
    return 'The strings are not anagrams '
    return True
print(find_anagrams('act', 'cat'))