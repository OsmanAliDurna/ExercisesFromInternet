import random

answer = random.randint(1, 101)

question = 'I can find it in max 7 times : '
print ("Let's play the guessing game!")

while True:
  guess = int(input(question))
  if guess < answer:
    print('Little higher')
  elif guess > answer:
    print('Little lower')
  else:
    print('Are you a MINDREADER!!!')
    break