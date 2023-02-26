
"""12
ALISHA:DOWN JACK
ANISH:UP ABIGAIL
MARTHA:UP JACK
AMY:UP AMY
GRACE:DOWN MARTHA
TONY:UP ANISH
JACK:DOWN JACK
ADI:DOWN ABIGAIL
NED:UP TONY
ABIGAIL:DOWN GRACE
NAVEENA:UP NED
RICHARD:UP GRACE"""

names_votes={}

n = int(input())
for i in range(n):
  name1, second = input().split(":")
  choice, name2 = second.split(" ")
  if name1 not in names_votes:
    names_votes[name1]=0
  if name2 not in names_votes:
    names_votes[name2]=0
  if choice.lower() == "down":
    names_votes[name2] -=1
  elif choice.lower() == "up":
    names_votes[name2]+=1

vote_out = min(names_votes.values())
name = [key for key in names_votes if names_votes[key] == vote_out]
#print(names_votes)
#print(name, vote_out)

for i in name: print(i)