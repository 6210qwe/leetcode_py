# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3698
标题: Minimum Operations to Make Subarray Elements Equal
难度: medium
链接: https://leetcode.cn/problems/minimum-operations-to-make-subarray-elements-equal/
题目类型: 数组、哈希表、数学、滑动窗口、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3422. 将子数组元素变为相等所需的最小操作数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表来记录每个元素的出现次数，并计算每个窗口内的最小操作数。

算法步骤:
1. 初始化一个哈希表 `count` 来记录当前窗口内每个元素的出现次数。
2. 使用两个指针 `left` 和 `right` 来表示滑动窗口的左右边界。
3. 移动右指针扩展窗口，更新哈希表 `count`。
4. 当窗口大小超过 `k` 时，移动左指针收缩窗口，更新哈希表 `count`。
5. 在每次窗口调整后，计算当前窗口内的最小操作数，并更新全局最小操作数。

关键点:
- 使用滑动窗口来维护当前子数组的范围。
- 使用哈希表来记录当前窗口内每个元素的出现次数。
- 通过窗口内最大频率的元素来计算最小操作数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。每个元素最多被处理两次（一次加入窗口，一次移出窗口）。
空间复杂度: O(n)，哈希表 `count` 最多存储 n 个不同的元素。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_operations_to_equal_subarray(nums: List[int], k: int) -> int:
    """
    计算将子数组元素变为相等所需的最小操作数。
    """
    if not nums or k <= 0:
        return 0

    count = {}
    left = 0
    min_ops = float('inf')
    max_freq = 0

    for right in range(len(nums)):
        # 更新当前窗口内元素的出现次数
        count[nums[right]] = count.get(nums[right], 0) + 1
        max_freq = max(max_freq, count[nums[right]])

        # 如果窗口大小超过 k，移动左指针收缩窗口
        if right - left + 1 > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1

        # 计算当前窗口内的最小操作数
        if right - left + 1 == k:
            min_ops = min(min_ops, k - max_freq)

    return min_ops


Solution = create_solution(min_operations_to_equal_subarray)