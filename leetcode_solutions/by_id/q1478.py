# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1478
标题: Maximum Number of Events That Can Be Attended
难度: medium
链接: https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/
题目类型: 贪心、数组、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1353. 最多可以参加的会议数目 - 给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于 endDayi 。 你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。在任意一天 d 中只能参加一场会议。 请你返回你可以参加的 最大 会议数目。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/16/e1.png] 输入：events = [[1,2],[2,3],[3,4]] 输出：3 解释：你可以参加所有的三个会议。 安排会议的一种方案如上图。 第 1 天参加第一个会议。 第 2 天参加第二个会议。 第 3 天参加第三个会议。 示例 2： 输入：events= [[1,2],[2,3],[3,4],[1,2]] 输出：4 提示： * 1 <= events.length <= 105 * events[i].length == 2 * 1 <= startDayi <= endDayi <= 105
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
