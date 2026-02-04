# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3364
标题: Minimum Sum of Values by Dividing Array
难度: hard
链接: https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/
题目类型: 位运算、线段树、队列、数组、二分查找、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3117. 划分数组得到最小的值之和 - 给你两个数组 nums 和 andValues，长度分别为 n 和 m。 数组的 值 等于该数组的 最后一个 元素。 你需要将 nums 划分为 m 个 不相交的连续 子数组，对于第 ith 个子数组 [li, ri]，子数组元素的按位 AND 运算结果等于 andValues[i]，换句话说，对所有的 1 <= i <= m，nums[li] & nums[li + 1] & ... & nums[ri] == andValues[i] ，其中 & 表示按位 AND 运算符。 返回将 nums 划分为 m 个子数组所能得到的可能的 最小 子数组 值 之和。如果无法完成这样的划分，则返回 -1 。 示例 1： 输入： nums = [1,4,3,3,2], andValues = [0,3,3,2] 输出： 12 解释： 唯一可能的划分方法为： 1. [1,4] 因为 1 & 4 == 0 2. [3] 因为单元素子数组的按位 AND 结果就是该元素本身 3. [3] 因为单元素子数组的按位 AND 结果就是该元素本身 4. [2] 因为单元素子数组的按位 AND 结果就是该元素本身 这些子数组的值之和为 4 + 3 + 3 + 2 = 12 示例 2： 输入： nums = [2,3,5,7,7,7,5], andValues = [0,7,5] 输出： 17 解释： 划分 nums 的三种方式为： 1. [[2,3,5],[7,7,7],[5]] 其中子数组的值之和为 5 + 7 + 5 = 17 2. [[2,3,5,7],[7,7],[5]] 其中子数组的值之和为 7 + 7 + 5 = 19 3. [[2,3,5,7,7],[7],[5]] 其中子数组的值之和为 7 + 7 + 5 = 19 子数组值之和的最小可能值为 17 示例 3： 输入： nums = [1,2,3,4], andValues = [2] 输出： -1 解释： 整个数组 nums 的按位 AND 结果为 0。由于无法将 nums 划分为单个子数组使得元素的按位 AND 结果为 2，因此返回 -1。 提示： * 1 <= n == nums.length <= 104 * 1 <= m == andValues.length <= min(n, 10) * 1 <= nums[i] < 105 * 0 <= andValues[j] < 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i][j] 为将 nums 的前 i 个元素划分为 j 个子数组的最小值之和。通过遍历 nums 和 andValues 来更新 dp 数组。

算法步骤:
1. 初始化 dp 数组，dp[i][j] 表示将 nums 的前 i 个元素划分为 j 个子数组的最小值之和。
2. 遍历 nums 和 andValues，更新 dp 数组。
3. 检查 dp[n][m] 是否有效，如果有效则返回其值，否则返回 -1。

关键点:
- 动态规划的状态转移方程：dp[i][j] = min(dp[i][j], dp[k][j-1] + nums[i-1])，其中 k 是满足 nums[k:i] 的 AND 结果等于 andValues[j-1] 的最大索引。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * m)，其中 n 是 nums 的长度，m 是 andValues 的长度。
空间复杂度: O(n * m)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], andValues: List[int]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    n, m = len(nums), len(andValues)
    
    # 初始化 dp 数组
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    # 遍历 nums 和 andValues，更新 dp 数组
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            current_and = nums[i - 1]
            for k in range(i, 0, -1):
                current_and &= nums[k - 1]
                if current_and == andValues[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[k - 1][j - 1] + nums[i - 1])
    
    # 检查 dp[n][m] 是否有效
    return dp[n][m] if dp[n][m] != float('inf') else -1


Solution = create_solution(solution_function_name)