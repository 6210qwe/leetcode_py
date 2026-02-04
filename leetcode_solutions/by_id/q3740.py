# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3740
标题: Maximum Number of Matching Indices After Right Shifts
难度: medium
链接: https://leetcode.cn/problems/maximum-number-of-matching-indices-after-right-shifts/
题目类型: 数组、双指针、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一个整数数组 nums 和一个整数 k，你需要对数组进行最多 k 次右移操作。每次右移操作会将数组的最后一个元素移动到数组的第一个位置。返回在所有可能的右移操作后，数组中匹配索引的最大数量。匹配索引是指数组中下标 i 的值等于 nums[i]。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针和滑动窗口来计算最大匹配索引数。

算法步骤:
1. 初始化一个长度为 n 的布尔数组 match，用于记录每个索引是否是匹配索引。
2. 遍历数组，填充 match 数组。
3. 使用滑动窗口技术，计算在 k 次右移操作内的最大匹配索引数。

关键点:
- 使用布尔数组来记录匹配索引。
- 通过滑动窗口技术来高效计算最大匹配索引数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], k: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    n = len(nums)
    match = [False] * n
    
    # 填充 match 数组
    for i in range(n):
        if i == nums[i]:
            match[i] = True
    
    # 计算初始窗口内的匹配索引数
    max_matches = current_matches = sum(match[:k])
    
    # 使用滑动窗口技术
    for i in range(k, n + k):
        if match[i % n]:
            current_matches += 1
        if match[(i - k) % n]:
            current_matches -= 1
        max_matches = max(max_matches, current_matches)
    
    return max_matches


Solution = create_solution(solution_function_name)