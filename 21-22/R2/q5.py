"""text1 = int(input())
text2 = int(input())"""

"""text1 = 12
text2 = 5"""

"""text1 = 17
text2 = 84"""

text1 = 10
text2 = 0

money1 = text1 + text2/100
money2 = text2 + text1/100
if max(money1, money2) <= 20:
  print("£%.2f" % min(money1, money2))
  print("£%.2f" % max(money1, money2))
else:
  print("£%.2f" % min(money1, money2))