#five passes and five fails
caves = input()
nth = int(input())

tree = {}
for i in range(len(caves) - 1):
  tree[caves[i]] = caves[i + 1:i + 2 + 1]
  #print(f" {tree} at {i} ")

#print(f"the final dictionary is {tree} ")

paths = ["A"]
count = len(paths)

while paths[0][-1] != caves[-1]:
  poss = tree[paths[0][-1]]
  #print(f"{poss} ")
  if len(poss) == 2:
    path1 = paths[0] + poss[0]
    path2 = paths[0] + poss[1]
    paths.append(path1)
    paths.append(path2)
    #print(f"i am going to pop {paths[0]} as it has become {path1} and {path2} ")
  elif len(poss) == 1:
    path = paths[0] + poss[0]
    paths.append(path)
    #print(f"i am going to pop {paths[0]} as it has become {path} ")
  else:
    break
  paths.pop(0)
  count = len(paths)
  print(paths, count)

  path = paths[0]
  countw = 0
  while path[-1] == caves[-1] and countw != count:
    paths.append(path)
    #print(f"before popping {paths}")
    paths.pop(0)
    #print(f"after removing {paths}")
    countw += 1
    path = paths[0]

print(paths)
paths.sort()
print(paths)
print(f"{paths[nth-1]}")
