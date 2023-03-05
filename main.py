
def build_path(in_str, path_str):
  path = in_str.join(path_str)
  

caves = input()
nth = int(input())


tree = {}
for i in range(len(caves)-1):
  tree[caves[i]] = caves[i+1:i+2+1] 
  print(f" {tree} at {i} ")

print(f"the final dictionary is {tree} ")

path=""
for i in range(len(caves)-1):
  path = path.join(tree[caves[i]])

  
  
