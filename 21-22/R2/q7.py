

"""x = int(inpu())
t = int(inpu())
y = int(inpu())"""

x = 5
t = 3
y = 10

x = 9
t = 4
y = 14

xhops=x*t
yhops = 0
count = 0+t
while yhops<xhops:
  xhops+=x
  yhops+=y
  count+=1
  print(count, xhops, yhops)

print(count, xhops, yhops)