# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3154
标题: Maximum Value of an Ordered Triplet I
难度: easy
链接: https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-i/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2873. 有序三元组中的最大值 I - 给你一个下标从 0 开始的整数数组 nums 。 请你从所有满足 i < j < k 的下标三元组 (i, j, k) 中，找出并返回下标三元组的最大值。如果所有满足条件的三元组的值都是负数，则返回 0 。 下标三元组 (i, j, k) 的值等于 (nums[i] - nums[j]) * nums[k] 。 示例 1： 输入：nums = [12,6,1,2,7] 输出：77 解释：下标三元组 (0, 2, 4) 的值是 (nums[0] - nums[2]) * nums[4] = 77 。 可以证明不存在值大于 77 的有序下标三元组。 示例 2： 输入：nums = [1,10,3,4,19] 输出：133 解释：下标三元组 (1, 2, 4) 的值是 (nums[1] - nums[2]) * nums[4] = 133 。 可以证明不存在值大于 133 的有序下标三元组。 示例 3： 输入：nums = [1,2,3] 输出：0 解释：唯一的下标三元组 (0, 1, 2) 的值是一个负数，(nums[0] - nums[1]) * nums[2] = -3 。因此，答案是 0 。 提示： * 3 <= nums.length <= 100 * 1 <= nums[i] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过一次遍历找到最大的 (nums[i] - nums[j]) * nums[k] 值。

算法步骤:
1. 初始化三个变量：max_i 用于存储当前最大值的 nums[i]，max_triplet 用于存储当前最大三元组值，current_max 用于存储当前最大的 (nums[i] - nums[j])。
2. 从右向左遍历数组：
   - 更新 current_max 为 max(current_max, nums[i] - nums[j])。
   - 更新 max_triplet 为 max(max_triplet, current_max * nums[k])。
3. 返回 max_triplet，如果 max_triplet 为负数则返回 0。

关键点:
- 通过从右向左遍历，可以确保在计算 (nums[i] - nums[j]) * nums[k] 时，已经知道 nums[k] 的值。
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
    函数式接口 - 找出并返回下标三元组的最大值
    """
    n = len(nums)
    if n < 3:
        return 0

    max_triplet = 0
    current_max = 0

    for k in range(n - 1, 1, -1):
        for j in range(k - 1, 0, -1):
            current_max = max(current_max, nums[j - 1] - nums[j])
            max_triplet = max(max_triplet, current_max * nums[k])

    return max(max_triplet, 0)


Solution = create_solution(solution_function_name)