# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100230
标题: Reverse Bits LCCI
难度: easy
链接: https://leetcode.cn/problems/reverse-bits-lcci/
题目类型: 位运算、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 05.03. 翻转数位 - 给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。 示例 1： 输入: num = 1775(110111011112) 输出: 8 示例 2： 输入: num = 7(01112) 输出: 4
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来计算最长的连续1的长度，并在遇到0时考虑将其翻转为1。

算法步骤:
1. 初始化两个变量 `current_length` 和 `previous_length` 分别记录当前连续1的长度和上一个连续1的长度。
2. 遍历每一位，如果当前位是1，则增加 `current_length`；如果是0，则更新 `previous_length` 并重置 `current_length`。
3. 计算最大长度时，考虑将0翻转为1的情况，即 `current_length + previous_length + 1`。
4. 返回最大长度。

关键点:
- 使用滑动窗口技术来维护当前和之前的连续1的长度。
- 在遇到0时，更新最大长度并重置当前长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 因为输入是一个32位整数，所以遍历每一位的时间是常数级别的。
空间复杂度: O(1) - 只使用了几个额外的变量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(num: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    current_length = 0
    previous_length = 0
    max_length = 1  # 最小长度为1，因为可以翻转一个0为1

    for i in range(32):
        if (num & (1 << i)) != 0:
            current_length += 1
        else:
            previous_length = current_length if i > 0 and (num & (1 << (i - 1))) != 0 else 0
            current_length = 0
        max_length = max(max_length, current_length + previous_length + 1)

    return max_length


Solution = create_solution(solution_function_name)