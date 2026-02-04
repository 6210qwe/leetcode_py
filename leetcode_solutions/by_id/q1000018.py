# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000018
标题: English Int LCCI
难度: hard
链接: https://leetcode.cn/problems/english-int-lcci/
题目类型: 递归、数学、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 16.08. 整数的英语表示 - 给定一个整数，打印该整数的英文描述。 示例 1： 输入：123 输出："One Hundred Twenty Three" 示例 2： 输入：12345 输出："Twelve Thousand Three Hundred Forty Five" 示例 3： 输入：1234567 输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven" 示例 4： 输入：1234567891 输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One" 注意：本题与 273 题相同：https://leetcode.cn/problems/integer-to-english-words/ [https://leetcode.cn/problems/integer-to-english-words/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将数字分段处理，每三位一组，然后将每组转换为英文表示，最后拼接起来。

算法步骤:
1. 定义三个字典，分别表示个位数、十位数和百位数的英文表示。
2. 将数字每三位一组进行分段。
3. 对每一段进行处理，转换为英文表示。
4. 拼接所有段的英文表示，并加上相应的单位（如Thousand, Million, Billion）。

关键点:
- 分段处理，每三位一组。
- 使用递归或迭代处理每一段。
- 注意特殊处理0的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n)，其中n是输入数字的大小。因为我们将数字每三位一组进行处理，处理次数与数字的位数成正比。
空间复杂度: O(1)，除了输出结果外，我们只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def number_to_words(num: int) -> str:
    if num == 0:
        return "Zero"

    def one(num: int) -> str:
        switcher = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        return switcher.get(num, '')

    def two_less_20(num: int) -> str:
        switcher = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        return switcher.get(num, '')

    def ten(num: int) -> str:
        switcher = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        return switcher.get(num, '')

    def two(num: int) -> str:
        if not num:
            return ''
        elif num < 10:
            return one(num)
        elif num < 20:
            return two_less_20(num)
        else:
            tenner = num // 10
            rest = num - tenner * 10
            return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)

    def three(num: int) -> str:
        hundred = num // 100
        rest = num - hundred * 100
        if hundred and rest:
            return one(hundred) + ' Hundred ' + two(rest)
        elif not hundred and rest:
            return two(rest)
        elif hundred and not rest:
            return one(hundred) + ' Hundred'

    billion = num // 1000000000
    million = (num - billion * 1000000000) // 1000000
    thousand = (num - billion * 1000000000 - million * 1000000) // 1000
    remainder = num - billion * 1000000000 - million * 1000000 - thousand * 1000

    result = ''
    if billion:
        result += three(billion) + ' Billion'
    if million:
        result += ' ' if result else ''
        result += three(million) + ' Million'
    if thousand:
        result += ' ' if result else ''
        result += three(thousand) + ' Thousand'
    if remainder:
        result += ' ' if result else ''
        result += three(remainder)
    return result.strip()

Solution = create_solution(number_to_words)