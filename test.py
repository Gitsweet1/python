def write_list_to_file(filename, data):
    with open(filename,'w') as file:
        for item in data:
            file.write(item + "\n")

def read_file_to_list(filename):
    with open(filename,'r') as file:
        lines=file.readlines()
    return [line.strip() for line in lines]

list1=read_file_to_list("1.txt")
list2=read_file_to_list("2.txt")
write_list_to_file("output3.txt",list1+list2)