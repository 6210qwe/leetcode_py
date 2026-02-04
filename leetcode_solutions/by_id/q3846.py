# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3846
标题: Minimum Operations to Make Array Sum Divisible by K
难度: easy
链接: https://leetcode.cn/problems/minimum-operations-to-make-array-sum-divisible-by-k/
题目类型: 数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3512. 使数组和能被 K 整除的最少操作次数 - 给你一个整数数组 nums 和一个整数 k。你可以执行以下操作任意次： * 选择一个下标 i，并将 nums[i] 替换为 nums[i] - 1。 返回使数组元素之和能被 k 整除所需的最小操作次数。 示例 1： 输入： nums = [3,9,7], k = 5 输出： 4 解释： * 对 nums[1] = 9 执行 4 次操作。现在 nums = [3, 5, 7]。 * 数组之和为 15，可以被 5 整除。 示例 2： 输入： nums = [4,1,3], k = 4 输出： 0 解释： * 数组之和为 8，已经可以被 4 整除。因此不需要操作。 示例 3： 输入： nums = [3,2], k = 6 输出： 5 解释： * 对 nums[0] = 3 执行 3 次操作，对 nums[1] = 2 执行 2 次操作。现在 nums = [0, 0]。 * 数组之和为 0，可以被 6 整除。 提示： * 1 <= nums.length <= 1000 * 1 <= nums[i] <= 1000 * 1 <= k <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算数组和对 k 的余数，然后通过减少数组中的元素来消除这个余数。

算法步骤:
1. 计算数组和对 k 的余数。
2. 如果余数为 0，直接返回 0。
3. 否则，计算每个元素对 k 的余数，并统计这些余数的频率。
4. 通过减少数组中的元素来消除余数，找到最小的操作次数。

关键点:
- 使用哈希表统计每个余数的频率。
- 通过贪心算法找到最小的操作次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(k)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], k: int) -> int:
    """
    函数式接口 - 实现
    """
    # 计算数组和对 k 的余数
    total_sum = sum(nums)
    remainder = total_sum % k
    
    if remainder == 0:
        return 0
    
    # 统计每个元素对 k 的余数
    freq = [0] * k
    for num in nums:
        freq[num % k] += 1
    
    # 通过减少数组中的元素来消除余数
    operations = 0
    for i in range(1, k // 2 + 1):
        while freq[i] > 0 and freq[k - i] > 0:
            freq[i] -= 1
            freq[k - i] -= 1
            operations += 2
    
    # 处理中间的余数
    if k % 2 == 0 and freq[k // 2] > 0:
        operations += 1
    
    # 处理剩余的余数
    for i in range(1, k // 2 + 1):
        if freq[i] > 0:
            operations += min(freq[i], remainder // i)
    
    return operations


Solution = create_solution(solution_function_name)