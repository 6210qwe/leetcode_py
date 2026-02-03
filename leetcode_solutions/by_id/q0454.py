# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 454
标题: 4Sum II
难度: medium
链接: https://leetcode.cn/problems/4sum-ii/
题目类型: 数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
454. 四数相加 II - 给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足： * 0 <= i, j, k, l < n * nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0 示例 1： 输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2] 输出：2 解释： 两个元组如下： 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0 示例 2： 输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0] 输出：1 提示： * n == nums1.length * n == nums2.length * n == nums3.length * n == nums4.length * 1 <= n <= 200 * -228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将四个数组分成两组，用哈希表优化

算法步骤:
1. 统计nums1和nums2的所有和，存入哈希表
2. 遍历nums3和nums4的所有和，查找相反数
3. 累加匹配的数量

关键点:
- 分组降低复杂度，从O(n^4)降到O(n^2)
- 使用哈希表快速查找
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - 遍历两个数组对
空间复杂度: O(n^2) - 哈希表存储
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def four_sum_ii(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    """
    函数式接口 - 四数相加 II
    
    实现思路:
    将四个数组分成两组，用哈希表记录前两组的和，然后查找后两组的和的相反数。
    
    Args:
        nums1: 第一个数组
        nums2: 第二个数组
        nums3: 第三个数组
        nums4: 第四个数组
        
    Returns:
        满足条件的元组数量
        
    Example:
        >>> four_sum_ii([1,2], [-2,-1], [-1,2], [0,2])
        2
    """
    # 统计nums1和nums2的所有和
    sum_map = {}
    for num1 in nums1:
        for num2 in nums2:
            s = num1 + num2
            sum_map[s] = sum_map.get(s, 0) + 1
    
    # 统计nums3和nums4的所有和，查找相反数
    count = 0
    for num3 in nums3:
        for num4 in nums4:
            target = -(num3 + num4)
            if target in sum_map:
                count += sum_map[target]
    
    return count


# 自动生成Solution类（无需手动编写）
Solution = create_solution(four_sum_ii)
