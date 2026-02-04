# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100240
标题: Magic Index LCCI
难度: easy
链接: https://leetcode.cn/problems/magic-index-lcci/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 08.03. 魔术索引 - 魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。 示例 1： 输入：nums = [0, 2, 3, 4, 5] 输出：0 说明：0下标的元素为0 示例 2： 输入：nums = [1, 1, 1] 输出：1 说明： 1. nums长度在[1, 1000000]之间 2. 此题为原书中的 Follow-up，即数组中可能包含重复元素的版本
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来减少搜索范围，但需要处理重复元素的情况。

算法步骤:
1. 定义一个辅助函数 `find_magic_index`，用于递归地进行二分查找。
2. 在每次递归中，计算中间索引 `mid`，并检查 `nums[mid]` 是否等于 `mid`。
3. 如果 `nums[mid]` 等于 `mid`，则继续在左半部分查找是否有更小的魔术索引。
4. 如果 `nums[mid]` 小于 `mid`，则在右半部分查找。
5. 如果 `nums[mid]` 大于 `mid`，则在左半部分查找。
6. 递归结束时，返回找到的魔术索引或 -1。

关键点:
- 通过二分查找减少搜索范围。
- 处理重复元素的情况，确保找到最小的魔术索引。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 二分查找的时间复杂度
空间复杂度: O(1) - 仅使用常数级额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_magic_index(nums: List[int], left: int, right: int) -> int:
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if nums[mid] == mid:
        # 继续在左半部分查找是否有更小的魔术索引
        left_magic = find_magic_index(nums, left, mid - 1)
        if left_magic != -1:
            return left_magic
        else:
            return mid
    elif nums[mid] < mid:
        # 在右半部分查找
        return find_magic_index(nums, mid + 1, right)
    else:
        # 在左半部分查找
        return find_magic_index(nums, left, mid - 1)


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 找到数组中的魔术索引
    """
    return find_magic_index(nums, 0, len(nums) - 1)


Solution = create_solution(solution_function_name)