# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 399
标题: Evaluate Division
难度: medium
链接: https://leetcode.cn/problems/evaluate-division/
题目类型: 深度优先搜索、广度优先搜索、并查集、图、数组、字符串、最短路
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
399. 除法求值 - 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。 注意：未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。 示例 1： 输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]] 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000] 解释： 条件：a / b = 2.0, b / c = 3.0 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 结果：[6.0, 0.5, -1.0, 1.0, -1.0 ] 注意：x 是未定义的 => -1.0 示例 2： 输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]] 输出：[3.75000,0.40000,5.00000,0.20000] 示例 3： 输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]] 输出：[0.50000,2.00000,-1.00000,-1.00000] 提示： * 1 <= equations.length <= 20 * equations[i].length == 2 * 1 <= Ai.length, Bi.length <= 5 * values.length == equations.length * 0.0 < values[i] <= 20.0 * 1 <= queries.length <= 20 * queries[i].length == 2 * 1 <= Cj.length, Dj.length <= 5 * Ai, Bi, Cj, Dj 由小写英文字母与数字组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将等式 Ai/Bi = value 看作带权有向边，构建图后用 BFS/DFS 在图上查询两个变量间的乘积路径。

算法步骤:
1. 遍历 equations 和 values，构建邻接表 `graph`：
   - 对每个等式 a/b = v，添加边 a->b 权重 v，b->a 权重 1/v。
2. 对于每个查询 (src, dst)：
   - 若任一变量不在图中，答案为 -1.0。
   - 若 src==dst，且存在于图中，答案为 1.0。
   - 否则从 src 出发做 BFS/DFS，搜索到 dst 为止，并在路径上累乘边权，找到则返回该积；找不到则返回 -1.0。

关键点:
- 图中权值满足乘法传递性：a/c = (a/b) * (b/c)。 
- 变量个数和等式条数都很小，用 BFS/DFS 搜索即可满足效率要求。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 构图 O(E)，E 为等式条数；每个查询最坏遍历整张图 O(V+E)，V 为变量个数。
空间复杂度: O(V+E)，存储图的邻接表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def evaluate_division(
    equations: List[List[str]], values: List[float], queries: List[List[str]]
) -> List[float]:
    """
    根据等式 Ai/Bi = values[i] 以及查询 Cj/Dj 计算结果。

    构建带权有向图，权值表示除法结果，对每个查询用 DFS 搜索并累乘路径上的权值。
    """
    from collections import defaultdict, deque

    graph: dict[str, list[tuple[str, float]]] = defaultdict(list)
    for (a, b), v in zip(equations, values):
        graph[a].append((b, v))
        graph[b].append((a, 1.0 / v))

    def bfs(src: str, dst: str) -> float:
        if src not in graph or dst not in graph:
            return -1.0
        if src == dst:
            return 1.0
        q = deque([(src, 1.0)])
        seen = {src}
        while q:
            x, val = q.popleft()
            if x == dst:
                return val
            for y, w in graph[x]:
                if y not in seen:
                    seen.add(y)
                    q.append((y, val * w))
        return -1.0

    return [bfs(a, b) for a, b in queries]


# 自动生成Solution类（无需手动编写）
Solution = create_solution(evaluate_division)
