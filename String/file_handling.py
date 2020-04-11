handle = open('/home/abbisk/Documents/Code/python-scripts/String/greetings.txt')
count = 0
for line in handle:
    count = count+1
print('Line count : ', count)

# Reading the whole file
fhand = open('/home/abbisk/Documents/Code/python-scripts/String/greetings.txt')
inp = fhand.read()
print("Length of the File : " + str(len(inp)))
# print(inp)
print(inp[0:5])

# Searching through the file
fhand = open('/home/abbisk/Documents/Code/python-scripts/String/greetings.txt')
for line in fhand:
    if line.startswith('Thanks'):
        print(line)

# Remove the blank lines 
fhand = open('/home/abbisk/Documents/Code/python-scripts/String/greetings.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('Thanks'):
        print(line)