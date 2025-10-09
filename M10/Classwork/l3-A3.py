outputfile = open("Updatedfile.txt", "w")

inputfile = open("codingal.txt", "r")

lines_seen_so_far = set() 
print("Eliminating duplicate lines.........................")

for line in inputfile:

    if line not in lines_seen_so_far: 

        outputfile.write(line)

        lines_seen_so_far.add(line)

inputfile.close()
outputfile.close()