# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3431
标题: Find the Minimum Cost Array Permutation
难度: hard
链接: https://leetcode.cn/problems/find-the-minimum-cost-array-permutation/
题目类型: 位运算、数组、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3149. 找出分数最低的排列 - 给你一个数组 nums ，它是 [0, 1, 2, ..., n - 1] 的一个排列 。对于任意一个 [0, 1, 2, ..., n - 1] 的排列 perm ，其 分数 定义为： score(perm) = |perm[0] - nums[perm[1]]| + |perm[1] - nums[perm[2]]| + ... + |perm[n - 1] - nums[perm[0]]| 返回具有 最低 分数的排列 perm 。如果存在多个满足题意且分数相等的排列，则返回其中字典序最小的一个。 示例 1： 输入：nums = [1,0,2] 输出：[0,1,2] 解释： [https://assets.leetcode.com/uploads/2024/04/04/example0gif.gif] 字典序最小且分数最低的排列是 [0,1,2]。这个排列的分数是 |0 - 0| + |1 - 2| + |2 - 1| = 2 。 示例 2： 输入：nums = [0,2,1] 输出：[0,2,1] 解释： [https://assets.leetcode.com/uploads/2024/04/04/example1gif.gif] 字典序最小且分数最低的排列是 [0,2,1]。这个排列的分数是 |0 - 1| + |2 - 2| + |1 - 0| = 2 。 提示： * 2 <= n == nums.length <= 14 * nums 是 [0, 1, 2, ..., n - 1] 的一个排列。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和状态压缩来找到最低分数的排列。

算法步骤:
1. 初始化一个三维 DP 数组 dp，其中 dp[mask][i][j] 表示当前状态 mask 下，以 i 结尾且下一个元素为 j 的最小分数。
2. 遍历所有可能的状态 mask，并更新 DP 数组。
3. 从 DP 数组中回溯得到最终的排列。

关键点:
- 使用状态压缩表示当前选择的元素集合。
- 动态规划递推公式：dp[mask][i][j] = min(dp[mask ^ (1 << j)][k][i] + abs(nums[i] - k))，其中 k 是前一个元素。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * 2^n)，其中 n 是 nums 的长度。因为有 2^n 个状态，每个状态需要 O(n^2) 的时间来更新。
空间复杂度: O(n^2 * 2^n)，用于存储 DP 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_min_cost_permutation(nums: List[int]) -> List[int]:
    n = len(nums)
    max_mask = 1 << n
    dp = [[[float('inf')] * n for _ in range(n)] for _ in range(max_mask)]
    
    # Initialize base cases
    for i in range(n):
        dp[1 << i][i][i] = 0
    
    # Fill DP table
    for mask in range(1, max_mask):
        for i in range(n):
            if mask & (1 << i) == 0:
                continue
            for j in range(n):
                if mask & (1 << j) == 0:
                    prev_mask = mask ^ (1 << i)
                    for k in range(n):
                        if prev_mask & (1 << k):
                            dp[mask][i][j] = min(dp[mask][i][j], dp[prev_mask][k][i] + abs(nums[i] - k))
    
    # Reconstruct the permutation
    min_score = float('inf')
    best_perm = []
    for i in range(n):
        for j in range(n):
            if dp[max_mask - 1][i][j] < min_score:
                min_score = dp[max_mask - 1][i][j]
                best_perm = [i, j]
    
    for step in range(n - 2, 0, -1):
        for i in range(n):
            for j in range(n):
                if dp[(max_mask - 1) ^ (1 << best_perm[step + 1])][i][best_perm[step + 1]] + abs(nums[best_perm[step + 1]] - i) == min_score:
                    best_perm.insert(step + 1, i)
                    break
    
    return best_perm


Solution = create_solution(find_min_cost_permutation)