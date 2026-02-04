# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3372
标题: Longest Strictly Increasing or Strictly Decreasing Subarray
难度: easy
链接: https://leetcode.cn/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3105. 最长的严格递增或递减子数组 - 给你一个整数数组 nums 。 返回数组 nums 中 严格递增 或 严格递减 的最长非空子数组的长度。 示例 1： 输入：nums = [1,4,3,3,2] 输出：2 解释： nums 中严格递增的子数组有[1]、[2]、[3]、[3]、[4] 以及 [1,4] 。 nums 中严格递减的子数组有[1]、[2]、[3]、[3]、[4]、[3,2] 以及 [4,3] 。 因此，返回 2 。 示例 2： 输入：nums = [3,3,3,3] 输出：1 解释： nums 中严格递增的子数组有 [3]、[3]、[3] 以及 [3] 。 nums 中严格递减的子数组有 [3]、[3]、[3] 以及 [3] 。 因此，返回 1 。 示例 3： 输入：nums = [3,2,1] 输出：3 解释： nums 中严格递增的子数组有 [3]、[2] 以及 [1] 。 nums 中严格递减的子数组有 [3]、[2]、[1]、[3,2]、[2,1] 以及 [3,2,1] 。 因此，返回 3 。 提示： * 1 <= nums.length <= 50 * 1 <= nums[i] <= 50
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个变量分别记录当前递增和递减子数组的长度，并在遍历过程中更新最大长度。

算法步骤:
1. 初始化两个变量 `inc_len` 和 `dec_len` 分别记录当前递增和递减子数组的长度，初始值为 1。
2. 初始化一个变量 `max_len` 记录最长的严格递增或递减子数组的长度，初始值为 1。
3. 遍历数组 `nums`，从第二个元素开始：
   - 如果当前元素大于前一个元素，更新 `inc_len` 并重置 `dec_len`。
   - 如果当前元素小于前一个元素，更新 `dec_len` 并重置 `inc_len`。
   - 如果当前元素等于前一个元素，重置 `inc_len` 和 `dec_len`。
   - 更新 `max_len` 为 `inc_len` 和 `dec_len` 中的最大值。
4. 返回 `max_len`。

关键点:
- 使用两个变量分别记录递增和递减子数组的长度，避免多次遍历。
- 在遍历过程中动态更新最大长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 `nums` 的长度。我们只需要遍历数组一次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_strictly_increasing_or_decreasing_subarray(nums: List[int]) -> int:
    """
    返回数组 nums 中 严格递增 或 严格递减 的最长非空子数组的长度。
    """
    if not nums:
        return 0

    inc_len = 1
    dec_len = 1
    max_len = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            inc_len += 1
            dec_len = 1
        elif nums[i] < nums[i - 1]:
            dec_len += 1
            inc_len = 1
        else:
            inc_len = 1
            dec_len = 1

        max_len = max(max_len, inc_len, dec_len)

    return max_len


Solution = create_solution(longest_strictly_increasing_or_decreasing_subarray)