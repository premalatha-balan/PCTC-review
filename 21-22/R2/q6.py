
"""c= int(input())
r=int(input())
for i in range(int(r/2)):
  q1q2[i]=input()
for i in range(int(r/2)):
  q3q4[i]=input()"""


c = 10
r = 6
q1q2=["1" for i in range(int(r/2))]
q3q4=["1" for i in range(int(r/2))]

q1q2[0] ="1111001111"
q1q2[1]="1010011110"
q1q2[2]="0011010100"

q3q4[0]="0111010111"
q3q4[1]="1111001011"
q3q4[2]="0011110001"


q1 = ["1" for i in range(int(r/2))]
q2 = ["1" for i in range(int(r/2))]

q3 = ["1" for i in range(int(r/2))]
q4 = ["1" for i in range(int(r/2))]

"""print(q1)
print(q2)
print(q3)
print(q4)
print(q1q2)
print(q3q4)"""

for i in range(int(r/2)):
  q1[i]=q1q2[i][:int(c/2)]
  q2[i]=q1q2[i][int(c/2):]
  q3[i]=q3q4[i][:int(c/2)]
  q4[i]=q3q4[i][int(c/2):]


count=0
for i in range(int(r/2)):
  for j in range(int(c/2)):
#    if q1[i][j] == "1" and q2[i][j] == "1" and q3[i][j] == "1" and q4[i][j] == "1":
#    count+=1
#    if q1[i][j] == "0" or q2[i][j] == "0" or q3[i][j] == "0" or q4[i][j] == "0":
#      continue
#    else:
#      count+=1"""
    a=int(q1[i][j])
    b=int(q2[i][j])
    c=int(q3[i][j])
    d=int(q4[i][j]) 
    if a*b*c*d!= 0:
      count+=1
      print(f"q1 = {a}, q2 = {b}, q3 = {c}, q4 = {d} and count = {count}")


print(count)