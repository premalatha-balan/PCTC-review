from math import sqrt
a=int(input())
b=int(input())
c=int(input())

outL = a**2 + b**2
outR = c**2
if outL < outR:
  print(f"{a} squared plus {b} squared is less than {c} squared")
elif outL > outR:
  print(f"{a} squared plus {b} squared is greater than {c} squared")
else:
  print(f"{a} squared plus {b} squared is equal to {c} squared")

