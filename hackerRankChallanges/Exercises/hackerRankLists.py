"""
Consider a list (list = []). You can perform the following commands:
1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command
will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example:
N = 4
append 1
append 2
insert 3 1
print

-> Append 1 to the list, arr = [1].
-> Append 2 to the list, arr = [1, 2].
-> Insert 3 at index 1, arr = [1, 3, 2].
-> Print the array.

Output:
[1, 3, 2]

Input Format:
The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints:
The elements added to the list must be integers.

Output Format:
For each command of type print, print the list on a new line.

Sample Input 0:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

if __name__ == '__main__':
    N = int(input())

output = []
commands = []

for i in range(N):
    commands.append(input().split())

for i in range(N):
    if commands[i][0] == "append":
        output.append(int(commands[i][1]))
    elif commands[i][0] == "pop":
        output.pop()
    elif commands[i][0] == "insert":
        output.insert(int(commands[i][1]),  int(commands[i][2]))
    elif commands[i][0] == "print":
        print(output)
    elif commands[i][0] == "remove":
        output.remove(int(commands[i][1]))
    elif commands[i][0] == "reverse":
        output.reverse()
    elif commands[i][0] == "sort":
        output.sort()
