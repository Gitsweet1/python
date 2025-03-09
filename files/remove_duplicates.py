def write_list_to_file(filename, data):
    with open(filename,'w') as file:
        for item in data:
            file.write(item + "\n")

def remove_duplicates(filename, data):
    list1=data
    list2=[]
    for l in range(len(list1)):
        if list1[l] not in list2:
            list2.append(list1[l])
    write_list_to_file(filename,list2)

str=['a','a','b','c','d','e','a','b']
remove_duplicates("output_rd.txt",str)