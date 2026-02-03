# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4
标题: Median of Two Sorted Arrays
难度: hard
链接: https://leetcode.cn/problems/median-of-two-sorted-arrays/
题目类型: 数组、二分查找、分治
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
4. 寻找两个正序数组的中位数 - 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。 算法的时间复杂度应该为 O(log (m+n)) 。 示例 1： 输入：nums1 = [1,3], nums2 = [2] 输出：2.00000 解释：合并数组 = [1,2,3] ，中位数 2 示例 2： 输入：nums1 = [1,2], nums2 = [3,4] 输出：2.50000 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5 提示： * nums1.length == m * nums2.length == n * 0 <= m <= 1000 * 0 <= n <= 1000 * 1 <= m + n <= 2000 * -106 <= nums1[i], nums2[i] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 二分查找，在两个有序数组中寻找分割点，使得分割点左侧的元素个数等于右侧

算法步骤:
1. 确保nums1是较短的数组（如果不是则交换），这样可以减少二分查找的范围
2. 在nums1中二分查找分割点i，使得nums2中对应的分割点j满足：
   - i + j = (m + n + 1) // 2（左侧元素个数）
   - nums1[i-1] <= nums2[j] 且 nums2[j-1] <= nums1[i]
3. 根据总元素个数的奇偶性返回中位数：
   - 奇数：max(nums1[i-1], nums2[j-1])
   - 偶数：(max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j])) / 2

关键点:
- 使用二分查找在较短的数组上查找分割点，时间复杂度O(log(min(m,n)))
- 分割点满足：左侧所有元素 <= 右侧所有元素
- 需要处理边界情况：i=0, i=m, j=0, j=n
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(min(m, n))) - 二分查找在较短的数组上进行
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    函数式接口 - 二分查找实现
    
    实现思路:
    在两个有序数组中寻找分割点，使得分割点左侧的元素个数等于右侧，从而找到中位数。
    
    Args:
        nums1: 第一个有序数组
        nums2: 第二个有序数组
        
    Returns:
        两个数组的中位数
        
    Example:
        >>> find_median_sorted_arrays([1, 3], [2])
        2.0
        >>> find_median_sorted_arrays([1, 2], [3, 4])
        2.5
    """
    # 确保nums1是较短的数组
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    total_left = (m + n + 1) // 2  # 左侧应该有的元素个数
    
    while left < right:
        i = (left + right + 1) // 2  # nums1的分割点
        j = total_left - i  # nums2的分割点
        
        if nums1[i - 1] > nums2[j]:
            # nums1左侧最大值太大，需要减小i
            right = i - 1
        else:
            # nums1左侧最大值合适，尝试增大i
            left = i
    
    i = left
    j = total_left - i
    
    # 处理边界情况
    nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
    nums1_right_min = float('inf') if i == m else nums1[i]
    nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
    nums2_right_min = float('inf') if j == n else nums2[j]
    
    if (m + n) % 2 == 1:
        # 奇数个元素，返回左侧最大值
        return float(max(nums1_left_max, nums2_left_max))
    else:
        # 偶数个元素，返回左侧最大值和右侧最小值的平均
        return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0


# 自动生成Solution类（无需手动编写）
Solution = create_solution(find_median_sorted_arrays)
