# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3152
标题: Maximum Value of an Ordered Triplet II
难度: medium
链接: https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2874. 有序三元组中的最大值 II - 给你一个下标从 0 开始的整数数组 nums 。 请你从所有满足 i < j < k 的下标三元组 (i, j, k) 中，找出并返回下标三元组的最大值。如果所有满足条件的三元组的值都是负数，则返回 0 。 下标三元组 (i, j, k) 的值等于 (nums[i] - nums[j]) * nums[k] 。 示例 1： 输入：nums = [12,6,1,2,7] 输出：77 解释：下标三元组 (0, 2, 4) 的值是 (nums[0] - nums[2]) * nums[4] = 77 。 可以证明不存在值大于 77 的有序下标三元组。 示例 2： 输入：nums = [1,10,3,4,19] 输出：133 解释：下标三元组 (1, 2, 4) 的值是 (nums[1] - nums[2]) * nums[4] = 133 。 可以证明不存在值大于 133 的有序下标三元组。 示例 3： 输入：nums = [1,2,3] 输出：0 解释：唯一的下标三元组 (0, 1, 2) 的值是一个负数，(nums[0] - nums[1]) * nums[2] = -3 。因此，答案是 0 。 提示： * 3 <= nums.length <= 105 * 1 <= nums[i] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和前缀最大值来优化计算。

算法步骤:
1. 初始化两个数组 `max_left` 和 `max_right`，分别记录每个位置左边和右边的最大值。
2. 遍历数组，填充 `max_left` 和 `max_right`。
3. 再次遍历数组，计算每个可能的三元组 `(i, j, k)` 的值，并更新最大值。

关键点:
- 使用 `max_left` 和 `max_right` 来避免重复计算，从而优化时间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def maximum_triplet_value(nums: List[int]) -> int:
    n = len(nums)
    max_left = [0] * n
    max_right = [0] * n
    
    # 填充 max_left 数组
    max_left[0] = nums[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], nums[i])
    
    # 填充 max_right 数组
    max_right[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], nums[i])
    
    max_value = 0
    for j in range(1, n - 1):
        if max_left[j - 1] > nums[j]:
            max_value = max(max_value, (max_left[j - 1] - nums[j]) * max_right[j + 1])
    
    return max_value


Solution = create_solution(maximum_triplet_value)