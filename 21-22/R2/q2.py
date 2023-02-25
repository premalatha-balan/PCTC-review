pour_out = float(input())

#re = round(pour_out%50.0, 1)
re = pour_out%50.0
free = 50 - re
#print(re, free)
print(round(free, 1))
