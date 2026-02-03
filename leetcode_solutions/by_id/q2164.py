# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2164
标题: Two Best Non-Overlapping Events
难度: medium
链接: https://leetcode.cn/problems/two-best-non-overlapping-events/
题目类型: 数组、二分查找、动态规划、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2054. 两个最好的不重叠活动 - 给你一个下标从 0 开始的二维整数数组 events ，其中 events[i] = [startTimei, endTimei, valuei] 。第 i 个活动开始于 startTimei ，结束于 endTimei ，如果你参加这个活动，那么你可以得到价值 valuei 。你 最多 可以参加 两个时间不重叠 活动，使得它们的价值之和 最大 。 请你返回价值之和的 最大值 。 注意，活动的开始时间和结束时间是 包括 在活动时间内的，也就是说，你不能参加两个活动且它们之一的开始时间等于另一个活动的结束时间。更具体的，如果你参加一个活动，且结束时间为 t ，那么下一个活动必须在 t + 1 或之后的时间开始。 示例 1: [https://assets.leetcode.com/uploads/2026/01/03/untitled-diagramdrawio.png] 输入：events = [[1,3,2],[4,5,2],[2,4,3]] 输出：4 解释：选择绿色的活动 0 和 1 ，价值之和为 2 + 2 = 4 。 示例 2： Example 1 Diagram [https://assets.leetcode.com/uploads/2026/01/03/2054b.png] 输入：events = [[1,3,2],[4,5,2],[1,5,5]] 输出：5 解释：选择活动 2 ，价值和为 5 。 示例 3： [https://assets.leetcode.com/uploads/2026/01/03/2054c.png] 输入：events = [[1,5,3],[1,5,1],[6,6,5]] 输出：8 解释：选择活动 0 和 2 ，价值之和为 3 + 5 = 8 。 提示： * 2 <= events.length <= 105 * events[i].length == 3 * 1 <= startTimei <= endTimei <= 109 * 1 <= valuei <= 106
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
