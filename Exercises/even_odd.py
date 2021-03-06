counterOdd = 0
counterEven = 0
numbers = range(10)

print(*numbers)

for i in numbers:
    if i % 2 == 0:
        counterEven += 1
    else:
        counterOdd += 1

print("There are {} evens and {} odds.".format( counterEven, counterOdd ))

sum = 0

for i in range(75):
    sum += i

print(sum)