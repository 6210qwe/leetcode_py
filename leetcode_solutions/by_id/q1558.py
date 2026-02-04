# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1558
标题: Course Schedule IV
难度: medium
链接: https://leetcode.cn/problems/course-schedule-iv/
题目类型: 深度优先搜索、广度优先搜索、图、拓扑排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1462. 课程表 IV - 你总共需要上 numCourses 门课，课程编号依次为 0 到 numCourses-1 。你会得到一个数组 prerequisite ，其中 prerequisites[i] = [ai, bi] 表示如果你想选 bi 课程，你 必须 先选 ai 课程。 * 有的课会有直接的先修课程，比如如果想上课程 1 ，你必须先上课程 0 ，那么会以 [0,1] 数对的形式给出先修课程数对。 先决条件也可以是 间接 的。如果课程 a 是课程 b 的先决条件，课程 b 是课程 c 的先决条件，那么课程 a 就是课程 c 的先决条件。 你也得到一个数组 queries ，其中 queries[j] = [uj, vj]。对于第 j 个查询，您应该回答课程 uj 是否是课程 vj 的先决条件。 返回一个布尔数组 answer ，其中 answer[j] 是第 j 个查询的答案。 示例 1： [https://assets.leetcode.com/uploads/2021/05/01/courses4-1-graph.jpg] 输入：numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]] 输出：[false,true] 解释：[1, 0] 数对表示在你上课程 0 之前必须先上课程 1。 课程 0 不是课程 1 的先修课程，但课程 1 是课程 0 的先修课程。 示例 2： 输入：numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]] 输出：[false,false] 解释：没有先修课程对，所以每门课程之间是独立的。 示例 3： [https://assets.leetcode.com/uploads/2021/05/01/courses4-3-graph.jpg] 输入：numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]] 输出：[true,true] 提示： * 2 <= numCourses <= 100 * 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2) * prerequisites[i].length == 2 * 0 <= ai, bi <= numCourses - 1 * ai != bi * 每一对 [ai, bi] 都 不同 * 先修课程图中没有环。 * 1 <= queries.length <= 104 * 0 <= ui, vi <= numCourses - 1 * ui != vi
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用Floyd-Warshall算法计算所有课程之间的传递闭包。

算法步骤:
1. 初始化一个二维数组 `reachable`，表示从课程 i 到课程 j 是否可达。
2. 根据 `prerequisites` 填充 `reachable` 数组。
3. 使用Floyd-Warshall算法更新 `reachable` 数组，计算所有课程之间的传递闭包。
4. 对于每个查询，检查 `reachable` 数组中的对应值。

关键点:
- Floyd-Warshall算法用于计算图的传递闭包。
- 通过传递闭包可以快速判断两个节点之间的可达性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^3)，其中 n 是课程数量。Floyd-Warshall算法的时间复杂度为 O(n^3)。
空间复杂度: O(n^2)，存储 `reachable` 数组所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    # 初始化可达性矩阵
    reachable = [[False] * numCourses for _ in range(numCourses)]
    
    # 根据先修课程填充可达性矩阵
    for pre, course in prerequisites:
        reachable[pre][course] = True
    
    # 使用Floyd-Warshall算法计算传递闭包
    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
    
    # 处理查询
    result = []
    for u, v in queries:
        result.append(reachable[u][v])
    
    return result

Solution = create_solution(checkIfPrerequisite)