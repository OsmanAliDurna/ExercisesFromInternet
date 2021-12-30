# Enter your code here. Read input from STDIN. Print output to STDOUT
K, M = list(map(int, input().split()))

sum = 0

for i in range(K):
    listem = list(map(int, input().split()))[1:]
    maxOfLine = max(listem) % M
    sum = (sum + (maxOfLine ** 2)) % M

print(sum)
