# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3640
标题: Maximum Frequency of an Element After Performing Operations II
难度: hard
链接: https://leetcode.cn/problems/maximum-frequency-of-an-element-after-performing-operations-ii/
题目类型: 数组、二分查找、前缀和、排序、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3347. 执行操作后元素的最高频率 II - 给你一个整数数组 nums 和两个整数 k 和 numOperations 。 你必须对 nums 执行 操作 numOperations 次。每次操作中，你可以： * 选择一个下标 i ，它在之前的操作中 没有 被选择过。 * 将 nums[i] 增加范围 [-k, k] 中的一个整数。 在执行完所有操作以后，请你返回 nums 中出现 频率最高 元素的出现次数。 一个元素 x 的 频率 指的是它在数组中出现的次数。 示例 1： 输入：nums = [1,4,5], k = 1, numOperations = 2 输出：2 解释： 通过以下操作得到最高频率 2 ： * 将 nums[1] 增加 0 ，nums 变为 [1, 4, 5] 。 * 将 nums[2] 增加 -1 ，nums 变为 [1, 4, 4] 。 示例 2： 输入：nums = [5,11,20,20], k = 5, numOperations = 1 输出：2 解释： 通过以下操作得到最高频率 2 ： * 将 nums[1] 增加 0 。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 109 * 0 <= k <= 109 * 0 <= numOperations <= nums.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到最长的子数组，使得该子数组中的所有元素可以通过不超过 numOperations 次操作变为相同的值。

算法步骤:
1. 对数组进行排序。
2. 使用滑动窗口来找到最长的子数组，使得该子数组中的所有元素可以通过不超过 numOperations 次操作变为相同的值。
3. 计算窗口内的元素是否可以通过 numOperations 次操作变为相同的值。
4. 更新最大频率。

关键点:
- 通过排序和滑动窗口，可以有效地找到最长的子数组。
- 通过计算窗口内的元素是否可以通过 numOperations 次操作变为相同的值，来更新最大频率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 nums 的长度。排序的时间复杂度是 O(n log n)，滑动窗口的时间复杂度是 O(n)。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def maxFrequency(nums: List[int], k: int, numOperations: int) -> int:
    """
    函数式接口 - 返回执行 numOperations 次操作后，nums 中出现频率最高的元素的出现次数。
    """
    nums.sort()
    left = 0
    max_freq = 0
    total_operations = 0
    
    for right in range(len(nums)):
        total_operations += (nums[right] - nums[right - 1]) * (right - left)
        
        while total_operations > numOperations * k:
            total_operations -= (nums[right] - nums[left])
            left += 1
        
        max_freq = max(max_freq, right - left + 1)
    
    return max_freq

Solution = create_solution(maxFrequency)