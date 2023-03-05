
def med(lst):
  lst.sort()
  return lst[round((len(lst)/2))-1]

#entstr= input()
#entstr = str(21423814127333)

enter = list(map(int, input()))

room =[]
chalk=[]

for i in range(len(enter)):
  room.append(enter[i])
  chalk.append(med(room))

print("".join(list(map(str, chalk))))

#21222222222233
#21122222222223