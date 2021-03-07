"""
Objective
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum
number of consecutive 1's in n's binary representation. When working with different bases, 
it is common to show the base as a subscript.

Example
n = 125
The binary representation of (125)_10 is (1111101)_2. In base 10, there are 5 and 1 consecutive ones in two groups.
Print the maximum, 5.

Input Format
A single integer, n.

Constraints
1 <= n <= 1000000

Output Format
Print a single base-10 integer that denotes the maximum number of consecutive 1's in the binary representation of n.

Sample Input 1
5

Sample Output 1
1

Sample Input 2
13

Sample Output 2
2

Explanation

Sample Case 1:
The binary representation of (5)_10 is (101)_2, so the maximum number of consecutive 1's is 1.

Sample Case 2:
The binary representation of (13)_10 is (1101)_2, so the maximum number of consecutive 1's is 2.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    
    if n >= 1 and n <= 1000000:

        i = 1
        count1s = 0
        max1s = 0

        while n > 2:
            
            if (n % (2 ** i)) :    

                count1s += 1
                
                if max1s < count1s:
                    max1s = count1s

            else:               

                count1s = 0
            
            n -= n % (2 ** i)
            i += 1

        print(max1s)