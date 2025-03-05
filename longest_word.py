def longest_word(sentence):
    splits=sentence.split()
    long=""
    for i in splits:
        if i>long:
            long=i
    return long

str=input("Write a string and i will find the longest word: ")
print("The longest word in your sentense is:",longest_word(str))