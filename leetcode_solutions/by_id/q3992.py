# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3992
标题: Longest Semi-Repeating Subarray
难度: medium
链接: https://leetcode.cn/problems/longest-semi-repeating-subarray/
题目类型: 数组、哈希表、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3641. 最长半重复子数组 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到最长的半重复子数组。

算法步骤:
1. 初始化两个指针 left 和 right，以及一个哈希表来记录当前窗口内的元素及其出现次数。
2. 移动右指针扩展窗口，更新哈希表。
3. 如果当前窗口内有超过一个元素出现两次以上，则移动左指针缩小窗口，直到窗口内最多只有一个元素出现两次。
4. 在每次调整窗口后，更新最长半重复子数组的长度。

关键点:
- 使用滑动窗口来维护当前子数组的状态。
- 哈希表用于记录当前窗口内每个元素的出现次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。每个元素最多被访问两次（一次通过右指针，一次通过左指针）。
空间复杂度: O(min(n, k))，其中 k 是数组中不同元素的数量。哈希表的大小最多为 k。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_semi_repeating_subarray(nums: List[int]) -> int:
    """
    函数式接口 - 找到最长的半重复子数组
    """
    if not nums:
        return 0

    left = 0
    max_length = 0
    count = {}

    for right in range(len(nums)):
        if nums[right] in count:
            count[nums[right]] += 1
        else:
            count[nums[right]] = 1

        while len([x for x in count.values() if x > 1]) > 1:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


Solution = create_solution(longest_semi_repeating_subarray)