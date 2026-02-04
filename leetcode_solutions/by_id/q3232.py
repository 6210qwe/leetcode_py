# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3232
标题: Maximum GCD-Sum of a Subarray
难度: hard
链接: https://leetcode.cn/problems/maximum-gcd-sum-of-a-subarray/
题目类型: 数组、数学、二分查找、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2941. 子数组的最大 GCD-Sum - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和与最大公因数 (GCD) 的性质来计算子数组的最大 GCD-Sum。

算法步骤:
1. 计算每个元素的前缀和，并存储在数组 `prefix_sum` 中。
2. 使用一个字典 `gcd_map` 来存储每个 GCD 值对应的前缀和的最大值。
3. 遍历数组，对于每个元素，计算其与前面所有元素的最大 GCD，并更新 `gcd_map`。
4. 最后，从 `gcd_map` 中找到最大的 GCD-Sum。

关键点:
- 使用前缀和可以快速计算任意子数组的和。
- 使用 GCD 的性质来优化计算过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * log(max(nums)))，其中 n 是数组长度，max(nums) 是数组中的最大值。
空间复杂度: O(n)，用于存储前缀和和 GCD 映射。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import math

def maxGCDSubarraySum(nums: List[int]) -> int:
    """
    函数式接口 - 计算子数组的最大 GCD-Sum
    """
    n = len(nums)
    if n == 0:
        return 0

    # 计算前缀和
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

    # 用于存储每个 GCD 值对应的前缀和的最大值
    gcd_map = {}

    max_gcd_sum = 0
    for i in range(n):
        for j in range(i, n):
            current_gcd = math.gcd(*nums[i:j+1])
            current_sum = prefix_sum[j + 1] - prefix_sum[i]
            if current_gcd not in gcd_map:
                gcd_map[current_gcd] = current_sum
            else:
                gcd_map[current_gcd] = max(gcd_map[current_gcd], current_sum)
            max_gcd_sum = max(max_gcd_sum, gcd_map[current_gcd])

    return max_gcd_sum

Solution = create_solution(maxGCDSubarraySum)