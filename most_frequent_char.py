def most_frequent_char(s):
    str1={}
    for i in s:
        if i in str1:
            str1[i] += 1
        else:
            str1[i]=1
    max_key = max(str1, key=str1.get)
    max_value = str1[max_key]
    return (max_key, max_value)

str="hello"
#str=input("Please enter a word or a sentence: ")
print("The most frequent char is:",most_frequent_char(str))