
questions = ["how", "what", "why", "who", "when", "where"]

while True:
  chat_in = input()
  if chat_in in questions or chat_in[-1] == "?":
    print("Not sure really")
    continue
  elif chat_in == "goodbye":
    print("see you!")
    break
  else:
    print("but why?")
    