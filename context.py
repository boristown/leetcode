import algorithm
import re

if __name__ == "__main__":
    print(algorithm.LCS("abc","ebvcy"))
    print(algorithm.largestRectangleArea([2,1,2]))
    pat = "^(.+?\D)?0\d"
    print(not re.match(pat,"1+051"))
    print(not re.match(pat,"05+1"))