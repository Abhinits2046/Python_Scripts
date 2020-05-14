# Append
t = ['a','b','c','d','e','f','g','h','i']
t.append(input('Input for append method : '))
print(t)

# Extend 
# Takes list as an arguement and append all the elements
t1 = ['k','l']
inp = list(map(str, input("Enter the elements Extend : ")))
t1.extend(inp)
print(t1)

# Sorting
print("Sorting")
t2 = ['d', 'c', 'e', 'b', 'a']
t2.sort()
print(t2)

# Deleting elements
print("Deleting elements")
t.pop(1)
t.remove('a')
print(t) 