name = input("What is your name?")
question = input("What is your question?")
answer = ""

import random
random_number = random.randint(1,10)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sourcecs say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very Doubtful."
else:
  answer = "Error"

if name =="" and question =="":
  print("Fortune-telling time!🤩 What's your name and what will you like to find out?")
elif name == "":
  print("Question :" , question)
  print("Magic 8-ball's answer:" , answer)
elif question == "":
    print("Hi " + name + ", what will you like to ask?")
else:
  print(name , "asks :" , question)
  print("Magic 8-ball's answer:" , answer)
