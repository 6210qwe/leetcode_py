# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3619
标题: Adjacent Increasing Subarrays Detection II
难度: medium
链接: https://leetcode.cn/problems/adjacent-increasing-subarrays-detection-ii/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3350. 检测相邻递增子数组 II - 给你一个由 n 个整数组成的数组 nums ，请你找出 k 的 最大值，使得存在 两个 相邻 且长度为 k 的 严格递增 子数组。具体来说，需要检查是否存在从下标 a 和 b (a < b) 开始的 两个 子数组，并满足下述全部条件： * 这两个子数组 nums[a..a + k - 1] 和 nums[b..b + k - 1] 都是 严格递增 的。 * 这两个子数组必须是 相邻的，即 b = a + k。 返回 k 的 最大可能 值。 子数组 是数组中的一个连续 非空 的元素序列。 示例 1： 输入：nums = [2,5,7,8,9,2,3,4,3,1] 输出：3 解释： * 从下标 2 开始的子数组是 [7, 8, 9]，它是严格递增的。 * 从下标 5 开始的子数组是 [2, 3, 4]，它也是严格递增的。 * 这两个子数组是相邻的，因此 3 是满足题目条件的 最大 k 值。 示例 2： 输入：nums = [1,2,3,4,4,4,4,5,6,7] 输出：2 解释： * 从下标 0 开始的子数组是 [1, 2]，它是严格递增的。 * 从下标 2 开始的子数组是 [3, 4]，它也是严格递增的。 * 这两个子数组是相邻的，因此 2 是满足题目条件的 最大 k 值。 提示： * 2 <= nums.length <= 2 * 105 * -109 <= nums[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来检测相邻的严格递增子数组，并记录最大长度。

算法步骤:
1. 初始化两个指针 `left` 和 `right`，分别表示当前窗口的左右边界。
2. 初始化变量 `max_k` 用于记录最大长度。
3. 遍历数组，使用 `right` 指针扩展窗口，直到遇到不递增的情况。
4. 如果窗口长度大于等于 `max_k`，则更新 `max_k`。
5. 移动 `left` 指针到新的起始位置，继续扩展窗口。
6. 返回 `max_k`。

关键点:
- 使用滑动窗口来检测严格递增的子数组。
- 更新最大长度时，确保子数组是相邻的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 检测相邻递增子数组 II
    """
    n = len(nums)
    max_k = 0
    left = 0
    right = 0

    while right < n - 1:
        if nums[right] < nums[right + 1]:
            right += 1
        else:
            window_length = right - left + 1
            if window_length >= max_k and right - left == max_k - 1:
                max_k = window_length
            left = right + 1
            right = left

    # Check the last window
    window_length = right - left + 1
    if window_length >= max_k and right - left == max_k - 1:
        max_k = window_length

    return max_k


Solution = create_solution(solution_function_name)