#EX6
my_tuple=()
my_list=[]
for i in range(1,20):
    if i%2==0:
        my_list.append(i)
        if len(my_list)==5:
            break
my_tuple=tuple(my_list)
#print("EX6:\nTuple is:",my_tuple,"\nThe sum of the tuple is:",sum(my_tuple))
print(f"EX6:\nTuple is:{my_tuple}\nThe sum of the tuple is:{sum(my_tuple)}")

#EX7
my_tuple=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
my_list=[]
for i in range(1,len(my_tuple)+1):
    if i%2==0:
        my_list.append(i)
my_tuple=tuple(my_list)
print("EX7:\nThe tuple include only even numbers:",my_tuple)

#EX8:
def reverse_str(s):
    #print(my_tuple)
    rev=list()
    for i in range(len(s)-1,-1,-1):
        #print(s[i])
        rev.append(s[i])
    return rev
print(f"EX8\n{reverse_str(my_tuple)}")

#EX9
if my_tuple.index(6):
    print("EX9\nThe number '6' in in the tuple, index of it is:",my_tuple.index(6))
else:
    print("EX9\nThe number '6' in not exist in this tuple!")

#EX10
tup1 = (2,3,4,5)
tup2 = (10,20,30,40)
print("EX10")
for i in range(len(tup1)):
	print(tup1[i],"*",tup2[i],"=",tup1[i]*tup2[i])