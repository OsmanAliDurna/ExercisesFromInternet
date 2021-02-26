import random

answer = random.randint(1, 101)

max = 7
counter = 0

question = 'I try to find it in max {} times : '.format(max)
print ("Let's play the guessing game!")

while True:
  guess = int(input(question))
  counter += 1
  if guess < answer:
    print('Little higher, I have still ', (max - counter), 'chances.')
  elif guess > answer:
    print('Little lower, I have still ', (max - counter), 'chances.')
  else:
    print('As I said I find it in ',counter,' times')
    break
  if (counter > 6):
    print("I LOSE this time :'( ")
    break