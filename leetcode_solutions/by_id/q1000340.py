# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000340
标题: 数组中的第 K 个最大元素
难度: medium
链接: https://leetcode.cn/problems/xx4gT2/
题目类型: 数组、分治、快速选择、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 076. 数组中的第 K 个最大元素 - 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 示例 1： 输入：nums = [3,2,1,5,6,4], k = 2 输出：5 示例 2： 输入：nums = [3,2,3,1,2,4,5,5,6], k = 4 输出：4 提示： * 1 <= k <= nums.length <= 104 * -104 <= nums[i] <= 104 注意：本题与主站 215 题相同： https://leetcode.cn/problems/kth-largest-element-in-an-array/ [https://leetcode.cn/problems/kth-largest-element-in-an-array/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 快速选择算法，类似快速排序的分区思想

算法步骤:
1. 使用快速选择算法，随机选择pivot
2. 将数组分为两部分：大于pivot和小于pivot
3. 根据k的位置决定继续在哪个区间查找

关键点:
- 快速选择算法，平均O(n)，最坏O(n^2)
- 也可以使用堆，时间复杂度O(n log k)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 平均情况，最坏O(n^2)
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import random
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_kth_largest(nums: List[int], k: int) -> int:
    """
    函数式接口 - 数组中的第 K 个最大元素
    
    实现思路:
    快速选择算法：使用分区思想找到第k大的元素。
    
    Args:
        nums: 整数数组
        k: 第k大
        
    Returns:
        第k大的元素
        
    Example:
        >>> find_kth_largest([3,2,1,5,6,4], 2)
        5
    """
    def quick_select(left: int, right: int, k: int) -> int:
        """快速选择函数"""
        if left == right:
            return nums[left]
        
        # 随机选择pivot
        pivot_index = random.randint(left, right)
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        # 分区
        i = left
        for j in range(left, right):
            if nums[j] > nums[right]:  # 降序排列
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        
        # 判断pivot的位置
        if i - left + 1 == k:
            return nums[i]
        elif i - left + 1 > k:
            return quick_select(left, i - 1, k)
        else:
            return quick_select(i + 1, right, k - (i - left + 1))
    
    return quick_select(0, len(nums) - 1, k)


Solution = create_solution(find_kth_largest)
