"""
3.无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


def func(str1):
    l = 0
    start = 0
    dic = {}
    for i in range(len(str1)):
        cur = str1[i]
        if cur not in dic.keys():
            dic[cur] = i
        else:
            if dic[cur] + 1 > start:
                start = dic[cur] + 1
            dic[cur] = i
        if i - start + 1 > l:
            l = i - start + 1

    return l


str1 = input('请输入字符串')
print(func(str1))

"""
返回结果
请输入字符串kwwpew
3
"""