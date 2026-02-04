# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 512
标题: Maximum Alternating Subarray Sum
难度: medium
链接: https://leetcode.cn/problems/maximum-alternating-subarray-sum/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2036. 最大交替子数组和 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们维护两个变量 `even` 和 `odd`，分别表示以偶数下标和奇数下标结尾的最大交替子数组和。

算法步骤:
1. 初始化 `even` 和 `odd` 为第一个元素的值。
2. 遍历数组，从第二个元素开始：
   - 如果当前下标是偶数，则更新 `even` 为 `max(even + nums[i], nums[i])`。
   - 如果当前下标是奇数，则更新 `odd` 为 `max(odd + nums[i], even - nums[i])`。
3. 最后返回 `max(even, odd)`。

关键点:
- 通过维护两个变量来避免使用额外的空间。
- 动态规划的状态转移方程确保了每一步都取到最大值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度，因为我们需要遍历整个数组一次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_alternating_subarray_sum(nums: List[int]) -> int:
    """
    函数式接口 - 计算最大交替子数组和
    """
    if not nums:
        return 0

    even = odd = nums[0]

    for i in range(1, len(nums)):
        if i % 2 == 0:
            even = max(even + nums[i], nums[i])
        else:
            odd = max(odd + nums[i], even - nums[i])

    return max(even, odd)


Solution = create_solution(max_alternating_subarray_sum)