# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3622
标题: Maximum Frequency of an Element After Performing Operations I
难度: medium
链接: https://leetcode.cn/problems/maximum-frequency-of-an-element-after-performing-operations-i/
题目类型: 数组、二分查找、前缀和、排序、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3346. 执行操作后元素的最高频率 I - 给你一个整数数组 nums 和两个整数 k 和 numOperations 。 你必须对 nums 执行 操作 numOperations 次。每次操作中，你可以： * 选择一个下标 i ，它在之前的操作中 没有 被选择过。 * 将 nums[i] 增加范围 [-k, k] 中的一个整数。 在执行完所有操作以后，请你返回 nums 中出现 频率最高 元素的出现次数。 一个元素 x 的 频率 指的是它在数组中出现的次数。 示例 1： 输入：nums = [1,4,5], k = 1, numOperations = 2 输出：2 解释： 通过以下操作得到最高频率 2 ： * 将 nums[1] 增加 0 ，nums 变为 [1, 4, 5] 。 * 将 nums[2] 增加 -1 ，nums 变为 [1, 4, 4] 。 示例 2： 输入：nums = [5,11,20,20], k = 5, numOperations = 1 输出：2 解释： 通过以下操作得到最高频率 2 ： * 将 nums[1] 增加 0 。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 105 * 0 <= k <= 105 * 0 <= numOperations <= nums.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到最大频率的子数组。

算法步骤:
1. 对数组进行排序。
2. 使用滑动窗口来找到满足条件的最大长度子数组。
3. 计算滑动窗口内的元素个数，并更新最大频率。

关键点:
- 排序后的数组可以方便地使用滑动窗口来找到满足条件的子数组。
- 滑动窗口的右边界不断扩展，直到不满足条件时收缩左边界。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 主要由排序操作决定。
空间复杂度: O(1) - 除了输入输出外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_frequency(nums: List[int], k: int, num_operations: int) -> int:
    """
    函数式接口 - 返回执行操作后元素的最高频率
    """
    # 对数组进行排序
    nums.sort()
    
    # 初始化滑动窗口的左右边界
    left = 0
    max_freq = 0
    total_operations = 0
    
    # 滑动窗口的右边界
    for right in range(len(nums)):
        # 计算当前窗口内需要的操作次数
        total_operations += (nums[right] - nums[right - 1]) * (right - left)
        
        # 如果操作次数超过限制，收缩左边界
        while total_operations > k * num_operations:
            total_operations -= nums[right] - nums[left]
            left += 1
        
        # 更新最大频率
        max_freq = max(max_freq, right - left + 1)
    
    return max_freq


Solution = create_solution(max_frequency)