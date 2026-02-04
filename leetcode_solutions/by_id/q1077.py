# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1077
标题: Confusing Number II
难度: hard
链接: https://leetcode.cn/problems/confusing-number-ii/
题目类型: 数学、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1088. 易混淆数 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法生成所有可能的易混淆数，并检查它们是否满足条件。

算法步骤:
1. 定义一个递归函数来生成所有可能的数字。
2. 在递归过程中，使用当前位数和旋转后的数字进行比较。
3. 如果当前数字是易混淆数，则将其加入结果列表。
4. 递归结束条件是当前数字达到最大长度。

关键点:
- 只使用可以旋转后仍然是有效数字的字符：0, 1, 6, 8, 9。
- 递归过程中需要考虑前导零的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(5^N)，其中 N 是数字的最大长度。每个位置有 5 种选择（0, 1, 6, 8, 9）。
空间复杂度: O(N)，递归调用栈的深度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def confusingNumberII(n: int) -> int:
    """
    函数式接口 - 计算小于等于 n 的易混淆数的数量
    """
    # 易混淆数的映射
    mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
    
    def is_confusing(num: int) -> bool:
        original = num
        rotated = 0
        while num > 0:
            digit = num % 10
            if digit not in mapping:
                return False
            rotated = rotated * 10 + mapping[digit]
            num //= 10
        return rotated != original
    
    def backtrack(current: int, position: int) -> int:
        if current > n:
            return 0
        count = 0
        if is_confusing(current):
            count += 1
        for digit in [0, 1, 6, 8, 9]:
            if current == 0 and digit == 0:
                continue
            next_num = current * 10 + digit
            count += backtrack(next_num, position + 1)
        return count
    
    return backtrack(0, 0)


Solution = create_solution(confusingNumberII)