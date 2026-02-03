# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3517
标题: Shortest Distance After Road Addition Queries I
难度: medium
链接: https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-i/
题目类型: 广度优先搜索、图、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3243. 新增道路查询后的最短距离 I - 给你一个整数 n 和一个二维整数数组 queries。 有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。 queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最短路径的长度。 返回一个数组 answer，对于范围 [0, queries.length - 1] 中的每个 i，answer[i] 是处理完前 i + 1 个查询后，从城市 0 到城市 n - 1 的最短路径的长度。 示例 1： 输入： n = 5, queries = [[2, 4], [0, 2], [0, 4]] 输出： [3, 2, 1] 解释： [https://assets.leetcode.com/uploads/2024/06/28/image8.jpg] 新增一条从 2 到 4 的道路后，从 0 到 4 的最短路径长度为 3。 [https://assets.leetcode.com/uploads/2024/06/28/image9.jpg] 新增一条从 0 到 2 的道路后，从 0 到 4 的最短路径长度为 2。 [https://assets.leetcode.com/uploads/2024/06/28/image10.jpg] 新增一条从 0 到 4 的道路后，从 0 到 4 的最短路径长度为 1。 示例 2： 输入： n = 4, queries = [[0, 3], [0, 2]] 输出： [1, 1] 解释： [https://assets.leetcode.com/uploads/2024/06/28/image11.jpg] 新增一条从 0 到 3 的道路后，从 0 到 3 的最短路径长度为 1。 [https://assets.leetcode.com/uploads/2024/06/28/image12.jpg] 新增一条从 0 到 2 的道路后，从 0 到 3 的最短路径长度仍为 1。 提示： * 3 <= n <= 500 * 1 <= queries.length <= 500 * queries[i].length == 2 * 0 <= queries[i][0] < queries[i][1] < n * 1 < queries[i][1] - queries[i][0] * 查询中没有重复的道路。
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
