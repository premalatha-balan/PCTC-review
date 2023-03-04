
X = "XXX"
O = "OOO"


def winning(win, p1, p2):
  X = "XXX"
  O = "OOO"
  if win == O: p1 += 1
  if win == X: p2 += 1
  return (p1, p2)


column = lambda grid, i: [grid[k][i] for k in range(4)]

d0033 = lambda grid: [grid[k][k] for k in range(4)]

d0330 = lambda grid: [grid[k][0 - k - 1] for k in range(4)]

d0123 = lambda grid: [grid[k][k + 1] for k in range(3)]

d1032 = lambda grid: [grid[k + 1][k] for k in range(3)]

d0220 = lambda grid: [grid[k][0 - k - 2] for k in range(3)]

d1331 = lambda grid: [grid[k + 1][0 - k - 1] for k in range(3)]

grid = [["" for i in range(4)] for j in range(4)]
grid_index = {"a": 0, "b": 1, "c": 2, "d": 3, "1": 3, "2": 2, "3": 1, "4": 0}

play = [input() for i in range(16)]

for i in range(0, 16, 2):
  r, c = grid_index[play[i][0]], grid_index[play[i][1]]
  grid[r][c] = "O"

  r, c = grid_index[play[i + 1][0]], grid_index[play[i + 1][1]]
  grid[r][c] = "X"

for i in range(4):
  print(grid[i])

p1, p2 = 0, 0
print(p1, p2)

for i in range(4):
  win = "".join(grid[i])[:-1]
  p1, p2 = winning(win, p1, p2)
  print(f"first cut is {win} and p1 = {p1}, p2 = {p2} ")
  win = "".join(grid[i])[1:]
  p1, p2 = winning(win, p1, p2)
  print(f"second cut is {win} and p1 = {p1}, p2 = {p2} ")

  colc = column(grid, i)
  win = "".join(colc)[:-1]
  #print(f"win = {win} ")
  p1, p2 = winning(win, p1, p2)
  print(f"first column cut is {win} and p1 = {p1}, p2 = {p2} ")
  win = "".join(colc)[1:]
  p1, p2 = winning(win, p1, p2)
  print(f"second column cut is {win} and p1 = {p1}, p2 = {p2} ")

win = "".join(d0033(grid))[:-1]
p1, p2 = winning(win, p1, p2)
print(f"first diag cut is {win} and p1 = {p1}, p2 = {p2} ")
win = "".join(d0033(grid))[1:]
p1, p2 = winning(win, p1, p2)
print(f"second diag cut is {win} and p1 = {p1}, p2 = {p2} ")

win = "".join(d0330(grid))[:-1]
p1, p2 = winning(win, p1, p2)
print(f"first diag2 cut is {win} and p1 = {p1}, p2 = {p2} ")
win = "".join(d0330(grid))[1:]
p1, p2 = winning(win, p1, p2)
print(f"second diag2 cut is {win} and p1 = {p1}, p2 = {p2} ")

#Now count the other diags. There are four more of them.
