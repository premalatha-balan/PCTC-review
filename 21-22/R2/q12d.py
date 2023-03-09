#4 score and runtime error

def addstr(instr, inlst):
  return [instr+strlst for strlst in inlst]

caves = input()
nth = int(input())

tree = {}
for i in range(len(caves) - 1):
  tree[caves[i]] = caves[i + 1:i + 2 + 1]

paths = [caves]
count = len(paths)
path = tree[caves[-2]]

for cave in reversed(caves[:-1]):
  print(cave, tree[cave])
  if len(tree[cave])==1:
    tree[cave]=[cave+tree[cave]]
  elif len(tree[cave])==2:
    poss0, poss1=tree[cave][0], tree[cave][1]
    print(f"poss0 = {poss0} and poss1 = {poss1} ")
    if poss0 in tree:
      tree[cave]=addstr(cave, tree[poss0])
    else:    
      tree[cave]=addstr(cave, tree[cave])
    if poss1 in tree:
      addlst = addstr(cave, tree[poss1])
      for item in addlst:
        tree[cave].append(item)
    elif poss1 == caves[-1]:
      tree[cave].append(cave+poss1)
  print(f"{cave} : {tree[cave]}")

print(tree["A"][nth-1])
  
