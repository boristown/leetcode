import algorithm
import re

if __name__ == "__main__":
    print(algorithm.LCS("abc","ebvcy"))
    print(algorithm.largestRectangleArea([2,1,2]))
    pat = "^(.+?\D)?0\d"
    print(not re.match(pat,"1+051"))
    print(not re.match(pat,"05+1"))
    print(algorithm.CourseScheduler.schedule_by_duration_lastDay([[0, 100, 200], [1, 200, 1300], [2, 1000, 1250], [3, 2000, 3200]]))