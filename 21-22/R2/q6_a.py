c= int(input())
r=int(input())
g = [input() for i in range(r)]
q1 = [i[:int(c/2)] for i in g[:int(r/2)]]
q2 = [i[int(c/2):] for i in g[:int(r/2)]]
q3 = [i[int(c/2):] for i in g[:int(r/2)]]
q4 = [i[int(c/2):] for i in g[int(r/2):]]
counter = 0
for i in range(len(q1)):
  counter+=str(bin(int(q1[i], 2) &int(q2[i], 2)&int(q3[i], 2)&int(q4[i], 2)))[2:].count('1')
print(counter)
