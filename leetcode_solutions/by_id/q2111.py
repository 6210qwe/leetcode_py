# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2111
标题: Binary Searchable Numbers in an Unsorted Array
难度: medium
链接: https://leetcode.cn/problems/binary-searchable-numbers-in-an-unsorted-array/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1966. 未排序数组中的可被二分搜索的数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过从左到右和从右到左两次遍历数组，分别找到每个位置的最大值和最小值。然后判断每个元素是否满足二分查找的条件。

算法步骤:
1. 从左到右遍历数组，记录每个位置左侧的最大值。
2. 从右到左遍历数组，记录每个位置右侧的最小值。
3. 再次遍历数组，判断每个元素是否满足二分查找的条件：即该元素大于其左侧的最大值且小于其右侧的最小值。

关键点:
- 通过两次遍历分别记录左侧最大值和右侧最小值，避免了嵌套循环，提高了效率。
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


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 计算未排序数组中可被二分搜索的数的数量
    """
    n = len(nums)
    if n == 0:
        return 0

    # 从左到右遍历，记录每个位置左侧的最大值
    left_max = [float('-inf')] * n
    max_val = float('-inf')
    for i in range(n):
        left_max[i] = max_val
        max_val = max(max_val, nums[i])

    # 从右到左遍历，记录每个位置右侧的最小值
    right_min = [float('inf')] * n
    min_val = float('inf')
    for i in range(n - 1, -1, -1):
        right_min[i] = min_val
        min_val = min(min_val, nums[i])

    # 判断每个元素是否满足二分查找的条件
    count = 0
    for i in range(n):
        if left_max[i] < nums[i] < right_min[i]:
            count += 1

    return count


Solution = create_solution(solution_function_name)