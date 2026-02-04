# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3378
标题: Maximum Increasing Triplet Value
难度: medium
链接: https://leetcode.cn/problems/maximum-increasing-triplet-value/
题目类型: 数组、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3073. 最大递增三元组 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个数组分别记录从左到右和从右到左的最大值，然后遍历中间元素，找到满足条件的三元组。

算法步骤:
1. 初始化两个数组 left_max 和 right_max，分别记录从左到右和从右到左的最大值。
2. 从左到右遍历数组，填充 left_max 数组。
3. 从右到左遍历数组，填充 right_max 数组。
4. 再次遍历数组，对于每个中间元素，检查是否存在 left_max[i-1] < nums[i] < right_max[i+1]，并更新最大三元组值。

关键点:
- 使用两个辅助数组来记录左右最大值，从而在 O(n) 时间内完成查找。
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


def max_increasing_triplet_value(nums: List[int]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    n = len(nums)
    if n < 3:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    # 填充 left_max 数组
    left_max[0] = nums[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], nums[i])

    # 填充 right_max 数组
    right_max[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], nums[i])

    max_triplet_value = 0
    # 遍历中间元素
    for i in range(1, n - 1):
        if left_max[i - 1] < nums[i] < right_max[i + 1]:
            max_triplet_value = max(max_triplet_value, left_max[i - 1] * nums[i] * right_max[i + 1])

    return max_triplet_value


Solution = create_solution(max_increasing_triplet_value)