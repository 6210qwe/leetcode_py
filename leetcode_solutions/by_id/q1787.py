# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1787
标题: Sum of Absolute Differences in a Sorted Array
难度: medium
链接: https://leetcode.cn/problems/sum-of-absolute-differences-in-a-sorted-array/
题目类型: 数组、数学、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1685. 有序数组中差绝对值之和 - 给你一个 非递减 有序整数数组 nums 。 请你建立并返回一个整数数组 result，它跟 nums 长度相同，且result[i] 等于 nums[i] 与数组中所有其他元素差的绝对值之和。 换句话说， result[i] 等于 sum(|nums[i]-nums[j]|) ，其中 0 <= j < nums.length 且 j != i （下标从 0 开始）。 示例 1： 输入：nums = [2,3,5] 输出：[4,3,5] 解释：假设数组下标从 0 开始，那么 result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4， result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3， result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5。 示例 2： 输入：nums = [1,4,6,8,10] 输出：[24,15,13,15,21] 提示： * 2 <= nums.length <= 105 * 1 <= nums[i] <= nums[i + 1] <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和来计算每个位置的绝对差值之和。

算法步骤:
1. 计算数组的前缀和。
2. 对于每个位置 i，使用前缀和公式计算 result[i]：
   - 左侧部分: (i * nums[i] - prefix_sum[i])
   - 右侧部分: (prefix_sum[-1] - prefix_sum[i] - (n - i - 1) * nums[i])
3. 将左侧部分和右侧部分相加得到 result[i]。

关键点:
- 前缀和的使用可以将时间复杂度降低到 O(n)。
- 通过前缀和公式避免了双重循环，提高了效率。
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


def solution_function_name(nums: List[int]) -> List[int]:
    """
    函数式接口 - 计算有序数组中差绝对值之和
    """
    n = len(nums)
    if n == 0:
        return []

    # 计算前缀和
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    # 计算结果数组
    result = [0] * n
    for i in range(n):
        left_part = (i * nums[i] - prefix_sum[i])
        right_part = (prefix_sum[-1] - prefix_sum[i] - (n - i - 1) * nums[i])
        result[i] = left_part + right_part

    return result


Solution = create_solution(solution_function_name)