
q = list(map(int, input()))
print(''.join(list(map(str, [sorted(q[:i+1])[:int((i+2)/2)][-1]for i in range(len(q))]))))