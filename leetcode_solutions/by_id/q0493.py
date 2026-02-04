# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 493
标题: Reverse Pairs
难度: hard
链接: https://leetcode.cn/problems/reverse-pairs/
题目类型: 树状数组、线段树、数组、二分查找、分治、有序集合、归并排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
493. 翻转对 - 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。 你需要返回给定数组中的重要翻转对的数量。 示例 1: 输入: [1,3,2,3,1] 输出: 2 示例 2: 输入: [2,4,3,5,1] 输出: 3 注意: 1. 给定数组的长度不会超过50000。 2. 输入数组中的所有数字都在32位整数的表示范围内。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用归并排序来统计逆序对，同时在合并过程中计算满足条件的翻转对。

算法步骤:
1. 分解数组为两个子数组，分别递归处理。
2. 在合并两个已排序子数组的过程中，统计满足 nums[i] > 2 * nums[j] 的翻转对。
3. 合并两个子数组，并返回结果。

关键点:
- 利用归并排序的分治思想，同时在合并过程中统计翻转对。
- 优化时间和空间复杂度，时间复杂度为 O(n log n)，空间复杂度为 O(n)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 归并排序的时间复杂度
空间复杂度: O(n) - 归并排序的空间复杂度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def reverse_pairs(nums: List[int]) -> int:
    """
    函数式接口 - 计算数组中的重要翻转对数量
    
    实现思路:
    使用归并排序，在合并过程中统计满足条件的翻转对。
    
    Args:
        nums: 输入的整数数组
        
    Returns:
        返回数组中的重要翻转对数量
        
    Example:
        >>> reverse_pairs([1,3,2,3,1])
        2
    """
    def merge_sort_and_count(l: int, r: int) -> int:
        if l >= r:
            return 0
        
        mid = (l + r) // 2
        count = merge_sort_and_count(l, mid) + merge_sort_and_count(mid + 1, r)
        
        # 统计满足条件的翻转对
        j = mid + 1
        for i in range(l, mid + 1):
            while j <= r and nums[i] > 2 * nums[j]:
                j += 1
            count += j - (mid + 1)
        
        # 合并两个子数组
        temp = []
        left, right = l, mid + 1
        while left <= mid and right <= r:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= r:
            temp.append(nums[right])
            right += 1
        for k in range(len(temp)):
            nums[l + k] = temp[k]
        
        return count
    
    return merge_sort_and_count(0, len(nums) - 1)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(reverse_pairs)