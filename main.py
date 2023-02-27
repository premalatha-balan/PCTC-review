
"""a = [0, 2, 0, 2, 1, 3, 0, 1, 0]
c = [2, 1, 3, 0, 1]
b = ''.join(map(str, a)).index(''.join(map(str, c)))
print(b)"""

def findPattern (in_lst):
  row_indx=[]
  p1_indx =[]
  for i in range(10): 
    counter = 0
    counter+=in_lst[i].count("1")
    if counter!=0:
      row_indx.append(i)
      print(f"counter is {counter} at {i} and the str is {in_lst[i]}")
      temp1 = 0
      temp0 = 0
      while (temp1 != 9 and temp1!=-1) or (temp0 != 9 and temp0!=-1):
        temp1 = in_lst[i].find("1", temp0)
        p1_indx.append(temp1)
        temp0 = in_lst[i].find("0",temp1)
        print(f"temp1 = {temp1} and temp0 ={temp0} ") 
    else:
      print(f"the entire string for {i} is {in_lst[i]} ")
  row_indx = list(dict.fromkeys(row_indx))
  p1_indx = list(dict.fromkeys(p1_indx))
  if -1 in row_indx: row_indx.remove(-1)
  if -1 in p1_indx: p1_indx.remove(-1)
  row_indx.sort()
  p1_indx.sort()
  print(f"rows in the pattern {row_indx}")
  print(f"columns in the pattern {p1_indx} ")
  return(counter)
    

firstgrid = [input() for i in range(10)]

subseq= ["0" for i in range(5)]
subseq[0] = [input() for i in range(10)]
subseq[1] = [input() for i in range(10)]
subseq[2] = [input() for i in range(10)]
subseq[3] = [input() for i in range(10)]
subseq[4] = [input() for i in range(10)]

#countf=findPattern(firstgrid)
countf=findPattern(subseq[3])
print(countf)