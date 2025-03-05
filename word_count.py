def word_count(sentence):
    counter={}
    words=sentence.split()
    print(words)
    for i in words:
        print(i)
        if i in counter:
            counter[i] += 1
        else:
            counter[i]=1
    return counter
str="the brown fox is differ from the fox store"
#str=input("Please write a sentence and I will count the words: ")
print("The counter is:",word_count(str))