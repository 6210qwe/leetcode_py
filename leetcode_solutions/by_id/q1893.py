# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1893
标题: Maximum Subarray Sum After One Operation
难度: medium
链接: https://leetcode.cn/problems/maximum-subarray-sum-after-one-operation/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1746. 经过一次操作后的最大子数组和 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们维护两个状态：
- `dp_max`：表示以当前元素结尾的最大子数组和。
- `dp_min`：表示以当前元素结尾的最小子数组和。

算法步骤:
1. 初始化 `dp_max` 和 `dp_min` 为第一个元素的值。
2. 遍历数组，对于每个元素，更新 `dp_max` 和 `dp_min`。
3. 计算当前元素变为负数后的最大子数组和，并更新全局最大值。

关键点:
- 通过维护 `dp_max` 和 `dp_min`，我们可以有效地计算出经过一次操作后的最大子数组和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度，因为我们需要遍历整个数组一次。
空间复杂度: O(1)，因为我们只使用了常数级的额外空间。
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
    函数式接口 - 实现最优解法
    """
    if not nums:
        return 0

    n = len(nums)
    if n == 1:
        return -nums[0]

    dp_max = dp_min = res = nums[0]

    for i in range(1, n):
        # 更新 dp_max 和 dp_min
        dp_max = max(nums[i], dp_max + nums[i])
        dp_min = min(nums[i], dp_min + nums[i])

        # 计算当前元素变为负数后的最大子数组和
        res = max(res, dp_max, -dp_min + 2 * nums[i])

    return res


Solution = create_solution(solution_function_name)