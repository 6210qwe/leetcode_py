# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3217
标题: Number of Possible Sets of Closing Branches
难度: hard
链接: https://leetcode.cn/problems/number-of-possible-sets-of-closing-branches/
题目类型: 位运算、图、枚举、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2959. 关闭分部的可行集合数目 - 一个公司在全国有 n 个分部，它们之间有的有道路连接。一开始，所有分部通过这些道路两两之间互相可以到达。 公司意识到在分部之间旅行花费了太多时间，所以它们决定关闭一些分部（也可能不关闭任何分部），同时保证剩下的分部之间两两互相可以到达且最远距离不超过 maxDistance 。 两个分部之间的 距离 是通过道路长度之和的 最小值 。 给你整数 n ，maxDistance 和下标从 0 开始的二维整数数组 roads ，其中 roads[i] = [ui, vi, wi] 表示一条从 ui 到 vi 长度为 wi的 无向 道路。 请你返回关闭分部的可行方案数目，满足每个方案里剩余分部之间的最远距离不超过 maxDistance。 注意，关闭一个分部后，与之相连的所有道路不可通行。 注意，两个分部之间可能会有多条道路。 示例 1： [https://assets.leetcode.com/uploads/2023/11/08/example11.png] 输入：n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]] 输出：5 解释：可行的关闭分部方案有： - 关闭分部集合 [2] ，剩余分部为 [0,1] ，它们之间的距离为 2 。 - 关闭分部集合 [0,1] ，剩余分部为 [2] 。 - 关闭分部集合 [1,2] ，剩余分部为 [0] 。 - 关闭分部集合 [0,2] ，剩余分部为 [1] 。 - 关闭分部集合 [0,1,2] ，关闭后没有剩余分部。 总共有 5 种可行的关闭方案。 示例 2： [https://assets.leetcode.com/uploads/2023/11/08/example22.png] 输入：n = 3, maxDistance = 5, roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]] 输出：7 解释：可行的关闭分部方案有： - 关闭分部集合 [] ，剩余分部为 [0,1,2] ，它们之间的最远距离为 4 。 - 关闭分部集合 [0] ，剩余分部为 [1,2] ，它们之间的距离为 2 。 - 关闭分部集合 [1] ，剩余分部为 [0,2] ，它们之间的距离为 2 。 - 关闭分部集合 [0,1] ，剩余分部为 [2] 。 - 关闭分部集合 [1,2] ，剩余分部为 [0] 。 - 关闭分部集合 [0,2] ，剩余分部为 [1] 。 - 关闭分部集合 [0,1,2] ，关闭后没有剩余分部。 总共有 7 种可行的关闭方案。 示例 3： 输入：n = 1, maxDistance = 10, roads = [] 输出：2 解释：可行的关闭分部方案有： - 关闭分部集合 [] ，剩余分部为 [0] 。 - 关闭分部集合 [0] ，关闭后没有剩余分部。 总共有 2 种可行的关闭方案。 提示： * 1 <= n <= 10 * 1 <= maxDistance <= 105 * 0 <= roads.length <= 1000 * roads[i].length == 3 * 0 <= ui, vi <= n - 1 * ui != vi * 1 <= wi <= 1000 * 一开始所有分部之间通过道路互相可以到达。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Floyd-Warshall 算法计算所有节点对之间的最短路径，然后枚举所有可能的关闭分部组合，检查每种组合是否满足条件。

算法步骤:
1. 构建邻接矩阵表示图。
2. 使用 Floyd-Warshall 算法计算所有节点对之间的最短路径。
3. 枚举所有可能的关闭分部组合。
4. 对于每种组合，检查剩余分部之间的最远距离是否不超过 maxDistance。
5. 计算满足条件的组合数量。

关键点:
- 使用 Floyd-Warshall 算法计算所有节点对之间的最短路径。
- 枚举所有可能的关闭分部组合，并检查每种组合是否满足条件。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^3 + 2^n * n^2)
- Floyd-Warshall 算法的时间复杂度是 O(n^3)。
- 枚举所有可能的关闭分部组合的时间复杂度是 O(2^n)，对于每种组合，检查最远距离的时间复杂度是 O(n^2)。

空间复杂度: O(n^2)
- 存储邻接矩阵的空间复杂度是 O(n^2)。
- 其他辅助变量的空间复杂度是 O(1)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(n: int, maxDistance: int, roads: List[List[int]]) -> int:
    """
    函数式接口 - 计算关闭分部的可行集合数目
    """
    # 构建邻接矩阵
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in roads:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)

    # 使用 Floyd-Warshall 算法计算所有节点对之间的最短路径
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 枚举所有可能的关闭分部组合
    def is_valid_subset(subset: List[bool]) -> bool:
        remaining_nodes = [i for i in range(n) if not subset[i]]
        if not remaining_nodes:
            return True
        for i in remaining_nodes:
            for j in remaining_nodes:
                if dist[i][j] > maxDistance:
                    return False
        return True

    count = 0
    for mask in range(1 << n):
        subset = [bool(mask & (1 << i)) for i in range(n)]
        if is_valid_subset(subset):
            count += 1

    return count


Solution = create_solution(solution_function_name)