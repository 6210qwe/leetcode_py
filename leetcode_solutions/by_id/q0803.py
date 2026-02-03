# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 803
标题: Cheapest Flights Within K Stops
难度: medium
链接: https://leetcode.cn/problems/cheapest-flights-within-k-stops/
题目类型: 深度优先搜索、广度优先搜索、图、动态规划、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
787. K 站中转内最便宜的航班 - 有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。 示例 1： [https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png] 输入: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1 输出: 700 解释: 城市航班图如上 从城市 0 到城市 3 经过最多 1 站的最佳路径用红色标记，费用为 100 + 600 = 700。 请注意，通过城市 [0, 1, 2, 3] 的路径更便宜，但无效，因为它经过了 2 站。 示例 2： [https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-1drawio.png] 输入: n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1 输出: 200 解释: 城市航班图如上 从城市 0 到城市 2 经过最多 1 站的最佳路径标记为红色，费用为 100 + 100 = 200。 示例 3： [https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-2drawio.png] 输入：n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0 输出：500 解释： 城市航班图如上 从城市 0 到城市 2 不经过站点的最佳路径标记为红色，费用为 500。 提示： * 2 <= n <= 100 * 0 <= flights.length <= (n * (n - 1) / 2) * flights[i].length == 3 * 0 <= fromi, toi < n * fromi != toi * 1 <= pricei <= 104 * 航班没有重复，且不存在自环 * 0 <= src, dst, k < n * src != dst
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
