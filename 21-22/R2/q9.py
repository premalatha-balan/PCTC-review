
def slice_pattern(pattern):
  for i in range(10):
    if pattern[i] !=0:
      break
  print(f"i = {i}")
  for j in range(9, -1, -1):
    if pattern[j] !=0:
      break
  print(f"j = {j} ")
  slicep = pattern[i:j+1]
  print(f"slicep is {slicep} ")
  return(slicep)

firstgrid = [input() for i in range(10)]

subseq= ["0" for i in range(5)]
subseq[0] = [input() for i in range(10)]
subseq[1] = [input() for i in range(10)]
subseq[2] = [input() for i in range(10)]
subseq[3] = [input() for i in range(10)]
subseq[4] = [input() for i in range(10)]

num1 =0
for i in range (10): 
  num1+=firstgrid[i].count("1")

pattern = [firstgrid[i].count("1") for i in range(10)]
print(pattern)

slicep = slice_pattern(pattern)

print(f"slicep is {slicep} ")

num2=0
for k in range(5):
  subpattern = [subseq[k][kk].count("1") for kk in range(10)]
  print(f"subpattern{k} is {subpattern} ")

  slices = slice_pattern(subpattern)
  
  print(f"slices[{k}] is {slices} ")
  if slicep == slices:
    num2+=1
    
print(num2)

print(num1*num2)