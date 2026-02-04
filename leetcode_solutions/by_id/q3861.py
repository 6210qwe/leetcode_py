# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3861
标题: Minimum Threshold for Inversion Pairs Count
难度: medium
链接: https://leetcode.cn/problems/minimum-threshold-for-inversion-pairs-count/
题目类型: 树状数组、线段树、数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3520. 逆序对计数的最小阈值 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用树状数组（Fenwick Tree）来高效计算逆序对，并结合二分查找来找到最小阈值。

算法步骤:
1. 定义一个树状数组类，用于维护前缀和并支持快速更新和查询。
2. 对数组进行离散化处理，将元素映射到较小的范围，以便于使用树状数组。
3. 使用二分查找来确定最小阈值，每次检查当前阈值下的逆序对数量是否满足条件。
4. 在每次检查中，使用树状数组来计算逆序对的数量。

关键点:
- 树状数组可以高效地进行区间和的查询和单点更新。
- 二分查找可以快速缩小搜索范围，找到最小阈值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.size:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res


def count_inversions(nums, threshold):
    n = len(nums)
    sorted_nums = sorted(set(nums))
    rank = {num: i + 1 for i, num in enumerate(sorted_nums)}
    fenwick_tree = FenwickTree(n)
    inv_count = 0

    for i in range(n - 1, -1, -1):
        r = rank[nums[i]]
        inv_count += fenwick_tree.query(r - 1)
        if inv_count > threshold:
            return False
        fenwick_tree.update(r, 1)

    return True


def solution_function_name(nums: List[int], k: int) -> int:
    """
    函数式接口 - 实现
    """
    left, right = 0, len(nums) * (len(nums) - 1) // 2

    while left < right:
        mid = (left + right) // 2
        if count_inversions(nums, mid):
            right = mid
        else:
            left = mid + 1

    return left


Solution = create_solution(solution_function_name)