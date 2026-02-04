# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2176
标题: Parallel Courses III
难度: hard
链接: https://leetcode.cn/problems/parallel-courses-iii/
题目类型: 图、拓扑排序、数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2050. 并行课程 III - 给你一个整数 n ，表示有 n 节课，课程编号从 1 到 n 。同时给你一个二维整数数组 relations ，其中 relations[j] = [prevCoursej, nextCoursej] ，表示课程 prevCoursej 必须在课程 nextCoursej 之前 完成（先修课的关系）。同时给你一个下标从 0 开始的整数数组 time ，其中 time[i] 表示完成第 (i+1) 门课程需要花费的 月份 数。 请你根据以下规则算出完成所有课程所需要的 最少 月份数： * 如果一门课的所有先修课都已经完成，你可以在 任意 时间开始这门课程。 * 你可以 同时 上 任意门课程 。 请你返回完成所有课程所需要的 最少 月份数。 注意：测试数据保证一定可以完成所有课程（也就是先修课的关系构成一个有向无环图）。 示例 1: [https://assets.leetcode.com/uploads/2021/10/07/ex1.png] 输入：n = 3, relations = [[1,3],[2,3]], time = [3,2,5] 输出：8 解释：上图展示了输入数据所表示的先修关系图，以及完成每门课程需要花费的时间。 你可以在月份 0 同时开始课程 1 和 2 。 课程 1 花费 3 个月，课程 2 花费 2 个月。 所以，最早开始课程 3 的时间是月份 3 ，完成所有课程所需时间为 3 + 5 = 8 个月。 示例 2： [https://assets.leetcode.com/uploads/2021/10/07/ex2.png] 输入：n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5] 输出：12 解释：上图展示了输入数据所表示的先修关系图，以及完成每门课程需要花费的时间。 你可以在月份 0 同时开始课程 1 ，2 和 3 。 在月份 1，2 和 3 分别完成这三门课程。 课程 4 需在课程 3 之后开始，也就是 3 个月后。课程 4 在 3 + 4 = 7 月完成。 课程 5 需在课程 1，2，3 和 4 之后开始，也就是在 max(1,2,3,7) = 7 月开始。 所以完成所有课程所需的最少时间为 7 + 5 = 12 个月。 提示： * 1 <= n <= 5 * 104 * 0 <= relations.length <= min(n * (n - 1) / 2, 5 * 104) * relations[j].length == 2 * 1 <= prevCoursej, nextCoursej <= n * prevCoursej != nextCoursej * 所有的先修课程对 [prevCoursej, nextCoursej] 都是 互不相同 的。 * time.length == n * 1 <= time[i] <= 104 * 先修课程图是一个有向无环图。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序和动态规划来计算完成所有课程所需的最少月份数。

算法步骤:
1. 构建邻接表和入度数组。
2. 初始化一个队列，将所有入度为 0 的节点加入队列。
3. 使用广度优先搜索（BFS）进行拓扑排序，同时维护一个 dp 数组，dp[i] 表示完成课程 i 所需的最少月份数。
4. 对于每个节点，更新其后续节点的 dp 值，并减少其后续节点的入度。如果某个节点的入度变为 0，则将其加入队列。
5. 最终结果为 dp 数组中的最大值。

关键点:
- 使用 BFS 进行拓扑排序。
- 动态规划的思想，通过前驱节点的 dp 值来更新当前节点的 dp 值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是课程数，m 是先修课程关系数。
空间复杂度: O(n + m)，用于存储邻接表、入度数组和 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_time(n: int, relations: List[List[int]], time: List[int]) -> int:
    # 构建邻接表和入度数组
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for prev, next in relations:
        graph[prev - 1].append(next - 1)
        indegree[next - 1] += 1
    
    # 初始化队列和 dp 数组
    queue = [i for i in range(n) if indegree[i] == 0]
    dp = [time[i] for i in range(n)]
    
    # BFS 拓扑排序
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            dp[neighbor] = max(dp[neighbor], dp[node] + time[neighbor])
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return max(dp)


Solution = create_solution(minimum_time)