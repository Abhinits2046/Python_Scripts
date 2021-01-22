''' Pattern 
    1
   1 2
  1   3
 1     4
1       5
1 2 3 4 5 
'''
n = int(input())
i = 1
while i<=n:
  space = 1
  while space <= n-i:
    print(" ",end = "")
    space +=1
  p=1
  j = 1
  while j<2:
    print(p,end="")
    j+=1
  if i>1:
    k = i-2
    j=1
    spaces = (2*k)+1
    while j <= spaces:
      print(" ",end = "")
      j = j+1
    p=1
    j=1
    while j<2:
      print(i,end="")
      j=j+1

  i+=1
  print()
for j in range(1,i):
  print(j,end = " ")