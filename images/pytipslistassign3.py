#Define a function is_palindrome() that recognizes palindromes (i.e. words that look thesame written backwards). For example, is_palindrome("radar") should return True.
from pytipslistassign2 import string_reverse
def is_palindrome(string):
    if (string_reverse(string)==string):
        return True
    else:
        return False
print(is_palindrome("radar"))