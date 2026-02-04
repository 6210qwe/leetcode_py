# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3452
标题: Find the Maximum Length of a Good Subsequence II
难度: hard
链接: https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-ii/
题目类型: 数组、哈希表、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3177. 求出最长好子序列 II - 给你一个整数数组 nums 和一个 非负 整数 k 。如果一个整数序列 seq 满足在范围下标范围 [0, seq.length - 2] 中存在 不超过 k 个下标 i 满足 seq[i] != seq[i + 1] ，那么我们称这个整数序列为 好 序列。 请你返回 nums 中 好 子序列 的最长长度 示例 1： 输入：nums = [1,2,1,1,3], k = 2 输出：4 解释： 最长好子序列为 [1,2,1,1,3] 。 示例 2： 输入：nums = [1,2,3,4,5,1], k = 0 输出：2 解释： 最长好子序列为 [1,2,3,4,5,1] 。 提示： * 1 <= nums.length <= 5 * 103 * 1 <= nums[i] <= 109 * 0 <= k <= min(50, nums.length)
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和哈希表来记录每个元素的最长好子序列长度。

算法步骤:
1. 初始化一个字典 `dp`，用于存储每个元素在不同变化次数下的最长好子序列长度。
2. 遍历数组 `nums`，对于每个元素 `num`，更新 `dp` 字典。
3. 对于每个 `num`，遍历 `dp` 字典中的所有元素，更新当前 `num` 在不同变化次数下的最长好子序列长度。
4. 返回 `dp` 字典中所有元素的最大值。

关键点:
- 使用哈希表来存储每个元素在不同变化次数下的最长好子序列长度。
- 动态规划的思想，通过遍历数组和更新哈希表来找到最优解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * k)，其中 n 是数组 `nums` 的长度，k 是给定的非负整数。
空间复杂度: O(n * k)，用于存储哈希表 `dp`。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_max_good_subsequence_length(nums: List[int], k: int) -> int:
    """
    函数式接口 - 找到最长的好子序列长度
    """
    dp = {}
    max_length = 0
    
    for num in nums:
        new_dp = {num: 1}
        for key, length in dp.items():
            if key == num:
                new_dp[key] = max(new_dp.get(key, 0), length + 1)
            else:
                for changes in range(k + 1):
                    if (key, changes) in dp:
                        new_length = dp[(key, changes)] + 1
                        if changes < k:
                            new_dp[(num, changes + 1)] = max(new_dp.get((num, changes + 1), 0), new_length)
                        else:
                            new_dp[(num, k)] = max(new_dp.get((num, k), 0), new_length)
        
        dp = new_dp
        max_length = max(max_length, max(dp.values()))
    
    return max_length


Solution = create_solution(find_max_good_subsequence_length)