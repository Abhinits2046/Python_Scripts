handle = open('/home/abbisk/Documents/Code/python-scripts/String/greetings.txt')
count = 0
for line in handle:
    count = count+1
print('Line count : ', count)

# Reading the whole file
fhand = open('/home/abbisk/Documents/Code/python-scripts/String/greetings.txt')
inp = fhand.read()
inp1 = inp.rstrip()
print("Length of the File : " + str(len(inp)))
print(inp.upper())  # Change the whole file text in capital latter
# print(inp[0:5])

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

# Method 2 for Remove blank line
fhand = open('/home/abbisk/Documents/Code/python-scripts/String/greetings.txt')
for line in fhand:
    if not line.startswith('Thanks'):
        continue
    print(line)

# Letting the use chose the file name
print("Letting the use choose the file name")
fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    count = count+1
print("No of line in the file are ", count)

# Writing files
fout = open()
