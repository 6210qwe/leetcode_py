# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2719
标题: Beautiful Pairs
难度: hard
链接: https://leetcode.cn/problems/beautiful-pairs/
题目类型: 几何、数组、数学、分治、有序集合、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2613. 美数对 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表统计每个元素的出现次数，然后遍历另一个数组，计算可以形成的美丽对数。

算法步骤:
1. 使用一个哈希表 `countA` 统计数组 A 中每个元素的出现次数。
2. 初始化美丽对数 `beautiful_pairs` 为 0。
3. 遍历数组 B，对于每个元素 b：
   - 如果 `b` 在 `countA` 中且 `countA[b] > 0`，则增加 `beautiful_pairs`，并将 `countA[b]` 减 1。
4. 最后，如果 `beautiful_pairs` 等于数组 A 的长度，则返回 `beautiful_pairs - 1`，否则返回 `beautiful_pairs + 1`。

关键点:
- 使用哈希表来统计元素出现次数，可以在 O(1) 时间内检查和更新。
- 最后一步的判断是为了确保我们总是返回一个最优解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(A: List[int], B: List[int]) -> int:
    """
    函数式接口 - 计算美丽对数
    """
    countA = {}
    for a in A:
        if a in countA:
            countA[a] += 1
        else:
            countA[a] = 1

    beautiful_pairs = 0
    for b in B:
        if b in countA and countA[b] > 0:
            beautiful_pairs += 1
            countA[b] -= 1

    if beautiful_pairs == len(A):
        return beautiful_pairs - 1
    else:
        return beautiful_pairs + 1


Solution = create_solution(solution_function_name)