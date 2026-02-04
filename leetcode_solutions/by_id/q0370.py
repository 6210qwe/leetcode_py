# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 370
标题: Range Addition
难度: medium
链接: https://leetcode.cn/problems/range-addition/
题目类型: 数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
370. 区间加法 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 差分数组 + 前缀和，高效处理多次区间加法。

算法步骤:
1. 创建长度为 length+1 的差分数组 diff，初始全为 0。
2. 对于每个操作 [start, end, val]：执行 `diff[start] += val`，若 end+1 在范围内，则执行 `diff[end+1] -= val`。
3. 最后对 diff 做前缀和，前 length 个位置即为答案数组。

关键点:
- 通过差分思想，将对区间的加法转化为对两个端点的 O(1) 更新。
- 所有操作处理完后，再一次性线性扫描恢复结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(length + m)，m 为更新操作数，每个操作 O(1)，最终一次前缀和 O(length)。
空间复杂度: O(length)，用于存储差分数组和结果数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def range_addition(length: int, updates: List[List[int]]) -> List[int]:
    """
    区间加法：多次对闭区间 [start, end] 加 val，返回最终数组。

    使用差分数组：对 diff[start]+=val，diff[end+1]-=val，最后前缀和恢复原数组。
    """
    diff = [0] * (length + 1)
    for start, end, val in updates:
        diff[start] += val
        if end + 1 < len(diff):
            diff[end + 1] -= val
    res = [0] * length
    cur = 0
    for i in range(length):
        cur += diff[i]
        res[i] = cur
    return res


# 自动生成Solution类（无需手动编写）
Solution = create_solution(range_addition)
