# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1701
标题: Remove Max Number of Edges to Keep Graph Fully Traversable
难度: hard
链接: https://leetcode.cn/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
题目类型: 并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1579. 保证图可完全遍历 - Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3 种类型的边： * 类型 1：只能由 Alice 遍历。 * 类型 2：只能由 Bob 遍历。 * 类型 3：Alice 和 Bob 都可以遍历。 给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。 返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/09/06/5510ex1.png] 输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]] 输出：2 解释：如果删除 [1,1,2] 和 [1,1,3] 这两条边，Alice 和 Bob 仍然可以完全遍历这个图。再删除任何其他的边都无法保证图可以完全遍历。所以可以删除的最大边数是 2 。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/09/06/5510ex2.png] 输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]] 输出：0 解释：注意，删除任何一条边都会使 Alice 和 Bob 无法完全遍历这个图。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/09/06/5510ex3.png] 输入：n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]] 输出：-1 解释：在当前图中，Alice 无法从其他节点到达节点 4 。类似地，Bob 也不能达到节点 1 。因此，图无法完全遍历。 提示： * 1 <= n <= 10^5 * 1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2) * edges[i].length == 3 * 1 <= edges[i][0] <= 3 * 1 <= edges[i][1] < edges[i][2] <= n * 所有元组 (typei, ui, vi) 互不相同
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
