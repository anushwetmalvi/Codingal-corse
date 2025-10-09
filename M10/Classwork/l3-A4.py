with open('Codingal2.txt') as fp:
    data1 = fp.read()

with open('sample_data.txt') as fp:
    data2 = fp.read()

data1 += "\n"
data1 += data2
print("Merging two files....")
with open ("Mergedfile.txt","w") as fp:
    fp.write(data1)
