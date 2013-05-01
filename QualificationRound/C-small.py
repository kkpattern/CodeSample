# Problem
#
# Little John likes palindromes, and thinks them to be fair (which is a fancy
# word for nice). A palindrome is just an integer that reads the same backwards
# and forwards - so 6, 11 and 121 are all palindromes, while 10, 12, 223 and
# 2244 are not (even though 010=10, we don't consider leading zeroes when
# determining whether a number is a palindrome).
#
# He recently became interested in squares as well, and formed the definition
# of a fair and square number - it is a number that is a palindrome and the
# square of a palindrome at the same time. For instance, 1, 9 and 121 are fair
# and square (being palindromes and squares, respectively, of 1, 3 and 11),
# while 16, 22 and 676 are not fair and square: 16 is not a palindrome, 22 is
# not a square, and while 676 is a palindrome and a square number, it is the
# square of 26, which is not a palindrome.
#
# Now he wants to search for bigger fair and square numbers. Your task is,
# given an interval Little John is searching through, to tell him how many fair
# and square numbers are there in the interval, so he knows when he has found
# them all.
# Solving this problem
#
# Usually, Google Code Jam problems have 1 Small input and 1 Large input. This
# problem has 1 Small input and 2 Large inputs. Once you have solved the Small
# input, you will be able to download any of the two Large inputs. As usual,
# you will be able to retry the Small input (with a time penalty), while you
# will get only one chance at each of the Large inputs.
#
# Input
#
# The first line of the input gives the number of test cases, T. T lines
# follow. Each line contains two integers, A and B - the endpoints of the
# interval Little John is looking at.
#
# Output
#
# For each test case, output one line containing "Case #x: y", where x is the
# case number (starting from 1) and y is the number of fair and square numbers
# greater than or equal to A and smaller than or equal to B.
#
# Limits
#
# 1 ≤ T ≤ 100.
# 1 ≤ A ≤ B ≤ 1000.
import math

def palindrome(n):
    old_n = n
    new_n = 0
    while n > 0:
        new_n = new_n*10+n%10
        n /= 10
    return new_n == old_n

def main():
    T = int(raw_input())
    for ti in xrange(T):
        AB = [int(x) for x in raw_input().split()]
        A = AB[0]
        B = AB[1]
        ans = 0
        for i in xrange(int(math.sqrt(A)), int(math.sqrt(B))+1):
            square = i*i
            if A<=square<=B and palindrome(i) and palindrome(square):
                ans += 1
        print "Case #{0}: {1}".format(ti+1, ans)
    pass

if __name__ == "__main__":
    main()
