#EX1
pow=dict()
for i in range(1,6):
    pow[i]=i*i

print("EX1:\r\n",pow.items())

#EX2
def list_dict(l1):
    print("EX2:\r\n",l1.keys())
list_dict(pow)

#EX3
def merge_dict(d1,d2):
    for i,j in d2.items():
        d1[i]=j
    return d1
dict1={1:1,2:2,3:3}
dict2={'a':'a','b':'b','c':'c'}
print("EX3:\n",merge_dict(dict1,dict2))

#EX4
def best_student(d1):
    # Find the student with the highest grade
    max_grade_student = max(d1, key=d1.get)
    return max_grade_student, d1[max_grade_student]

students = {'Alis': 80, 'Max': 79, 'Dovi': 99, 'Lili': 94}
name, grade = best_student(students)
#print(max(students, key=students.get))
print("EX4:\nThe student with the highest grade is:", name, "with a grade of", grade)
'''
def best_student(d1):
    return (max(d1.values()))
students={'Alis':80,'Max':79,'Dovi':99,'Lili':94}
print("EX4:\nThe student with highest grade is:",(best_student(students)))
print(students.get('Alis'))
'''

#EX5
def most_frequent_char(s):
    str1={}
    for i in s:
        if i in str1:
            str1[i] += 1
        else:
            str1[i]=1
    max_key = max(str1, key=str1.get)
    #max_value = str1[max_key]
    return (max_key, str1[max_key])

str="hello"
#str=input("Please enter a word or a sentence: ")
print("EX5:\nThe most frequent char is:",most_frequent_char(str))