# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000332
标题: 搜索插入位置
难度: easy
链接: https://leetcode.cn/problems/N6YdxV/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 068. 搜索插入位置 - 给定一个排序的整数数组 nums 和一个整数目标值 target ，请在数组中找到 target ，并返回其下标。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。 请必须使用时间复杂度为 O(log n) 的算法。 示例 1： 输入: nums = [1,3,5,6], target = 5 输出: 2 示例 2： 输入: nums = [1,3,5,6], target = 2 输出: 1 示例 3： 输入: nums = [1,3,5,6], target = 7 输出: 4 示例 4： 输入: nums = [1,3,5,6], target = 0 输出: 0 示例 5： 输入: nums = [1], target = 0 输出: 0 提示： * 1 <= nums.length <= 104 * -104 <= nums[i] <= 104 * nums 为无重复元素的升序排列数组 * -104 <= target <= 104 注意：本题与主站 35 题相同： https://leetcode.cn/problems/search-insert-position/ [https://leetcode.cn/problems/search-insert-position/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到目标值或其插入位置。

算法步骤:
1. 初始化左右指针 left 和 right，分别指向数组的起始和末尾。
2. 进行二分查找：
   - 计算中间位置 mid。
   - 如果 nums[mid] 等于 target，返回 mid。
   - 如果 nums[mid] 小于 target，将 left 移动到 mid + 1。
   - 如果 nums[mid] 大于 target，将 right 移动到 mid - 1。
3. 如果没有找到 target，返回 left 作为插入位置。

关键点:
- 二分查找的时间复杂度为 O(log n)，空间复杂度为 O(1)。
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


def search_insert_position(nums: List[int], target: int) -> int:
    """
    函数式接口 - 使用二分查找找到目标值或其插入位置
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left


Solution = create_solution(search_insert_position)