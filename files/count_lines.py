def read_file_to_list(filename):
    with open(filename,'r') as file:
        lines=file.readlines()
        #print(lines)
    print(len([line.strip() for line in lines]))
    return len([line.strip() for line in lines])

def count_lines(filename):
    return read_file_to_list(filename)

print("this file have:",count_lines("output.txt"),"lines")

#print(len(['a','bbb','ccccc']))