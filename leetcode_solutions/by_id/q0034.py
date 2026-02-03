# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 34
标题: Find First and Last Position of Element in Sorted Array
难度: medium
链接: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
34. 在排序数组中查找元素的第一个和最后一个位置 - 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。 如果数组中不存在目标值 target，返回 [-1, -1]。 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。 示例 1： 输入：nums = [5,7,7,8,8,10], target = 8 输出：[3,4] 示例 2： 输入：nums = [5,7,7,8,8,10], target = 6 输出：[-1,-1] 示例 3： 输入：nums = [], target = 0 输出：[-1,-1] 提示： * 0 <= nums.length <= 105 * -109 <= nums[i] <= 109 * nums 是一个非递减数组 * -109 <= target <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 二分查找，分别找到第一个和最后一个等于target的位置

算法步骤:
1. 使用二分查找找到第一个大于等于target的位置（左边界）
2. 如果左边界不存在或nums[left] != target，返回[-1, -1]
3. 使用二分查找找到第一个大于target的位置（右边界）
4. 返回[left, right - 1]

关键点:
- 使用两次二分查找分别找到左边界和右边界
- 左边界：第一个>=target的位置
- 右边界：第一个>target的位置
- 时间复杂度O(log n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 两次二分查找，n为数组长度
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def search_range(nums: List[int], target: int) -> List[int]:
    """
    函数式接口 - 二分查找实现
    
    实现思路:
    使用两次二分查找，分别找到第一个和最后一个等于target的位置。
    
    Args:
        nums: 非递减顺序排列的整数数组
        target: 目标值
        
    Returns:
        目标值在数组中的开始位置和结束位置，如果不存在则返回[-1, -1]
        
    Example:
        >>> search_range([5,7,7,8,8,10], 8)
        [3, 4]
        >>> search_range([5,7,7,8,8,10], 6)
        [-1, -1]
    """
    def find_left(nums: List[int], target: int) -> int:
        """找到第一个>=target的位置"""
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
    def find_right(nums: List[int], target: int) -> int:
        """找到第一个>target的位置"""
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left
    
    if not nums:
        return [-1, -1]
    
    left = find_left(nums, target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    
    right = find_right(nums, target)
    return [left, right - 1]


# 自动生成Solution类（无需手动编写）
Solution = create_solution(search_range)
