# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3177
标题: Minimizing Array After Replacing Pairs With Their Product
难度: medium
链接: https://leetcode.cn/problems/minimizing-array-after-replacing-pairs-with-their-product/
题目类型: 贪心、数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2892. 将相邻元素相乘后得到最小化数组 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i] 为将 nums[0:i+1] 中的任意两个相邻元素相乘后的最小值。通过递推关系，我们可以逐步计算出最终结果。

算法步骤:
1. 初始化一个长度为 n 的 dp 数组，dp[i] 表示将 nums[0:i+1] 中的任意两个相邻元素相乘后的最小值。
2. 设置 dp[0] = nums[0]，因为只有一个元素时，最小值就是它本身。
3. 对于每个 i 从 1 到 n-1，计算 dp[i] 的值。我们需要考虑两种情况：
   - 不合并 nums[i] 和 nums[i-1]，此时 dp[i] = dp[i-1] + nums[i]。
   - 合并 nums[i] 和 nums[i-1]，此时 dp[i] = min(dp[i-2] + nums[i] * nums[i-1], dp[i-1] + nums[i])。
4. 返回 dp[n-1] 作为最终结果。

关键点:
- 动态规划的状态转移方程是 dp[i] = min(dp[i-2] + nums[i] * nums[i-1], dp[i-1] + nums[i])。
- 通过维护一个 dp 数组，我们可以有效地计算出最小值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。我们需要遍历整个数组一次。
空间复杂度: O(n)，我们需要一个长度为 n 的 dp 数组来存储中间结果。
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
    函数式接口 - 实现将相邻元素相乘后得到最小化数组
    """
    n = len(nums)
    if n == 1:
        return nums[0]

    # 初始化 dp 数组
    dp = [float('inf')] * n
    dp[0] = nums[0]

    for i in range(1, n):
        # 不合并 nums[i] 和 nums[i-1]
        dp[i] = dp[i-1] + nums[i]
        if i > 1:
            # 合并 nums[i] 和 nums[i-1]
            dp[i] = min(dp[i], dp[i-2] + nums[i] * nums[i-1])

    return dp[n-1]


Solution = create_solution(solution_function_name)