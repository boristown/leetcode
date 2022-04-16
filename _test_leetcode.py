import re

if __name__ == "__main__":
    pat = "^(.+?\D)?0\d"
    print(not re.match(pat,"1+051"))
    print(not re.match(pat,"05+1"))