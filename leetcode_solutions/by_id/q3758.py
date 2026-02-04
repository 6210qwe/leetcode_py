# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3758
标题: Minimum Unlocked Indices to Sort Nums
难度: medium
链接: https://leetcode.cn/problems/minimum-unlocked-indices-to-sort-nums/
题目类型: 数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3431. 对数字排序的最小解锁下标 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法找到需要解锁的最小下标集合。

算法步骤:
1. 创建一个数组 `sorted_nums`，它是 `nums` 的排序版本。
2. 初始化两个指针 `i` 和 `j`，分别指向 `nums` 和 `sorted_nums` 的起始位置。
3. 遍历 `nums`，如果 `nums[i]` 不等于 `sorted_nums[j]`，则将 `i` 添加到结果集中，并移动 `j` 指针。
4. 如果 `nums[i]` 等于 `sorted_nums[j]`，则同时移动 `i` 和 `j` 指针。
5. 返回结果集。

关键点:
- 通过比较 `nums` 和 `sorted_nums`，找到需要解锁的最小下标集合。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 `nums` 的长度。排序操作的时间复杂度为 O(n log n)，遍历操作为 O(n)。
空间复杂度: O(n)，用于存储排序后的数组和结果集。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_unlocked_indices(nums: List[int]) -> List[int]:
    """
    函数式接口 - 找到对数字排序的最小解锁下标
    """
    n = len(nums)
    sorted_nums = sorted(nums)
    i, j = 0, 0
    unlocked_indices = []

    while i < n and j < n:
        if nums[i] != sorted_nums[j]:
            unlocked_indices.append(i)
            j += 1
        else:
            i += 1
            j += 1

    return unlocked_indices


Solution = create_solution(minimum_unlocked_indices)