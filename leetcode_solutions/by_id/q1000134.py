# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000134
标题: 追逐游戏
难度: hard
链接: https://leetcode.cn/problems/Za25hA/
题目类型: 深度优先搜索、广度优先搜索、图、拓扑排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 21. 追逐游戏 - 秋游中的小力和小扣设计了一个追逐游戏。他们选了秋日市集景区中的 N 个景点，景点编号为 1~N。此外，他们还选择了 N 条小路，满足任意两个景点之间都可以通过小路互相到达，且不存在两条连接景点相同的小路。整个游戏场景可视作一个无向连通图，记作二维数组 `edges`，数组中以 `[a,b]` 形式表示景点 a 与景点 b 之间有一条小路连通。 小力和小扣只能沿景点间的小路移动。小力的目标是在最快时间内追到小扣，小扣的目标是尽可能延后被小力追到的时间。游戏开始前，两人分别站在两个不同的景点 `startA` 和 `startB`。每一回合，小力先行动，小扣观察到小力的行动后再行动。小力和小扣在每回合可选择以下行动之一： - 移动至相邻景点 - 留在原地 如果小力追到小扣（即两人于某一时刻出现在同一位置），则游戏结束。若小力可以追到小扣，请返回最少需要多少回合；若小力无法追到小扣，请返回 -1。 注意：小力和小扣一定会采取最优移动策略。 **示例 1：** >输入：`edges = [[1,2],[2,3],[3,4],[4,1],[2,5],[5,6]], startA = 3, startB = 5` > >输出：`3` > >解释： >![image.png](https://pic.leetcode.cn/1597991318-goeHHr-image.png){:height="250px"} > >第一回合，小力移动至 2 号点，小扣观察到小力的行动后移动至 6 号点； >第二回合，小力移动至 5 号点，小扣无法移动，留在原地； >第三回合，小力移动至 6 号点，小力追到小扣。返回 3。 **示例 2：** >输入：`edges = [[1,2],[2,3],[3,4],[4,1]], startA = 1, startB = 3` > >输出：`-1` > >解释： >![image.png](https://pic.leetcode.cn/1597991157-QfeakF-image.png){:height="250px"} > >小力如果不动，则小扣也不动；否则小扣移动到小力的对角线位置。这样小力无法追到小扣。 **提示：** - `edges` 的长度等于图中节点个数 - `3 <= edges.length <= 10^5` - `1 <= edges[i][0], edges[i][1] <= edges.length 且 edges[i][0] != edges[i][1]` - `1 <= startA, startB <= edges.length 且 startA != startB`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用 BFS 计算从每个节点出发到其他所有节点的最短距离。
- 通过这些最短距离，模拟小力和小扣的移动过程，计算小力追到小扣所需的最少回合。

算法步骤:
1. 构建图的邻接表表示。
2. 使用 BFS 计算从每个节点出发到其他所有节点的最短距离。
3. 模拟小力和小扣的移动过程，计算小力追到小扣所需的最少回合。

关键点:
- 使用 BFS 计算最短路径。
- 模拟小力和小扣的移动过程，确保小力和小扣都采取最优策略。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N + M)，其中 N 是节点数，M 是边数。构建图和 BFS 计算最短路径的时间复杂度都是 O(N + M)。
空间复杂度: O(N + M)，存储图的邻接表和最短路径的距离矩阵。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import deque
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def bfs_shortest_paths(graph: List[List[int]], start: int) -> List[int]:
    n = len(graph)
    distances = [-1] * n
    queue = deque([start])
    distances[start] = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances


def chase_game(edges: List[List[int]], startA: int, startB: int) -> int:
    n = len(edges) + 1
    graph = [[] for _ in range(n)]
    
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    
    # 计算从每个节点出发到其他所有节点的最短距离
    dist_from_A = bfs_shortest_paths(graph, startA - 1)
    dist_from_B = bfs_shortest_paths(graph, startB - 1)
    
    # 模拟小力和小扣的移动过程
    max_distance = 0
    for i in range(n):
        if dist_from_A[i] < dist_from_B[i]:
            max_distance = max(max_distance, dist_from_B[i])
    
    # 检查是否存在环
    for i in range(n):
        if dist_from_A[i] == dist_from_B[i] and dist_from_A[i] != -1:
            return -1
    
    return max_distance


Solution = create_solution(chase_game)