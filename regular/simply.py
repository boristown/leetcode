import re

if __name__ == '__main__':
    #模式匹配：邮箱
    print("模式匹配：邮箱:")
    s = "boristown@gmail.com"
    pat = "^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
    print("字符串："+s+"\n正则："+pat+"\n匹配结果："+str(re.match(pat,s)))
    #模式匹配：域名
    print("模式匹配：域名:")
    s = "leetcode.cn"
    pat = "[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?"
    print("字符串："+s+"\n正则："+pat+"\n匹配结果："+str(re.match(pat,s)))