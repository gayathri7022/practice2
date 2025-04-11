def is_palindrome(word):
    if word[::-1] == word:
        return True
    else:
        return False
    
is_palindrome("maam")
is_palindrome("racecar")
is_palindrome("good")