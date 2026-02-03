# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 745
标题: Find Smallest Letter Greater Than Target
难度: easy
链接: https://leetcode.cn/problems/find-smallest-letter-greater-than-target/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
744. 寻找比目标字母大的最小字母 - 给你一个字符数组 letters，该数组按非递减顺序排序，以及一个字符 target。letters 里至少有两个不同的字符。 返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。 示例 1： 输入: letters = ['c', 'f', 'j']，target = 'a' 输出: 'c' 解释：letters 中字典上比 'a' 大的最小字符是 'c'。 示例 2: 输入: letters = ['c','f','j'], target = 'c' 输出: 'f' 解释：letters 中字典顺序上大于 'c' 的最小字符是 'f'。 示例 3: 输入: letters = ['x','x','y','y'], target = 'z' 输出: 'x' 解释：letters 中没有一个字符在字典上大于 'z'，所以我们返回 letters[0]。 提示： * 2 <= letters.length <= 104 * letters[i] 是一个小写字母 * letters 按非递减顺序排序 * letters 最少包含两个不同的字母 * target 是一个小写字母
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
