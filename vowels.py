def count_vowels(s):
    count=0
    vowels=('a','e','i','o','u')
    s=s.lower()
    for i in s:
        if i in vowels:
            count+=1
    return count

str=input("Please write a word: ")
print("there are",count_vowels(str), "vowels in your word.")