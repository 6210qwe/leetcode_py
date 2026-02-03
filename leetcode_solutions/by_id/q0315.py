# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 315
标题: Count of Smaller Numbers After Self
难度: hard
链接: https://leetcode.cn/problems/count-of-smaller-numbers-after-self/
题目类型: 树状数组、线段树、数组、二分查找、分治、有序集合、归并排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
315. 计算右侧小于当前元素的个数 - 给你一个整数数组 nums ，按要求返回一个新数组 counts 。数组 counts 有该性质： counts[i] 的值是 nums[i] 右侧小于 nums[i] 的元素的数量。 示例 1： 输入：nums = [5,2,6,1] 输出：[2,1,1,0] 解释： 5 的右侧有 2 个更小的元素 (2 和 1) 2 的右侧仅有 1 个更小的元素 (1) 6 的右侧有 1 个更小的元素 (1) 1 的右侧有 0 个更小的元素 示例 2： 输入：nums = [-1] 输出：[0] 示例 3： 输入：nums = [-1,-1] 输出：[0,0] 提示： * 1 <= nums.length <= 105 * -104 <= nums[i] <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用归并排序，在归并过程中统计右侧小于当前元素的个数

算法步骤:
1. 使用归并排序，同时记录每个元素的原始索引
2. 在归并过程中，当右半部分的元素小于左半部分的元素时，统计数量
3. 更新结果数组

关键点:
- 使用归并排序统计逆序对
- 时间复杂度O(nlogn)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(nlogn) - 归并排序的时间复杂度
空间复杂度: O(n) - 临时数组空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def count_of_smaller_numbers_after_self(nums: List[int]) -> List[int]:
    """
    函数式接口 - 计算右侧小于当前元素的个数
    
    实现思路:
    使用归并排序，在归并过程中统计右侧小于当前元素的个数。
    
    Args:
        nums: 整数数组
        
    Returns:
        每个元素右侧小于它的元素个数数组
        
    Example:
        >>> count_of_smaller_numbers_after_self([5, 2, 6, 1])
        [2, 1, 1, 0]
    """
    n = len(nums)
    result = [0] * n
    indices = list(range(n))
    
    def merge_sort(left: int, right: int):
        """归并排序"""
        if left >= right:
            return
        
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        merge(left, mid, right)
    
    def merge(left: int, mid: int, right: int):
        """合并两个有序数组"""
        temp = []
        i, j = left, mid + 1
        right_count = 0
        
        while i <= mid and j <= right:
            if nums[indices[i]] <= nums[indices[j]]:
                result[indices[i]] += right_count
                temp.append(indices[i])
                i += 1
            else:
                right_count += 1
                temp.append(indices[j])
                j += 1
        
        while i <= mid:
            result[indices[i]] += right_count
            temp.append(indices[i])
            i += 1
        
        while j <= right:
            temp.append(indices[j])
            j += 1
        
        for k in range(len(temp)):
            indices[left + k] = temp[k]
    
    merge_sort(0, n - 1)
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(count_of_smaller_numbers_after_self)
