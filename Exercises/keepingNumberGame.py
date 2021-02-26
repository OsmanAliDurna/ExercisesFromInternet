answer = int(input("Keep a number in your mind : "))

max = 7
counter = 0
guess = 50
last = 100
first = 1

question = 'I can find it in max {} times : '.format(max)
print ("Let's play the guessing game!")

while True:
  print('Your number is : {} My guess is : {}'.format(answer,guess))
  if guess < answer:
    first = guess
    guess = (guess + last) // 2
    counter += 1
    print('Little higher, I have still ', (max - counter), 'chances.')
  elif guess > answer:
    last = guess
    guess = (guess + first) // 2
    counter += 1
    print('Little lower, I have still ', (max - counter), 'chances.')
  else:
    counter += 1
    print('As I said I find it in ', counter ,' times')
    break