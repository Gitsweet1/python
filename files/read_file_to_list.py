def read_file_to_list(filename):
    with open(filename,'r') as file:
        lines=file.readlines()
        #print(lines)
    return [line.strip() for line in lines]
'''
    lines=[]
    for line in open(filename):
        lines.append(line)
    #lines=open(filename)
    return lines
'''
print(read_file_to_list("t1.txt"))
#open('t1.txt','r')