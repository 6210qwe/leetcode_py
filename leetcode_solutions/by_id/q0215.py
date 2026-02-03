# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 215
标题: Kth Largest Element in an Array
难度: medium
链接: https://leetcode.cn/problems/kth-largest-element-in-an-array/
题目类型: 数组、分治、快速选择、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
215. 数组中的第K个最大元素 - 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。 示例 1: 输入: [3,2,1,5,6,4], k = 2 输出: 5 示例 2: 输入: [3,2,3,1,2,4,5,5,6], k = 4 输出: 4 提示： * 1 <= k <= nums.length <= 105 * -104 <= nums[i] <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快速选择算法（Quick Select），类似快速排序

算法步骤:
1. 使用快速选择算法，每次选择一个pivot
2. 将数组分为小于、等于、大于pivot三部分
3. 根据k的位置决定在哪一部分继续查找
4. 平均时间复杂度O(n)，最坏O(n^2)

关键点:
- 使用快速选择算法
- 时间复杂度平均O(n)，最坏O(n^2)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 平均O(n)，最坏O(n^2)
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import random
from leetcode_solutions.utils.solution import create_solution


def kth_largest_element_in_an_array(nums: List[int], k: int) -> int:
    """
    函数式接口 - 数组中的第K个最大元素
    
    实现思路:
    使用快速选择算法（Quick Select），类似快速排序。
    
    Args:
        nums: 整数数组
        k: 第k大元素的位置
        
    Returns:
        第k个最大的元素
        
    Example:
        >>> kth_largest_element_in_an_array([3, 2, 1, 5, 6, 4], 2)
        5
    """
    def quick_select(left, right, k_smallest):
        """快速选择算法"""
        if left == right:
            return nums[left]
        
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)
        
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quick_select(left, pivot_index - 1, k_smallest)
        else:
            return quick_select(pivot_index + 1, right, k_smallest)
    
    def partition(left, right, pivot_index):
        """分区函数"""
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index
    
    return quick_select(0, len(nums) - 1, len(nums) - k)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(kth_largest_element_in_an_array)
