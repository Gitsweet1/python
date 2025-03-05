str="abcdeab"
str1=""
for i in str:
    if i in str1:
        continue
    else:
        str1+=i
print(str1)