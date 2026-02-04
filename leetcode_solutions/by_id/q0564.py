# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 564
标题: Find the Closest Palindrome
难度: hard
链接: https://leetcode.cn/problems/find-the-closest-palindrome/
题目类型: 数学、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
564. 寻找最近的回文数 - 给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。 “最近的”定义为两个整数差的绝对值最小。 示例 1: 输入: n = "123" 输出: "121" 示例 2: 输入: n = "1" 输出: "0" 解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。 提示: * 1 <= n.length <= 18 * n 只由数字组成 * n 不含前导 0 * n 代表在 [1, 1018 - 1] 范围内的整数
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过生成三个候选回文数来找到最近的回文数。

算法步骤:
1. 生成中间部分减一的回文数。
2. 生成中间部分加一的回文数。
3. 生成中间部分不变的回文数。
4. 比较这三个回文数与原数的差值，选择差值最小且不等于原数的回文数。

关键点:
- 生成回文数时，需要考虑长度为奇数和偶数的情况。
- 处理特殊情况，如所有9或所有0的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_closest_palindrome(n: str) -> str:
    """
    函数式接口 - 寻找最近的回文数
    """
    # 特殊情况处理
    if len(n) == 1:
        return str(int(n) - 1)
    
    # 将字符串转换为列表以便操作
    n_list = list(n)
    length = len(n_list)
    
    # 生成中间部分减一的回文数
    mid = (length - 1) // 2
    left = n_list[:mid + 1]
    if length % 2 == 0:
        left[-1] = str(int(left[-1]) - 1)
    else:
        left[mid] = str(int(left[mid]) - 1)
    
    if left[0] == '0':
        left = ['9'] * (len(left) - 1)
    else:
        for i in range(len(left) - 1, -1, -1):
            if left[i] < '0':
                left[i] = '9'
                left[i - 1] = str(int(left[i - 1]) - 1)
            else:
                break
    
    candidate1 = left + left[:-1][::-1] if length % 2 == 0 else left + left[::-1]
    
    # 生成中间部分加一的回文数
    left = n_list[:mid + 1]
    if length % 2 == 0:
        left[-1] = str(int(left[-1]) + 1)
    else:
        left[mid] = str(int(left[mid]) + 1)
    
    if left[0] > '9':
        left = ['0'] + ['0'] * (len(left) - 1)
        left[0] = '1'
    else:
        for i in range(len(left)):
            if left[i] > '9':
                left[i] = '0'
                left[i + 1] = str(int(left[i + 1]) + 1)
            else:
                break
    
    candidate2 = left + left[:-1][::-1] if length % 2 == 0 else left + left[::-1]
    
    # 生成中间部分不变的回文数
    left = n_list[:mid + 1]
    candidate3 = left + left[:-1][::-1] if length % 2 == 0 else left + left[::-1]
    
    # 比较三个候选回文数
    candidates = [candidate1, candidate2, candidate3]
    closest = min(candidates, key=lambda x: (abs(int(''.join(x)) - int(n)), int(''.join(x))))
    
    return ''.join(closest)


Solution = create_solution(find_closest_palindrome)