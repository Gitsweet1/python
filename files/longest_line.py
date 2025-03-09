def read_file_to_list(filename):
    with open(filename,'r') as file:
        lines=file.readlines()
        long=""
        for line in lines:
            if len(line)>len(long):
                long=line
    return long

def longest_line(filename):
    return read_file_to_list(filename)

print("the longest line is:",longest_line("t1.txt"))
