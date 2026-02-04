# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2258
标题: Elements in Array After Removing and Replacing Elements
难度: medium
链接: https://leetcode.cn/problems/elements-in-array-after-removing-and-replacing-elements/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一个整数数组 nums 和两个整数 k 和 threshold。你可以在数组中进行以下操作任意次：
1. 选择数组中的任意一个元素 x，将它移除。
2. 将值为 x + 1 的元素添加到数组中。

你的目标是使数组中所有元素的和至少为 threshold。返回数组中可能的最小元素数量。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，优先处理较大的元素，以减少需要添加的元素数量。

算法步骤:
1. 计算当前数组的总和。
2. 如果当前总和已经大于等于 threshold，则直接返回数组长度。
3. 否则，从大到小遍历数组中的元素，计算需要添加的元素数量，直到总和达到或超过 threshold。

关键点:
- 优先处理较大的元素，可以减少需要添加的元素数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数组的长度。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], k: int, threshold: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    # 计算当前数组的总和
    current_sum = sum(nums)
    
    # 如果当前总和已经大于等于 threshold，则直接返回数组长度
    if current_sum >= threshold:
        return len(nums)
    
    # 从大到小遍历数组中的元素
    nums.sort(reverse=True)
    
    # 计算需要添加的元素数量
    for i, num in enumerate(nums):
        while current_sum < threshold and num + k > nums[0]:
            current_sum += k
            num += k
        if current_sum >= threshold:
            return i + 1
    
    return len(nums)


Solution = create_solution(solution_function_name)