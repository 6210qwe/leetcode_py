# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2171
标题: Second Minimum Time to Reach Destination
难度: hard
链接: https://leetcode.cn/problems/second-minimum-time-to-reach-destination/
题目类型: 广度优先搜索、图、最短路
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2045. 到达目的地的第二短时间 - 城市用一个 双向连通 图表示，图中有 n 个节点，从 1 到 n 编号（包含 1 和 n）。图中的边用一个二维整数数组 edges 表示，其中每个 edges[i] = [ui, vi] 表示一条节点 ui 和节点 vi 之间的双向连通边。每组节点对由 最多一条 边连通，顶点不存在连接到自身的边。穿过任意一条边的时间是 time 分钟。 每个节点都有一个交通信号灯，每 change 分钟改变一次，从绿色变成红色，再由红色变成绿色，循环往复。所有信号灯都 同时 改变。你可以在 任何时候 进入某个节点，但是 只能 在节点 信号灯是绿色时 才能离开。如果信号灯是 绿色 ，你 不能 在节点等待，必须离开。 第二小的值 是 严格大于 最小值的所有值中最小的值。 * 例如，[2, 3, 4] 中第二小的值是 3 ，而 [2, 2, 4] 中第二小的值是 4 。 给你 n、edges、time 和 change ，返回从节点 1 到节点 n 需要的 第二短时间 。 注意： * 你可以 任意次 穿过任意顶点，包括 1 和 n 。 * 你可以假设在 启程时 ，所有信号灯刚刚变成 绿色 。 示例 1： [https://assets.leetcode.com/uploads/2021/09/29/e1.png] [https://assets.leetcode.com/uploads/2021/09/29/e2.png] 输入：n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5 输出：13 解释： 上面的左图展现了给出的城市交通图。 右图中的蓝色路径是最短时间路径。 花费的时间是： - 从节点 1 开始，总花费时间=0 - 1 -> 4：3 分钟，总花费时间=3 - 4 -> 5：3 分钟，总花费时间=6 因此需要的最小时间是 6 分钟。 右图中的红色路径是第二短时间路径。 - 从节点 1 开始，总花费时间=0 - 1 -> 3：3 分钟，总花费时间=3 - 3 -> 4：3 分钟，总花费时间=6 - 在节点 4 等待 4 分钟，总花费时间=10 - 4 -> 5：3 分钟，总花费时间=13 因此第二短时间是 13 分钟。 示例 2： [https://assets.leetcode.com/uploads/2021/09/29/eg2.png] 输入：n = 2, edges = [[1,2]], time = 3, change = 2 输出：11 解释： 最短时间路径是 1 -> 2 ，总花费时间 = 3 分钟 第二短时间路径是 1 -> 2 -> 1 -> 2 ，总花费时间 = 11 分钟 提示： * 2 <= n <= 104 * n - 1 <= edges.length <= min(2 * 104, n * (n - 1) / 2) * edges[i].length == 2 * 1 <= ui, vi <= n * ui != vi * 不含重复边 * 每个节点都可以从其他节点直接或者间接到达 * 1 <= time, change <= 103
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从起点到终点的第二短路径。通过维护两个队列，一个用于当前层的节点，另一个用于下一层的节点，并记录每个节点的访问次数。

算法步骤:
1. 构建图的邻接表表示。
2. 初始化两个队列，一个用于当前层的节点，另一个用于下一层的节点。
3. 使用BFS遍历图，记录每个节点的访问次数和到达时间。
4. 当到达终点时，记录第一次和第二次到达的时间。
5. 返回第二次到达的时间。

关键点:
- 使用两个队列分别存储当前层和下一层的节点。
- 记录每个节点的访问次数，确保每个节点最多访问两次。
- 处理信号灯的变化，计算等待时间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是节点数，m 是边数。因为每个节点最多访问两次，每条边最多访问两次。
空间复杂度: O(n + m)，存储图的邻接表和队列所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import deque
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def second_minimum_time_to_reach_destination(n: int, edges: List[List[int]], time: int, change: int) -> int:
    # 构建图的邻接表
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 初始化队列和访问计数
    queue = deque([(1, 0)])  # (节点, 时间)
    visited = [0] * (n + 1)
    visited[1] = 1
    first_time, second_time = None, None

    while queue:
        next_queue = deque()
        while queue:
            node, t = queue.popleft()

            # 计算下一个节点的时间
            for neighbor in graph[node]:
                if visited[neighbor] < 2:
                    new_time = t + time
                    if (t // change) % 2 == 1:
                        new_time += change - (t % change)

                    if neighbor == n:
                        if first_time is None:
                            first_time = new_time
                        elif new_time > first_time and (second_time is None or new_time < second_time):
                            second_time = new_time
                    else:
                        next_queue.append((neighbor, new_time))
                        visited[neighbor] += 1

        queue = next_queue

    return second_time


Solution = create_solution(second_minimum_time_to_reach_destination)