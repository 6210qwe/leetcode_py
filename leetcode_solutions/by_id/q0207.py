# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 207
标题: Course Schedule
难度: medium
链接: https://leetcode.cn/problems/course-schedule/
题目类型: 深度优先搜索、广度优先搜索、图、拓扑排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
207. 课程表 - 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程 bi 。 * 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。 示例 1： 输入：numCourses = 2, prerequisites = [[1,0]] 输出：true 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。 示例 2： 输入：numCourses = 2, prerequisites = [[1,0],[0,1]] 输出：false 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。 提示： * 1 <= numCourses <= 2000 * 0 <= prerequisites.length <= 5000 * prerequisites[i].length == 2 * 0 <= ai, bi < numCourses * prerequisites[i] 中的所有课程对 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序检测是否有环，如果有环则无法完成所有课程

算法步骤:
1. 构建邻接表和入度数组
2. 将所有入度为0的节点加入队列
3. 从队列中取出节点，减少其邻居节点的入度
4. 如果所有节点都被访问，说明无环，返回True

关键点:
- 使用拓扑排序检测环
- 时间复杂度O(V+E)，空间复杂度O(V+E)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(V+E) - V为课程数，E为依赖关系数
空间复杂度: O(V+E) - 邻接表和队列空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import deque
from leetcode_solutions.utils.solution import create_solution


def course_schedule(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    函数式接口 - 判断是否能完成所有课程
    
    实现思路:
    使用拓扑排序检测是否有环，如果有环则无法完成所有课程。
    
    Args:
        numCourses: 课程总数
        prerequisites: 先修课程关系列表
        
    Returns:
        如果能够完成所有课程返回True，否则返回False
        
    Example:
        >>> course_schedule(2, [[1, 0]])
        True
    """
    # 构建邻接表和入度数组
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    
    # 将所有入度为0的节点加入队列
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    
    while queue:
        node = queue.popleft()
        count += 1
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return count == numCourses


# 自动生成Solution类（无需手动编写）
Solution = create_solution(course_schedule)
