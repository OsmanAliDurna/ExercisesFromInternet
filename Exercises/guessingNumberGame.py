import random

answer = random.randint(1, 101)

max = 7
counter = 0

question = 'I can find it in max {} times : '.format(max)
print ("Let's play the guessing game!")

while True:
  guess = int(input(question))
  if guess < answer:
    counter += 1
    print('Little higher, I have still ', (max - counter), 'chances.')
  elif guess > answer:
    counter += 1
    print('Little lower, I have still ', (max - counter), 'chances.')
  else:
    print('As I said I find it in ',counter,' times')
    break