# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1185
标题: Find in Mountain Array
难度: hard
链接: https://leetcode.cn/problems/find-in-mountain-array/
题目类型: 数组、二分查找、交互
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1095. 山脉数组中查找目标值 - （这是一个 交互式问题 ） 你可以将一个数组 arr 称为 山脉数组 当且仅当： * arr.length >= 3 * 存在一些 0 < i < arr.length - 1 的 i 使得： * arr[0] < arr[1] < ... < arr[i - 1] < arr[i] * arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 给定一个山脉数组 mountainArr ，返回 最小 的 index 使得 mountainArr.get(index) == target。如果不存在这样的 index，返回 -1 。 你无法直接访问山脉数组。你只能使用 MountainArray 接口来访问数组： * MountainArray.get(k) 返回数组中下标为 k 的元素（从 0 开始）。 * MountainArray.length() 返回数组的长度。 调用 MountainArray.get 超过 100 次的提交会被判定为错误答案。此外，任何试图绕过在线评测的解决方案都将导致取消资格。 示例 1： 输入：mountainArr = [1,2,3,4,5,3,1], target = 3 输出：2 解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。 示例 2： 输入：mountainArr = [0,1,2,4,2,1], target = 3 输出：-1 解释：3 在数组中没有出现，返回 -1。 提示： * 3 <= mountainArr.length() <= 104 * 0 <= target <= 109 * 0 <= mountainArr.get(index) <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找找到山脉数组的峰值，然后分别在上升和下降部分进行二分查找。

算法步骤:
1. 使用二分查找找到山脉数组的峰值。
2. 在上升部分进行二分查找，寻找目标值。
3. 如果在上升部分未找到目标值，在下降部分进行二分查找。

关键点:
- 通过二分查找减少调用 MountainArray.get 的次数。
- 分别处理上升和下降部分的二分查找逻辑。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


def find_peak(mountain_arr: MountainArray) -> int:
    left, right = 0, mountain_arr.length() - 1
    while left < right:
        mid = (left + right) // 2
        if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
            left = mid + 1
        else:
            right = mid
    return left


def binary_search_asc(mountain_arr: MountainArray, target: int, left: int, right: int) -> int:
    while left <= right:
        mid = (left + right) // 2
        mid_val = mountain_arr.get(mid)
        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_desc(mountain_arr: MountainArray, target: int, left: int, right: int) -> int:
    while left <= right:
        mid = (left + right) // 2
        mid_val = mountain_arr.get(mid)
        if mid_val == target:
            return mid
        elif mid_val < target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def solution_function_name(mountain_arr: MountainArray, target: int) -> int:
    peak_index = find_peak(mountain_arr)

    # 在上升部分进行二分查找
    result = binary_search_asc(mountain_arr, target, 0, peak_index)
    if result != -1:
        return result

    # 在下降部分进行二分查找
    return binary_search_desc(mountain_arr, target, peak_index + 1, mountain_arr.length() - 1)


Solution = create_solution(solution_function_name)