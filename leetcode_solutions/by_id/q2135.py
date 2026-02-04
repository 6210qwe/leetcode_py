# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2135
标题: Maximum Number of Ways to Partition an Array
难度: hard
链接: https://leetcode.cn/problems/maximum-number-of-ways-to-partition-an-array/
题目类型: 数组、哈希表、计数、枚举、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2025. 分割数组的最多方案数 - 给你一个下标从 0 开始且长度为 n 的整数数组 nums 。分割 数组 nums 的方案数定义为符合以下两个条件的 pivot 数目： * 1 <= pivot < n * nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1] 同时给你一个整数 k 。你可以将 nums 中 一个 元素变为 k 或 不改变 数组。 请你返回在 至多 改变一个元素的前提下，最多 有多少种方法 分割 nums 使得上述两个条件都满足。 示例 1： 输入：nums = [2,-1,2], k = 3 输出：1 解释：一个最优的方案是将 nums[0] 改为 k 。数组变为 [3,-1,2] 。 有一种方法分割数组： - pivot = 2 ，我们有分割 [3,-1 | 2]：3 + -1 == 2 。 示例 2： 输入：nums = [0,0,0], k = 1 输出：2 解释：一个最优的方案是不改动数组。 有两种方法分割数组： - pivot = 1 ，我们有分割 [0 | 0,0]：0 == 0 + 0 。 - pivot = 2 ，我们有分割 [0,0 | 0]: 0 + 0 == 0 。 示例 3： 输入：nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33 输出：4 解释：一个最优的方案是将 nums[2] 改为 k 。数组变为 [22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14] 。 有四种方法分割数组。 提示： * n == nums.length * 2 <= n <= 105 * -105 <= k, nums[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和和哈希表来记录每个前缀和出现的位置，并通过枚举每个位置的变化来计算最大分割方案数。

算法步骤:
1. 计算数组的前缀和。
2. 使用哈希表记录每个前缀和出现的位置。
3. 枚举每个位置的变化，计算新的前缀和，并更新最大分割方案数。

关键点:
- 使用前缀和可以快速计算任意子数组的和。
- 使用哈希表记录前缀和的位置，可以快速查找和更新分割方案数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_ways_to_partition(nums: List[int], k: int) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    total_sum = prefix_sum[-1]
    left_diff_count = {}
    right_diff_count = {}
    
    # 记录左边的差值
    for i in range(1, n):
        diff = prefix_sum[i] - (total_sum - prefix_sum[i])
        if diff not in left_diff_count:
            left_diff_count[diff] = 0
        left_diff_count[diff] += 1
    
    # 初始的最大分割方案数
    max_ways = left_diff_count.get(0, 0)
    
    # 枚举每个位置的变化
    for i in range(n):
        new_val = k
        old_val = nums[i]
        diff = new_val - old_val
        
        # 更新左边的差值
        for d, count in left_diff_count.items():
            new_d = d - diff
            if new_d not in right_diff_count:
                right_diff_count[new_d] = 0
            right_diff_count[new_d] += count
            left_diff_count[d] -= count
            if left_diff_count[d] == 0:
                del left_diff_count[d]
        
        # 更新右边的差值
        for j in range(i + 1, n):
            diff = prefix_sum[j] - (total_sum - prefix_sum[j])
            if diff not in right_diff_count:
                right_diff_count[diff] = 0
            right_diff_count[diff] += 1
        
        # 更新最大分割方案数
        max_ways = max(max_ways, right_diff_count.get(0, 0))
        
        # 清空右边的差值
        right_diff_count.clear()
    
    return max_ways


Solution = create_solution(max_ways_to_partition)