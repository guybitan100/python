# Open file for write and create it
fw = open('sample.txt', 'w')
fw.write('writing some stuff in my text file\n')
fw.write('i lobe python\n')
fw.close()
# Open file for read
fr = open('sample.txt', 'r')
text = fr.read()
print(text)
