# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1799
标题: Minimum Incompatibility
难度: hard
链接: https://leetcode.cn/problems/minimum-incompatibility/
题目类型: 位运算、数组、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1681. 最小不兼容性 - 给你一个整数数组 nums 和一个整数 k 。你需要将这个数组划分到 k 个相同大小的子集中，使得同一个子集里面没有两个相同的元素。 一个子集的 不兼容性 是该子集里面最大值和最小值的差。 请你返回将数组分成 k 个子集后，各子集 不兼容性 的 和 的 最小值 ，如果无法分成分成 k 个子集，返回 -1 。 子集的定义是数组中一些数字的集合，对数字顺序没有要求。 示例 1： 输入：nums = [1,2,1,4], k = 2 输出：4 解释：最优的分配是 [1,2] 和 [1,4] 。 不兼容性和为 (2-1) + (4-1) = 4 。 注意到 [1,1] 和 [2,4] 可以得到更小的和，但是第一个集合有 2 个相同的元素，所以不可行。 示例 2： 输入：nums = [6,3,8,1,3,1,2,2], k = 4 输出：6 解释：最优的子集分配为 [1,2]，[2,3]，[6,8] 和 [1,3] 。 不兼容性和为 (2-1) + (3-2) + (8-6) + (3-1) = 6 。 示例 3： 输入：nums = [5,3,3,6,3,3], k = 3 输出：-1 解释：没办法将这些数字分配到 3 个子集且满足每个子集里没有相同数字。 提示： * 1 <= k <= nums.length <= 16 * nums.length 能被 k 整除。 * 1 <= nums[i] <= nums.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 状态压缩DP，枚举所有可能的子集

算法步骤:
1. 预处理所有有效的子集（无重复元素）
2. 使用DP[mask]表示选择mask状态下的最小不兼容性和
3. 枚举所有可能的子集组合

关键点:
- 状态压缩DP
- 子集枚举
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(3^n) - n为数组长度
空间复杂度: O(2^n) - DP数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_incompatibility(nums: List[int], k: int) -> int:
    """
    函数式接口 - 最小不兼容性
    
    实现思路:
    状态压缩DP：枚举所有可能的子集。
    
    Args:
        nums: 整数数组
        k: 子集数量
        
    Returns:
        最小不兼容性和，如果无法分配返回-1
        
    Example:
        >>> minimum_incompatibility([1,2,1,4], 2)
        4
    """
    n = len(nums)
    size = n // k
    
    # 预处理所有有效的子集
    valid_subsets = {}
    
    for mask in range(1, 1 << n):
        if bin(mask).count('1') != size:
            continue
        
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        
        # 检查是否有重复元素
        if len(subset) != len(set(subset)):
            continue
        
        subset.sort()
        incompatibility = subset[-1] - subset[0]
        valid_subsets[mask] = incompatibility
    
    # DP
    dp = [float('inf')] * (1 << n)
    dp[0] = 0
    
    for mask in range(1 << n):
        if dp[mask] == float('inf'):
            continue
        
        # 找到未使用的元素
        unused = []
        for i in range(n):
            if not (mask & (1 << i)):
                unused.append(i)
        
        # 枚举所有可能的子集
        for subset_mask, incompatibility in valid_subsets.items():
            # 检查子集是否完全由未使用的元素组成
            if (mask & subset_mask) == 0:
                new_mask = mask | subset_mask
                dp[new_mask] = min(dp[new_mask], dp[mask] + incompatibility)
    
    return dp[(1 << n) - 1] if dp[(1 << n) - 1] != float('inf') else -1


Solution = create_solution(minimum_incompatibility)
