# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1101
标题: Parallel Courses
难度: medium
链接: https://leetcode.cn/problems/parallel-courses/
题目类型: 图、拓扑排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1136. 并行课程 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序判断课程是否可以并行完成。

算法步骤:
1. 构建图的邻接表表示和入度数组。
2. 初始化一个队列，将所有入度为0的节点加入队列。
3. 进行拓扑排序，每轮从队列中取出一个节点，并将其邻居节点的入度减1。如果某个邻居节点的入度变为0，则将其加入队列。
4. 如果所有节点都被处理过，则返回学期数；否则返回-1，表示无法完成所有课程。

关键点:
- 使用队列进行广度优先搜索（BFS）来实现拓扑排序。
- 通过入度数组记录每个节点的入度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是课程数量，m 是先修关系的数量。
空间复杂度: O(n + m)，用于存储图的邻接表和入度数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> int:
    """
    判断是否可以在给定的先修关系下完成所有课程，并返回所需的最少学期数。
    """
    # 构建图的邻接表表示
    graph = [[] for _ in range(numCourses)]
    # 入度数组
    in_degree = [0] * numCourses
    
    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1
    
    # 初始化队列，将所有入度为0的节点加入队列
    queue = [i for i in range(numCourses) if in_degree[i] == 0]
    
    # 拓扑排序
    semester = 0
    while queue:
        next_queue = []
        for node in queue:
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    next_queue.append(neighbor)
        queue = next_queue
        semester += 1
    
    # 如果所有节点都被处理过，则返回学期数；否则返回-1
    return semester if sum(in_degree) == 0 else -1


Solution = create_solution(canFinish)