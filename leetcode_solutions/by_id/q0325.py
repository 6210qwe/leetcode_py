# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 325
标题: Maximum Size Subarray Sum Equals k
难度: medium
链接: https://leetcode.cn/problems/maximum-size-subarray-sum-equals-k/
题目类型: 数组、哈希表、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
325. 和等于 k 的最长子数组长度 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 前缀和+哈希表，记录前缀和第一次出现的位置

算法步骤:
1. 计算前缀和
2. 使用哈希表记录前缀和第一次出现的位置
3. 如果prefix_sum - k在哈希表中，更新最大长度

关键点:
- 前缀和
- 哈希表
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历数组一次
空间复杂度: O(n) - 哈希表空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_sub_array_len(nums: List[int], k: int) -> int:
    """
    函数式接口 - 和等于 k 的最长子数组长度
    
    实现思路:
    前缀和+哈希表：记录前缀和第一次出现的位置。
    
    Args:
        nums: 整数数组
        k: 目标和
        
    Returns:
        最长子数组长度
        
    Example:
        >>> max_sub_array_len([1,-1,5,-2,3], 3)
        4
    """
    prefix_sum = 0
    prefix_map = {0: -1}  # 前缀和为0的位置是-1
    max_len = 0
    
    for i, num in enumerate(nums):
        prefix_sum += num
        
        if prefix_sum - k in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum - k])
        
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
    
    return max_len


# 自动生成Solution类（无需手动编写）
Solution = create_solution(max_sub_array_len)
