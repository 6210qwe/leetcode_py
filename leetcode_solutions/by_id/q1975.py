# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1975
标题: Minimum Distance to the Target Element
难度: easy
链接: https://leetcode.cn/problems/minimum-distance-to-the-target-element/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1848. 到目标元素的最小距离 - 给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数 target 和 start ，请你找出一个下标 i ，满足 nums[i] == target 且 abs(i - start) 最小化 。注意：abs(x) 表示 x 的绝对值。 返回 abs(i - start) 。 题目数据保证 target 存在于 nums 中。 示例 1： 输入：nums = [1,2,3,4,5], target = 5, start = 3 输出：1 解释：nums[4] = 5 是唯一一个等于 target 的值，所以答案是 abs(4 - 3) = 1 。 示例 2： 输入：nums = [1], target = 1, start = 0 输出：0 解释：nums[0] = 1 是唯一一个等于 target 的值，所以答案是 abs(0 - 0) = 0 。 示例 3： 输入：nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0 输出：0 解释：nums 中的每个值都是 1 ，但 nums[0] 使 abs(i - start) 的结果得以最小化，所以答案是 abs(0 - 0) = 0 。 提示： * 1 <= nums.length <= 1000 * 1 <= nums[i] <= 104 * 0 <= start < nums.length * target 存在于 nums 中
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
