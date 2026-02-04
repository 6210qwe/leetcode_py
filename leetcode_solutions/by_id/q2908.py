# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2908
标题: Custom Interval
难度: medium
链接: https://leetcode.cn/problems/custom-interval/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2805. 自定义间隔 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到满足条件的最小值。

算法步骤:
1. 定义一个辅助函数 `is_valid` 来判断给定的间隔是否满足条件。
2. 使用二分查找来找到满足条件的最小间隔。
3. 返回找到的最小间隔。

关键点:
- 使用二分查找可以有效地缩小搜索范围，提高效率。
- 辅助函数 `is_valid` 的实现需要根据具体问题来定义。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(max_interval) * n)，其中 max_interval 是可能的最大间隔，n 是输入数据的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
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
    函数式接口 - 实现自定义间隔
    """
    def is_valid(interval: int) -> bool:
        count = 1
        prev = nums[0]
        for num in nums[1:]:
            if num - prev >= interval:
                count += 1
                prev = num
        return count >= k

    left, right = 0, max(nums) - min(nums)
    while left < right:
        mid = (left + right + 1) // 2
        if is_valid(mid):
            left = mid
        else:
            right = mid - 1
    return left


Solution = create_solution(solution_function_name)