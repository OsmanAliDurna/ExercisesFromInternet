"""
Create a function that takes a number num and returns each place value in the number.

Examples
num_split(39) ➞ [30, 9]
num_split(-434) ➞ [-400, -30, -4]
num_split(100) ➞ [100, 0, 0]
"""

def num_split(num):
    resultlist = []
    number = abs(int(num))
    for i in range(len(str(number))):
        resultlist.append(number%(10**(i+1)))
        number -= number%(10**(i+1))
    return resultlist[::-1] if int(num)>0 else [-1*i for i in resultlist[::-1]]