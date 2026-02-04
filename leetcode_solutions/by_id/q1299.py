# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1299
标题: K-Concatenation Maximum Sum
难度: medium
链接: https://leetcode.cn/problems/k-concatenation-maximum-sum/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1191. K 次串联后最大子数组之和 - 给定一个整数数组 arr 和一个整数 k ，通过重复 k 次来修改数组。 例如，如果 arr = [1, 2] ， k = 3 ，那么修改后的数组将是 [1, 2, 1, 2, 1, 2] 。 返回修改后的数组中的最大的子数组之和。注意，子数组长度可以是 0，在这种情况下它的总和也是 0。 由于 结果可能会很大，需要返回的 109 + 7 的 模 。 示例 1： 输入：arr = [1,2], k = 3 输出：9 示例 2： 输入：arr = [1,-2,1], k = 5 输出：2 示例 3： 输入：arr = [-1,-2], k = 7 输出：0 提示： * 1 <= arr.length <= 105 * 1 <= k <= 105 * -104 <= arr[i] <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Kadane 算法计算单个数组的最大子数组和，并根据 k 的值进行扩展。

算法步骤:
1. 计算单个数组的最大子数组和。
2. 如果 k > 1，计算两个数组拼接后的最大子数组和。
3. 根据 k 的值和数组总和，计算最终结果。

关键点:
- 使用 Kadane 算法计算最大子数组和。
- 处理 k > 1 的情况，考虑多次拼接的影响。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def k_concatenation_max_sum(arr: List[int], k: int) -> int:
    """
    函数式接口 - 计算 K 次串联后最大子数组之和
    """
    MOD = 10**9 + 7
    n = len(arr)
    
    # Kadane's algorithm to find the maximum subarray sum for a single array
    def kadane(nums):
        max_ending_here = max_so_far = nums[0]
        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    
    # Calculate the maximum subarray sum for a single array
    max_single = kadane(arr)
    
    # If k == 1, return the result of a single array
    if k == 1:
        return max(0, max_single) % MOD
    
    # Calculate the maximum subarray sum for two concatenated arrays
    max_double = kadane(arr + arr)
    
    # Calculate the total sum of the array
    total_sum = sum(arr)
    
    # If total sum is positive, we can add (k-2) * total_sum to the result
    if total_sum > 0:
        return (max_double + (k - 2) * total_sum) % MOD
    else:
        return max(0, max_double) % MOD


Solution = create_solution(k_concatenation_max_sum)