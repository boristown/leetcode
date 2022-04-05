#!/usr/bin/python
# -*- coding: utf-8 -*-
#最长回文子串—Manacher 算法 及 python实现
#https://www.cnblogs.com/dahu-daqing/p/9302681.html

def max_substr(string):
  s_list = [s for s in string]
  string = '#' + '#'.join(s_list) + '#'
  max_length = 0
  length = len(string)
  for index in range(0, length):
    r_length = get_length2(string, index, max_length)
    if max_length < r_length:
      max_length = r_length
  return max_length

def get_length2(string, index, max_length):
  # 基于已知的最长字串求最长字串
  # 1.中心+最大半径超出字符串范围, return
  r_ = len(string)
  if index + max_length > r_:
    return max_length

  # 2.无法超越最大半径, return
  l_string = string[index - max_length + 1 : index + 1]
  r_string = string[index : index + max_length]
  if l_string != r_string[::-1]:
    return max_length

  # 3.计算新的最大半径
  result = max_length
  for i in range(max_length, r_):
    if index-i >= 0 and index+i < r_ and string[index-i] == string[index+i]:
      result += 1
    else:
      break
  return result - 1

if __name__ == "__main__":
  result = max_substr("35534321")
  print(result)