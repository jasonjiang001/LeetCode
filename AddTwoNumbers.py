"""
2.两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


def func(str1,str2):
    list1 = list(str1)
    list2 = list(str2)
    l1 = ''
    for i in reversed(list1):
        l1 += i

    l2 = ''
    for i in reversed(list2):
        l2 += i

    sum = int(l1) + int(l2)
    print('{}+{}={}'.format(int(l1),int(l2),sum))

    l3 = ''
    for i in reversed(str(sum)):
        l3 += i

    return l3


str1 = input('请输入第一个数字字符串')
str2 = input('请输入第二个数字字符串')

print(func(str1,str2))


"""
返回结果：
请输入第一个数字字符串123
请输入第二个数字字符串456
321+654=975
579
"""