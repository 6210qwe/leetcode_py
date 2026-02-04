# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 698
标题: Partition to K Equal Sum Subsets
难度: medium
链接: https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/
题目类型: 位运算、记忆化搜索、数组、动态规划、回溯、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
698. 划分为k个相等的子集 - 给定一个整数数组 nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。 示例 1： 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4 输出： True 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。 示例 2: 输入: nums = [1,2,3,4], k = 3 输出: false 提示： * 1 <= k <= len(nums) <= 16 * 0 < nums[i] < 10000 * 每个元素的频率在 [1,4] 范围内
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）和记忆化搜索来尝试将数组划分为 k 个子集，每个子集的和相等。

算法步骤:
1. 计算总和 sum(nums)，如果 sum(nums) 不能被 k 整除，则直接返回 False。
2. 对数组进行降序排序，以便更快地找到解。
3. 使用 DFS 和记忆化搜索来尝试将数组划分为 k 个子集。
4. 在每次递归调用中，尝试将当前数字放入某个子集中，并检查是否可以继续划分。

关键点:
- 使用记忆化搜索来避免重复计算。
- 通过降序排序来加速搜索过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(k^n)，其中 n 是数组的长度。虽然最坏情况下是指数级的，但通过记忆化搜索可以大大减少不必要的计算。
空间复杂度: O(n)，用于存储递归调用栈和记忆化搜索的状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def can_partition_k_subsets(nums: List[int], k: int) -> bool:
    total_sum = sum(nums)
    if total_sum % k != 0:
        return False
    target = total_sum // k
    nums.sort(reverse=True)
    used = [False] * len(nums)
    
    @lru_cache(None)
    def dfs(start, k, current_sum):
        if k == 0:
            return True
        if current_sum == target:
            return dfs(0, k - 1, 0)
        for i in range(start, len(nums)):
            if not used[i] and current_sum + nums[i] <= target:
                used[i] = True
                if dfs(i + 1, k, current_sum + nums[i]):
                    return True
                used[i] = False
        return False
    
    return dfs(0, k, 0)

Solution = create_solution(can_partition_k_subsets)