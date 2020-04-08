fruit = 'apple'
user = input("Enter the fruits name \n")

if user == 'apple':
    print("All right it's apple")

if user < 'apple':
    print("String comes befor apple")

if user > 'appl e':
    print("String comes after \n")

# String library
greet = 'HEllo world'
zap = greet.lower()
print(zap)
print("Hello dude".upper() + "\n")

# Searching a String
fruit = 'banana'
pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)

# Search and Replace
greet = 'Hello abhishek'
nstr = greet.replace('abhishek', 'Abhishek')
print(nstr)
nstr1 = greet.replace('abhishek','Krishna')
print(nstr1 + "\n")

# String whitespace
greet = '  Hello abhishek   '
print(greet.lstrip() + "\n")
print(greet.rstrip() + "\n")
print(greet.strip())


# Prefix
line = 'Please have a nice day'
print(line.startswith('Please \n'))
print(line.startswith('p \n'))

# Parsing and Extracting

data = input("Enter email id and name after a space")
data.
firstpos = data.find('@')
print("Position of @ ", + firstpos)
host = data[firstpos+1 : -1]
print("Mail hosting \t" + host)