# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3047
标题: Maximum Element-Sum of a Complete Subset of Indices
难度: hard
链接: https://leetcode.cn/problems/maximum-element-sum-of-a-complete-subset-of-indices/
题目类型: 数组、数学、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2862. 完全子集的最大元素和 - 给你一个下标从 1 开始、由 n 个整数组成的数组。你需要从 nums 选择一个 完全集，其中每对元素下标的乘积都是一个 完全平方数，例如选择 ai 和 aj ，i * j 一定是完全平方数。 返回 完全子集 所能取到的 最大元素和 。 示例 1： 输入：nums = [8,7,3,5,7,2,4,9] 输出：16 解释： 我们选择下标为 2 和 8 的元素，并且 2 * 8 是一个完全平方数。 示例 2： 输入：nums = [8,10,3,8,1,13,7,9,4] 输出：20 解释： 我们选择下标为 1, 4, 9 的元素。1 * 4, 1 * 9, 4 * 9 是完全平方数。 提示： * 1 <= n == nums.length <= 104 * 1 <= nums[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过分解每个下标的质因数并分组，找到所有符合条件的下标集合，然后计算这些集合中元素的最大和。

算法步骤:
1. 分解每个下标的质因数。
2. 将具有相同质因数的下标分组。
3. 计算每个组中元素的和，并返回最大值。

关键点:
- 使用质因数分解来确定哪些下标可以组成完全平方数。
- 通过哈希表来存储和查找具有相同质因数的下标。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * sqrt(n))，其中 n 是数组的长度。分解每个下标的质因数需要 O(sqrt(n)) 的时间。
空间复杂度: O(n)，用于存储质因数分组和结果。
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
    函数式接口 - 实现
    """
    def get_prime_factors(index: int) -> int:
        """获取下标的质因数乘积（去重）"""
        factors = set()
        while index % 2 == 0:
            factors.add(2)
            index //= 2
        for i in range(3, int(index**0.5) + 1, 2):
            while index % i == 0:
                factors.add(i)
                index //= i
        if index > 2:
            factors.add(index)
        return tuple(sorted(factors))

    n = len(nums)
    factor_to_sum = {}
    for i in range(1, n + 1):
        factors = get_prime_factors(i)
        if factors not in factor_to_sum:
            factor_to_sum[factors] = 0
        factor_to_sum[factors] += nums[i - 1]

    return max(factor_to_sum.values())


Solution = create_solution(solution_function_name)