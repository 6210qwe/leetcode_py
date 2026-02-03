# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 327
标题: Count of Range Sum
难度: hard
链接: https://leetcode.cn/problems/count-of-range-sum/
题目类型: 树状数组、线段树、数组、二分查找、分治、有序集合、归并排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
327. 区间和的个数 - 给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 区间和的个数 。 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。 示例 1： 输入：nums = [-2,5,-1], lower = -2, upper = 2 输出：3 解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。 示例 2： 输入：nums = [0], lower = 0, upper = 0 输出：1 提示： * 1 <= nums.length <= 105 * -231 <= nums[i] <= 231 - 1 * -105 <= lower <= upper <= 105 * 题目数据保证答案是一个 32 位 的整数
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 前缀和+归并排序，在归并过程中统计满足条件的区间

算法步骤:
1. 计算前缀和数组
2. 使用归并排序，在归并过程中统计
3. 对于左半部分的每个前缀和，在右半部分找满足条件的范围

关键点:
- 前缀和
- 归并排序
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 归并排序
空间复杂度: O(n) - 辅助数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_range_sum(nums: List[int], lower: int, upper: int) -> int:
    """
    函数式接口 - 区间和的个数
    
    实现思路:
    前缀和+归并排序：在归并过程中统计满足条件的区间。
    
    Args:
        nums: 整数数组
        lower: 下界
        upper: 上界
        
    Returns:
        满足条件的区间个数
        
    Example:
        >>> count_range_sum([-2,5,-1], -2, 2)
        3
    """
    # 计算前缀和
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    
    count = [0]
    
    def merge_sort(left: int, right: int):
        """归并排序"""
        if left >= right:
            return
        
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        
        # 统计满足条件的区间
        i, j = mid + 1, mid + 1
        for k in range(left, mid + 1):
            # 找到满足prefix[j] - prefix[k] >= lower的最小j
            while i <= right and prefix[i] - prefix[k] < lower:
                i += 1
            # 找到满足prefix[j] - prefix[k] <= upper的最大j
            while j <= right and prefix[j] - prefix[k] <= upper:
                j += 1
            count[0] += j - i
        
        # 归并
        merged = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if prefix[i] <= prefix[j]:
                merged.append(prefix[i])
                i += 1
            else:
                merged.append(prefix[j])
                j += 1
        
        while i <= mid:
            merged.append(prefix[i])
            i += 1
        while j <= right:
            merged.append(prefix[j])
            j += 1
        
        prefix[left:right+1] = merged
    
    merge_sort(0, len(prefix) - 1)
    return count[0]


# 自动生成Solution类（无需手动编写）
Solution = create_solution(count_range_sum)
