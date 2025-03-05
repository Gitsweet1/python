def reverse_str(s):
    rev=""
    for i in range(len(s)-1,-1,-1):
        rev+=s[i]
    return rev

str=input("Write a string and i will reverse it: ")
print(reverse_str(str))