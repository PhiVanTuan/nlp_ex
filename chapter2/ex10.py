file_object  = open("hightemp.txt","r")
num_lines = sum(1 for line in file_object)
print(num_lines)
