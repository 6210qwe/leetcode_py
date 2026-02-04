# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 681
标题: Next Closest Time
难度: medium
链接: https://leetcode.cn/problems/next-closest-time/
题目类型: 哈希表、字符串、回溯、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
681. 最近时刻 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 枚举所有可能的时间，并找到下一个最近的合法时间。

算法步骤:
1. 从给定的时间中提取出所有不同的数字。
2. 枚举所有可能的时间组合（4个位置，每个位置可以是这4个数字之一）。
3. 将这些时间组合转换为分钟数，并排序。
4. 找到当前时间在排序后的列表中的位置，并返回下一个时间。
5. 如果当前时间是最后一个，则返回第一个时间。

关键点:
- 使用集合来存储唯一的数字。
- 使用生成器表达式来生成所有可能的时间组合。
- 转换时间为分钟数以便于比较。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 因为时间组合的数量是固定的（最多4^4 = 256种）。
空间复杂度: O(1) - 使用常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def nextClosestTime(time: str) -> str:
    """
    函数式接口 - 返回给定时间的下一个最近合法时间
    """
    # 提取所有不同的数字
    digits = set(digit for digit in time if digit != ':')
    
    # 生成所有可能的时间组合
    def generate_times():
        for h1 in digits:
            for h2 in digits:
                for m1 in digits:
                    for m2 in digits:
                        candidate = f"{h1}{h2}:{m1}{m2}"
                        if "00:00" <= candidate < "24:00" and "00" <= candidate[3:] < "60":
                            yield candidate
    
    # 将时间转换为分钟数
    def to_minutes(t):
        return int(t[:2]) * 60 + int(t[3:])
    
    # 当前时间的分钟数
    current_minutes = to_minutes(time)
    
    # 找到下一个最近的时间
    for t in sorted(generate_times(), key=to_minutes):
        if to_minutes(t) > current_minutes:
            return t
    
    # 如果没有找到更大的时间，返回最小的时间
    return min(generate_times(), key=to_minutes)


Solution = create_solution(nextClosestTime)