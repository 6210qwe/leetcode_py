# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4155
标题: Maximum Number of Equal Length Runs
难度: medium
链接: https://leetcode.cn/problems/maximum-number-of-equal-length-runs/
题目类型: 哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3773. 最大等长连续字符组 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表来统计每个字符的最长连续子串，并找到最大等长连续字符组。

算法步骤:
1. 初始化一个哈希表 `count` 来记录每个字符的最长连续子串长度。
2. 使用滑动窗口遍历字符串，记录每个字符的连续长度。
3. 更新哈希表 `count` 中每个字符的最大连续长度。
4. 遍历哈希表 `count`，找到最大等长连续字符组的数量。

关键点:
- 使用滑动窗口来统计每个字符的最长连续子串。
- 使用哈希表来记录每个字符的最大连续长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)（因为字符集是固定的，最多有 26 个字母）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(s: str) -> int:
    """
    函数式接口 - 实现最优解法
    """
    if not s:
        return 0

    n = len(s)
    max_length = 1
    current_length = 1
    count = {}

    for i in range(1, n):
        if s[i] == s[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            count[current_length] = count.get(current_length, 0) + 1
            current_length = 1

    # 处理最后一个连续子串
    max_length = max(max_length, current_length)
    count[current_length] = count.get(current_length, 0) + 1

    # 找到最大等长连续字符组的数量
    return count[max_length]


Solution = create_solution(solution_function_name)