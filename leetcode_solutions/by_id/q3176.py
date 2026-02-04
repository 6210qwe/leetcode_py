# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3176
标题: Minimum Sum of Mountain Triplets I
难度: easy
链接: https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-i/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2908. 元素和最小的山形三元组 I - 给你一个下标从 0 开始的整数数组 nums 。 如果下标三元组 (i, j, k) 满足下述全部条件，则认为它是一个 山形三元组 ： * i < j < k * nums[i] < nums[j] 且 nums[k] < nums[j] 请你找出 nums 中 元素和最小 的山形三元组，并返回其 元素和 。如果不存在满足条件的三元组，返回 -1 。 示例 1： 输入：nums = [8,6,1,5,3] 输出：9 解释：三元组 (2, 3, 4) 是一个元素和等于 9 的山形三元组，因为： - 2 < 3 < 4 - nums[2] < nums[3] 且 nums[4] < nums[3] 这个三元组的元素和等于 nums[2] + nums[3] + nums[4] = 9 。可以证明不存在元素和小于 9 的山形三元组。 示例 2： 输入：nums = [5,4,8,7,10,2] 输出：13 解释：三元组 (1, 3, 5) 是一个元素和等于 13 的山形三元组，因为： - 1 < 3 < 5 - nums[1] < nums[3] 且 nums[5] < nums[3] 这个三元组的元素和等于 nums[1] + nums[3] + nums[5] = 13 。可以证明不存在元素和小于 13 的山形三元组。 示例 3： 输入：nums = [6,5,4,3,4,5] 输出：-1 解释：可以证明 nums 中不存在山形三元组。 提示： * 3 <= nums.length <= 50 * 1 <= nums[i] <= 50
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个辅助数组来记录每个位置左边和右边的最小值，然后遍历中间位置，找到满足条件的最小和。

算法步骤:
1. 初始化两个数组 left_min 和 right_min，分别记录每个位置左边和右边的最小值。
2. 填充 left_min 数组，left_min[i] 表示 nums[0:i] 中的最小值。
3. 填充 right_min 数组，right_min[i] 表示 nums[i+1:] 中的最小值。
4. 遍历中间位置 j，检查是否存在满足条件的山形三元组 (i, j, k)，并更新最小和。

关键点:
- 使用两个辅助数组来减少重复计算。
- 遍历中间位置时，确保 i < j < k 并且 nums[i] < nums[j] 且 nums[k] < nums[j]。
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


def minimum_sum_of_mountain_triplets(nums: List[int]) -> int:
    """
    函数式接口 - 找出 nums 中元素和最小的山形三元组，并返回其元素和。如果不存在满足条件的三元组，返回 -1。
    """
    n = len(nums)
    if n < 3:
        return -1
    
    # 初始化 left_min 和 right_min 数组
    left_min = [float('inf')] * n
    right_min = [float('inf')] * n
    
    # 填充 left_min 数组
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], nums[i - 1])
    
    # 填充 right_min 数组
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], nums[i + 1])
    
    # 遍历中间位置 j，找到满足条件的最小和
    min_sum = float('inf')
    for j in range(1, n - 1):
        if left_min[j] < nums[j] and right_min[j] < nums[j]:
            min_sum = min(min_sum, left_min[j] + nums[j] + right_min[j])
    
    return min_sum if min_sum != float('inf') else -1


Solution = create_solution(minimum_sum_of_mountain_triplets)