# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4036
标题: Sum of Weighted Modes in Subarrays
难度: medium
链接: https://leetcode.cn/problems/sum-of-weighted-modes-in-subarrays/
题目类型: 数组、哈希表、计数、有序集合、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3672. 子数组中加权众数的总和 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和有序字典来维护当前窗口内的元素及其频率，并在每次移动窗口时更新众数。

算法步骤:
1. 初始化一个有序字典 `freq` 来记录当前窗口内每个元素的频率。
2. 初始化变量 `max_freq` 和 `mode_sum` 分别记录当前窗口的最大频率和众数的总和。
3. 使用滑动窗口遍历数组：
   - 将新元素加入窗口，并更新其频率。
   - 如果新元素的频率大于 `max_freq`，更新 `max_freq` 和 `mode_sum`。
   - 如果新元素的频率等于 `max_freq`，将新元素加入 `mode_sum`。
   - 移除旧元素，并更新其频率。如果旧元素的频率等于 `max_freq`，从 `mode_sum` 中移除。
4. 返回 `mode_sum`。

关键点:
- 使用有序字典来维护频率，以便快速找到最大频率的元素。
- 滑动窗口的大小固定为 `k`，确保时间复杂度为 O(n)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(k)，其中 k 是滑动窗口的大小。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import OrderedDict, Counter

def sum_of_weighted_modes(nums: List[int], k: int) -> int:
    """
    计算所有长度为 k 的子数组中加权众数的总和。
    """
    freq = OrderedDict()
    max_freq = 0
    mode_sum = 0
    n = len(nums)

    for i in range(n):
        # 添加新元素到窗口
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1

        # 更新最大频率和众数总和
        if freq[nums[i]] > max_freq:
            max_freq = freq[nums[i]]
            mode_sum = nums[i]
        elif freq[nums[i]] == max_freq:
            mode_sum += nums[i]

        # 移除旧元素
        if i >= k:
            old_num = nums[i - k]
            freq[old_num] -= 1
            if freq[old_num] == 0:
                del freq[old_num]
            if old_num == mode_sum:
                mode_sum -= old_num
                if freq and max(freq.values()) < max_freq:
                    max_freq = max(freq.values())
                    mode_sum = 0
                    for num, count in freq.items():
                        if count == max_freq:
                            mode_sum += num

    return mode_sum

Solution = create_solution(sum_of_weighted_modes)