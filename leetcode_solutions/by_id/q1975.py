# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1975
标题: Minimum Distance to the Target Element
难度: easy
链接: https://leetcode.cn/problems/minimum-distance-to-the-target-element/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1848. 到目标元素的最小距离 - 给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数 target 和 start ，请你找出一个下标 i ，满足 nums[i] == target 且 abs(i - start) 最小化 。注意：abs(x) 表示 x 的绝对值。 返回 abs(i - start) 。 题目数据保证 target 存在于 nums 中。 示例 1： 输入：nums = [1,2,3,4,5], target = 5, start = 3 输出：1 解释：nums[4] = 5 是唯一一个等于 target 的值，所以答案是 abs(4 - 3) = 1 。 示例 2： 输入：nums = [1], target = 1, start = 0 输出：0 解释：nums[0] = 1 是唯一一个等于 target 的值，所以答案是 abs(0 - 0) = 0 。 示例 3： 输入：nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0 输出：0 解释：nums 中的每个值都是 1 ，但 nums[0] 使 abs(i - start) 的结果得以最小化，所以答案是 abs(0 - 0) = 0 。 提示： * 1 <= nums.length <= 1000 * 1 <= nums[i] <= 104 * 0 <= start < nums.length * target 存在于 nums 中
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 从 start 位置开始，向左和向右同时扩展，找到第一个等于 target 的位置。

算法步骤:
1. 初始化最小距离为无穷大。
2. 从 start 位置开始，分别向左和向右扩展，找到第一个等于 target 的位置。
3. 更新最小距离。
4. 返回最小距离。

关键点:
- 从 start 位置开始双向扩展，确保找到最近的目标元素。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。最坏情况下需要遍历整个数组。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_distance_to_target(nums: List[int], target: int, start: int) -> int:
    """
    函数式接口 - 找到与 start 位置最近的目标元素的距离
    """
    min_distance = float('inf')
    
    # 向左扩展
    for i in range(start, -1, -1):
        if nums[i] == target:
            min_distance = min(min_distance, start - i)
            break
    
    # 向右扩展
    for i in range(start, len(nums)):
        if nums[i] == target:
            min_distance = min(min_distance, i - start)
            break
    
    return min_distance


Solution = create_solution(min_distance_to_target)