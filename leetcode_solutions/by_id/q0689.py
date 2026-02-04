# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 689
标题: Maximum Sum of 3 Non-Overlapping Subarrays
难度: hard
链接: https://leetcode.cn/problems/maximum-sum-of-3-non-overlapping-subarrays/
题目类型: 数组、动态规划、前缀和、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
689. 三个无重叠子数组的最大和 - 给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且全部数字和最大的子数组，并返回这三个子数组。 以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。 示例 1： 输入：nums = [1,2,1,2,6,7,5,1], k = 2 输出：[0,3,5] 解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。 也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。 示例 2： 输入：nums = [1,2,1,2,1,2,1,2,1], k = 2 输出：[0,2,4] 提示： * 1 <= nums.length <= 2 * 104 * 1 <= nums[i] < 216 * 1 <= k <= floor(nums.length / 3)
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和动态规划来找到三个无重叠子数组的最大和。

算法步骤:
1. 计算每个长度为 k 的子数组的和。
2. 使用动态规划计算从左到右和从右到左的最优解。
3. 结合左右两个方向的最优解，找到三个无重叠子数组的最大和及其起始位置。

关键点:
- 使用滑动窗口计算子数组和。
- 动态规划记录从左到右和从右到左的最优解。
- 结合左右最优解找到最终结果。
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


def max_sum_of_three_subarrays(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    subarray_sums = [sum(nums[i:i + k]) for i in range(n - k + 1)]
    
    # 从左到右的动态规划
    left_dp = [0] * (n - k + 1)
    left_pos = [0] * (n - k + 1)
    max_sum = 0
    for i in range(n - k + 1):
        if subarray_sums[i] > max_sum:
            max_sum = subarray_sums[i]
            left_pos[i] = i
        else:
            left_pos[i] = left_pos[i - 1]
        left_dp[i] = max_sum
    
    # 从右到左的动态规划
    right_dp = [0] * (n - k + 1)
    right_pos = [n - k] * (n - k + 1)
    max_sum = 0
    for i in range(n - k, -1, -1):
        if subarray_sums[i] >= max_sum:
            max_sum = subarray_sums[i]
            right_pos[i] = i
        else:
            right_pos[i] = right_pos[i + 1]
        right_dp[i] = max_sum
    
    # 找到三个无重叠子数组的最大和及其起始位置
    max_total = 0
    result = [0, 0, 0]
    for j in range(k, n - 2 * k + 1):
        total = left_dp[j - k] + subarray_sums[j] + right_dp[j + k]
        if total > max_total:
            max_total = total
            result = [left_pos[j - k], j, right_pos[j + k]]
    
    return result


Solution = create_solution(max_sum_of_three_subarrays)