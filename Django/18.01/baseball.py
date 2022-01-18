# ops = ["5", "2", "C", "D", "+"]

ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]

score = [0]

for i in ops:
    if i == "D":
        score.append(2 * score[-1])
    elif i == "C":
        score.pop()
    elif i == "+":
        score.append(score[-2] + score[-1])
    else:
        score.append(int(i))

print(sum(score))
