# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1849
标题: Maximum Absolute Sum of Any Subarray
难度: medium
链接: https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1749. 任意子数组和的绝对值的最大值 - 给你一个整数数组 nums 。一个子数组 [numsl, numsl+1, ..., numsr-1, numsr] 的 和的绝对值 为 abs(numsl + numsl+1 + ... + numsr-1 + numsr) 。 请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。 abs(x) 定义如下： * 如果 x 是负整数，那么 abs(x) = -x 。 * 如果 x 是非负整数，那么 abs(x) = x 。 示例 1： 输入：nums = [1,-3,2,3,-4] 输出：5 解释：子数组 [2,3] 和的绝对值最大，为 abs(2+3) = abs(5) = 5 。 示例 2： 输入：nums = [2,-5,1,-4,3,-2] 输出：8 解释：子数组 [-5,1,-4] 和的绝对值最大，为 abs(-5+1-4) = abs(-8) = 8 。 提示： * 1 <= nums.length <= 105 * -104 <= nums[i] <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和来计算子数组的和，并维护最大和最小的前缀和。

算法步骤:
1. 初始化前缀和 `prefix_sum` 为 0。
2. 初始化最大前缀和 `max_prefix` 和最小前缀和 `min_prefix` 为 0。
3. 遍历数组 `nums`，更新前缀和 `prefix_sum`。
4. 更新 `max_prefix` 和 `min_prefix`。
5. 计算最大绝对值 `max_abs` 为 `max_prefix - min_prefix`。

关键点:
- 前缀和可以帮助我们快速计算任意子数组的和。
- 通过维护最大和最小的前缀和，可以找到和的绝对值最大的子数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 `nums` 的长度。我们只需要遍历一次数组。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_absolute_sum(nums: List[int]) -> int:
    """
    函数式接口 - 计算数组中和的绝对值最大的子数组
    """
    prefix_sum = 0
    max_prefix = 0
    min_prefix = 0
    max_abs = 0
    
    for num in nums:
        prefix_sum += num
        max_prefix = max(max_prefix, prefix_sum)
        min_prefix = min(min_prefix, prefix_sum)
        max_abs = max(max_abs, max_prefix - min_prefix)
    
    return max_abs


Solution = create_solution(max_absolute_sum)