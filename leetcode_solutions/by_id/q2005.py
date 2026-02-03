# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2005
标题: Check if All the Integers in a Range Are Covered
难度: easy
链接: https://leetcode.cn/problems/check-if-all-the-integers-in-a-range-are-covered/
题目类型: 数组、哈希表、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1893. 检查是否区域内所有整数都被覆盖 - 给你一个二维整数数组 ranges 和两个整数 left 和 right 。每个 ranges[i] = [starti, endi] 表示一个从 starti 到 endi 的 闭区间 。 如果闭区间 [left, right] 内每个整数都被 ranges 中 至少一个 区间覆盖，那么请你返回 true ，否则返回 false 。 已知区间 ranges[i] = [starti, endi] ，如果整数 x 满足 starti <= x <= endi ，那么我们称整数x 被覆盖了。 示例 1： 输入：ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5 输出：true 解释：2 到 5 的每个整数都被覆盖了： - 2 被第一个区间覆盖。 - 3 和 4 被第二个区间覆盖。 - 5 被第三个区间覆盖。 示例 2： 输入：ranges = [[1,10],[10,20]], left = 21, right = 21 输出：false 解释：21 没有被任何一个区间覆盖。 提示： * 1 <= ranges.length <= 50 * 1 <= starti <= endi <= 50 * 1 <= left <= right <= 50
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
