# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1918
标题: Maximum Score of a Good Subarray
难度: hard
链接: https://leetcode.cn/problems/maximum-score-of-a-good-subarray/
题目类型: 栈、数组、双指针、二分查找、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1793. 好子数组的最大分数 - 给你一个整数数组 nums （下标从 0 开始）和一个整数 k 。 一个子数组 (i, j) 的 分数 定义为 min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1) 。一个 好 子数组的两个端点下标需要满足 i <= k <= j 。 请你返回 好 子数组的最大可能 分数 。 示例 1： 输入：nums = [1,4,3,7,4,5], k = 3 输出：15 解释：最优子数组的左右端点下标是 (1, 5) ，分数为 min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15 。 示例 2： 输入：nums = [5,5,4,5,4,1,1,1], k = 0 输出：20 解释：最优子数组的左右端点下标是 (0, 4) ，分数为 min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20 。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 2 * 104 * 0 <= k < nums.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针方法，从中间向两边扩展，找到最大分数。

算法步骤:
1. 初始化左指针 `left` 和右指针 `right`，初始值分别为 `k`。
2. 初始化当前最小值 `min_val` 为 `nums[k]`，并初始化最大分数 `max_score` 为 `nums[k]`。
3. 在 `left` 和 `right` 没有越界的情况下，比较 `nums[left-1]` 和 `nums[right+1]`，选择较大的一方进行扩展。
4. 更新 `min_val` 为当前子数组中的最小值，并更新 `max_score`。
5. 返回 `max_score`。

关键点:
- 使用双指针从中间向两边扩展，确保每次扩展时都选择较大的值。
- 通过维护当前子数组的最小值来计算分数。
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


def solution_function_name(nums: List[int], k: int) -> int:
    """
    函数式接口 - 实现
    """
    left, right = k, k
    min_val = nums[k]
    max_score = nums[k]

    while left > 0 or right < len(nums) - 1:
        if (nums[left - 1] if left > 0 else float('-inf')) > (nums[right + 1] if right < len(nums) - 1 else float('-inf')):
            left -= 1
        else:
            right += 1
        min_val = min(min_val, nums[left], nums[right])
        max_score = max(max_score, min_val * (right - left + 1))

    return max_score


Solution = create_solution(solution_function_name)