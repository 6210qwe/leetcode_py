# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3003
标题: Status of Flight Tickets
难度: hard
链接: https://leetcode.cn/problems/status-of-flight-tickets/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2793. 航班机票状态 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序来判断是否有环。如果存在环，则说明有重复的机票。

算法步骤:
1. 构建图和入度数组。
2. 初始化队列，将所有入度为0的节点加入队列。
3. 进行拓扑排序，如果在排序过程中发现环，则返回 False。
4. 如果所有节点都被访问过且没有发现环，则返回 True。

关键点:
- 使用拓扑排序来检测图中是否存在环。
- 通过入度数组来判断节点是否可以加入队列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(V + E)，其中 V 是节点数（机场数量），E 是边数（机票数量）。
空间复杂度: O(V + E)，存储图和入度数组的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    判断给定的课程安排是否合理，即是否存在环。
    
    :param numCourses: 课程数量
    :param prerequisites: 课程先修关系
    :return: 是否可以完成所有课程
    """
    # 构建图和入度数组
    graph = [[] for _ in range(numCourses)]
    in_degree = [0] * numCourses
    
    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1
    
    # 初始化队列，将所有入度为0的节点加入队列
    queue = [i for i in range(numCourses) if in_degree[i] == 0]
    
    # 拓扑排序
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 如果所有节点都被访问过且没有发现环，则返回 True
    return sum(in_degree) == 0


Solution = create_solution(canFinish)