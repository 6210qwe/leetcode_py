# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1805
标题: Minimum Adjacent Swaps for K Consecutive Ones
难度: hard
链接: https://leetcode.cn/problems/minimum-adjacent-swaps-for-k-consecutive-ones/
题目类型: 贪心、数组、前缀和、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1703. 得到连续 K 个 1 的最少相邻交换次数 - 给你一个整数数组 nums 和一个整数 k 。 nums 仅包含 0 和 1 。每一次移动，你可以选择 相邻 两个数字并将它们交换。 请你返回使 nums 中包含 k 个 连续 1 的 最少 交换次数。 示例 1： 输入：nums = [1,0,0,1,0,1], k = 2 输出：1 解释：在第一次操作时，nums 可以变成 [1,0,0,0,1,1] 得到连续两个 1 。 示例 2： 输入：nums = [1,0,0,0,0,0,1,1], k = 3 输出：5 解释：通过 5 次操作，最左边的 1 可以移到右边直到 nums 变为 [0,0,0,0,0,1,1,1] 。 示例 3： 输入：nums = [1,1,0,1], k = 2 输出：0 解释：nums 已经有连续 2 个 1 了。 提示： * 1 <= nums.length <= 105 * nums[i] 要么是 0 ，要么是 1 。 * 1 <= k <= sum(nums)
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 滑动窗口，找到k个1的最佳位置

算法步骤:
1. 收集所有1的位置
2. 使用滑动窗口找到k个连续1的最佳位置
3. 计算将1移到目标位置的最小交换次数

关键点:
- 滑动窗口
- 中位数位置最优
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n为数组长度
空间复杂度: O(n) - 存储1的位置
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_moves(nums: List[int], k: int) -> int:
    """
    函数式接口 - 得到连续 K 个 1 的最少相邻交换次数
    
    实现思路:
    滑动窗口：找到k个1的最佳位置。
    
    Args:
        nums: 整数数组
        k: 连续1的个数
        
    Returns:
        最少交换次数
        
    Example:
        >>> min_moves([1,0,0,1,0,1], 2)
        1
    """
    # 收集所有1的位置
    ones = [i for i, num in enumerate(nums) if num == 1]
    
    if len(ones) < k:
        return -1
    
    n = len(ones)
    # 前缀和
    prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + ones[i])
    
    result = float('inf')
    
    # 滑动窗口，窗口大小为k
    for i in range(n - k + 1):
        # 窗口内的1的位置
        window = ones[i:i+k]
        # 目标位置：中位数位置
        mid = i + k // 2
        target = ones[mid]
        
        # 计算交换次数
        moves = 0
        for j in range(i, i + k):
            moves += abs(ones[j] - (target - mid + j))
        
        result = min(result, moves)
    
    return result


Solution = create_solution(min_moves)
