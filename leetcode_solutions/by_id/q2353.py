# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2353
标题: Maximum Score of a Node Sequence
难度: hard
链接: https://leetcode.cn/problems/maximum-score-of-a-node-sequence/
题目类型: 图、数组、枚举、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2242. 节点序列的最大得分 - 给你一个 n 个节点的 无向图 ，节点编号为 0 到 n - 1 。 给你一个下标从 0 开始的整数数组 scores ，其中 scores[i] 是第 i 个节点的分数。同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] ，表示节点 ai 和 bi 之间有一条 无向 边。 一个合法的节点序列如果满足以下条件，我们称它是 合法的 ： * 序列中每 相邻 节点之间有边相连。 * 序列中没有节点出现超过一次。 节点序列的分数定义为序列中节点分数之 和 。 请你返回一个长度为 4 的合法节点序列的最大分数。如果不存在这样的序列，请你返回 -1 。 示例 1： [https://assets.leetcode.com/uploads/2022/04/15/ex1new3.png] 输入：scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]] 输出：24 解释：上图为输入的图，节点序列为 [0,1,2,3] 。 节点序列的分数为 5 + 2 + 9 + 8 = 24 。 观察可知，没有其他节点序列得分和超过 24 。 注意节点序列 [3,1,2,0] 和 [1,0,2,3] 也是合法的，且分数为 24 。 序列 [0,3,2,4] 不是合法的，因为没有边连接节点 0 和 3 。 示例 2： [https://assets.leetcode.com/uploads/2022/03/17/ex2.png] 输入：scores = [9,20,6,4,11,12], edges = [[0,3],[5,3],[2,4],[1,3]] 输出：-1 解释：上图为输入的图。 没有长度为 4 的合法序列，所以我们返回 -1 。 提示： * n == scores.length * 4 <= n <= 5 * 104 * 1 <= scores[i] <= 108 * 0 <= edges.length <= 5 * 104 * edges[i].length == 2 * 0 <= ai, bi <= n - 1 * ai != bi * 不会有重边。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过枚举所有可能的三元组 (a, b, c)，并检查是否存在合法的四元组 (a, b, c, d) 来找到最大分数。

算法步骤:
1. 构建图的邻接表表示。
2. 对于每个节点，维护其前三个最高分邻居。
3. 枚举所有可能的三元组 (a, b, c)，并检查是否存在合法的四元组 (a, b, c, d)。
4. 计算每个合法四元组的分数，并更新最大分数。

关键点:
- 使用邻接表来存储图结构。
- 通过维护每个节点的前三个最高分邻居来减少枚举的复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E + V * log V)，其中 E 是边的数量，V 是节点的数量。
空间复杂度: O(V + E)，用于存储图的邻接表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def maximum_score_of_node_sequence(scores: List[int], edges: List[List[int]]) -> int:
    """
    函数式接口 - 返回长度为 4 的合法节点序列的最大分数
    """
    from collections import defaultdict
    from heapq import heappush, heappop

    # 构建图的邻接表表示
    graph = defaultdict(list)
    for u, v in edges:
        heappush(graph[u], (scores[v], v))
        heappush(graph[v], (scores[u], u))
        if len(graph[u]) > 3:
            heappop(graph[u])
        if len(graph[v]) > 3:
            heappop(graph[v])

    max_score = -1

    # 枚举所有可能的三元组 (a, b, c)
    for b, neighbors in graph.items():
        for score_a, a in neighbors:
            for score_c, c in neighbors:
                if a == c:
                    continue
                for score_d, d in graph[c]:
                    if d != a and d != b:
                        current_score = scores[b] + score_a + score_c + score_d
                        max_score = max(max_score, current_score)

    return max_score


Solution = create_solution(maximum_score_of_node_sequence)