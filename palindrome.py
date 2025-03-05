def reverse_str(s):
    rev=""
    for i in range(len(s)-1,-1,-1):
        rev+=s[i]
    return rev

def is_palindrome(s):
    if reverse_str(s) == s:
        return True
    else:
        return False

str=input("Write a string and i will find if it is palindrom: ")
print("The longest word in your sentense is:",is_palindrome(str))