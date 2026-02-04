# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000310
标题: 课程表 II
难度: medium
链接: https://leetcode.cn/problems/QA2IGt/
题目类型: 深度优先搜索、广度优先搜索、图、拓扑排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 113. 课程表 II - 现在总共有 numCourses 门课需要选，记为 0 到 numCourses-1。 给定一个数组 prerequisites ，它的每一个元素 prerequisites[i] 表示两门课程之间的先修顺序。 例如 prerequisites[i] = [ai, bi] 表示想要学习课程 ai ，需要先完成课程 bi 。 请根据给出的总课程数 numCourses 和表示先修顺序的 prerequisites 得出一个可行的修课序列。 可能会有多个正确的顺序，只要任意返回一种就可以了。如果不可能完成所有课程，返回一个空数组。 示例 1： 输入: numCourses = 2, prerequisites = [[1,0]] 输出: [0,1] 解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1]。 示例 2： 输入: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] 输出: [0,1,2,3] or [0,2,1,3] 解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。因此，一个正确的课程顺序是 [0,1,2,3]。另一个正确的排序是 [0,2,1,3]。 示例 3： 输入: numCourses = 1, prerequisites = [] 输出: [0] 解释: 总共 1 门课，直接修第一门课就可。 提示： * 1 <= numCourses <= 2000 * 0 <= prerequisites.length <= numCourses * (numCourses - 1) * prerequisites[i].length == 2 * 0 <= ai, bi < numCourses * ai != bi * prerequisites 中不存在重复元素 注意：本题与主站 210 题相同：https://leetcode.cn/problems/course-schedule-ii/ [https://leetcode.cn/problems/course-schedule-ii/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序来解决这个问题。拓扑排序可以用来检测有向图中是否存在环，并且可以生成一个线性序列。

算法步骤:
1. 构建图的邻接表表示和入度数组。
2. 初始化队列，将所有入度为 0 的节点加入队列。
3. 进行广度优先搜索（BFS），每次从队列中取出一个节点，将其加入结果列表，并减少其邻接节点的入度。
4. 如果某个邻接节点的入度变为 0，则将其加入队列。
5. 最后检查结果列表的长度是否等于课程总数，如果是则返回结果列表，否则返回空列表。

关键点:
- 使用拓扑排序来检测环并生成修课顺序。
- 入度为 0 的节点表示没有先修课程，可以直接学习。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(V + E)，其中 V 是课程数量，E 是先修关系的数量。
空间复杂度: O(V + E)，用于存储图的邻接表和入度数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import deque, defaultdict


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # 构建图的邻接表表示
    graph = defaultdict(list)
    # 记录入度
    in_degree = [0] * numCourses
    
    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1
    
    # 初始化队列，将所有入度为 0 的节点加入队列
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 检查结果列表的长度是否等于课程总数
    return result if len(result) == numCourses else []

Solution = create_solution(findOrder)