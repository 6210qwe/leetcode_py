# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 81
标题: Search in Rotated Sorted Array II
难度: medium
链接: https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
81. 搜索旋转排序数组 II - 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。 给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。 你必须尽可能减少整个操作步骤。 示例 1： 输入：nums = [2,5,6,0,0,1,2], target = 0 输出：true 示例 2： 输入：nums = [2,5,6,0,0,1,2], target = 3 输出：false 提示： * 1 <= nums.length <= 5000 * -104 <= nums[i] <= 104 * 题目数据保证 nums 在预先未知的某个下标上进行了旋转 * -104 <= target <= 104 进阶： * 此题与 搜索旋转排序数组 [https://leetcode.cn/problems/search-in-rotated-sorted-array/description/] 相似，但本题中的 nums 可能包含 重复 元素。这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 二分查找，处理重复元素的情况

算法步骤:
1. 使用二分查找，但需要处理nums[left] == nums[mid] == nums[right]的情况
2. 如果nums[left] == nums[mid] == nums[right]，无法判断哪边有序，left++，right--
3. 否则，判断哪边有序：
   - 如果nums[left] <= nums[mid]，左半部分有序
   - 否则，右半部分有序
4. 在有序部分中判断target是否在其中，调整搜索范围

关键点:
- 由于有重复元素，当nums[left] == nums[mid] == nums[right]时，需要缩小范围
- 最坏情况下时间复杂度O(n)，平均O(log n)
- 空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 最坏情况需要遍历整个数组（当所有元素都相同时）
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def search(nums: List[int], target: int) -> bool:
    """
    函数式接口 - 二分查找（处理重复元素）
    
    实现思路:
    使用二分查找，处理重复元素的情况，当无法判断哪边有序时缩小范围。
    
    Args:
        nums: 旋转后的非降序数组，可能包含重复元素
        target: 目标值
        
    Returns:
        如果target存在于数组中返回True，否则返回False
        
    Example:
        >>> search([2,5,6,0,0,1,2], 0)
        True
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return True
        
        # 处理重复元素的情况
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            # 左半部分有序
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # 右半部分有序
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return False


# 自动生成Solution类（无需手动编写）
Solution = create_solution(search)
