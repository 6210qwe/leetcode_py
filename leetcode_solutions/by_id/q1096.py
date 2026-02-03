# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1096
标题: Maximum Sum of Two Non-Overlapping Subarrays
难度: medium
链接: https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/
题目类型: 数组、动态规划、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1031. 两个无重叠子数组的最大和 - 给你一个整数数组 nums 和两个整数 firstLen 和 secondLen，请你找出并返回两个无重叠 子数组 中元素的最大和，长度分别为 firstLen 和 secondLen 。 长度为 firstLen 的子数组可以出现在长为 secondLen 的子数组之前或之后，但二者必须是无重叠。 子数组是数组的一个 连续 部分。 示例 1： 输入：nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2 输出：20 解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。 示例 2： 输入：nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2 输出：29 解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。 示例 3： 输入：nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3 输出：31 解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。 提示： * 1 <= firstLen, secondLen <= 1000 * 2 <= firstLen + secondLen <= 1000 * firstLen + secondLen <= nums.length <= 1000 * 0 <= nums[i] <= 1000
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
