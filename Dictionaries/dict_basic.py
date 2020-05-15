purse = dict()
purse['age'] = 21 #putting 21 in purse dictionary by lebel age#
purse['price'] = 300
purse['count'] = 3
print(purse)

# Dictionar is mutable
purse['count'] = purse['count']+10
print("Changed output :  ", purse)

# word counting method1
counts = dict()
names = ['abhishek','anurag','abhishek','ashvin','vikash','mukul','ashvin','anurag']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name]+1
print(counts)

# word counting method2:
print("Method2")
count1 = dict()
for name in names:
    count1[name] = count1.get(name, 0)+1
print(count1)
 