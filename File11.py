outputfile=open("new_file.txt","w")
inputfile=open("my_file.txt","r")
line_seen_so_file=set()
print("Eliminating duplicate lines from the file")
for line in inputfile:
    if line not in line_seen_so_file:
        outputfile.write(line)
        line_seen_so_file.add(line)
inputfile.close()
outputfile.close()