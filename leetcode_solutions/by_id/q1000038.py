# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000038
标题: Find Majority Element LCCI
难度: easy
链接: https://leetcode.cn/problems/find-majority-element-lcci/
题目类型: 数组、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.10. 主要元素 - 数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。 示例 1： 输入：[1,2,5,9,5,9,5,5,5] 输出：5 示例 2： 输入：[3,2] 输出：-1 示例 3： 输入：[2,2,1,1,1,2,2] 输出：2
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Boyer-Moore 投票算法来找到主要元素。

算法步骤:
1. 初始化候选元素和计数器。
2. 遍历数组，更新候选元素和计数器。
3. 检查候选元素是否为主要元素。

关键点:
- Boyer-Moore 投票算法能够在 O(N) 时间复杂度和 O(1) 空间复杂度内找到主要元素。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 使用 Boyer-Moore 投票算法找到主要元素
    """
    if not nums:
        return -1

    # Step 1: Find the candidate
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Step 2: Verify the candidate
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return -1


Solution = create_solution(solution_function_name)