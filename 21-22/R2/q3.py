
n = int(input())
m = int(input())
fc = input()
sc = input()

"""n=15
m=5
fc = "#"
sc = "%""""

empty = int((n-m-2)/2)
for i in range(n):
  print(fc, end="")
print()
for e in range (empty):
  print(fc, end="")
  for ee in range (n-2):
    print(" ",end="")
  print(fc)
    
for jj in range(m):
  print(fc, end="")
  for k in range(empty):
    print(" ", end="")
  for j in range(m):
    print(sc, end="")

