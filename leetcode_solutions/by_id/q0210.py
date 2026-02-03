# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 210
标题: Course Schedule II
难度: medium
链接: https://leetcode.cn/problems/course-schedule-ii/
题目类型: 深度优先搜索、广度优先搜索、图、拓扑排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
210. 课程表 II - 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。 * 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。 返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。 示例 1： 输入：numCourses = 2, prerequisites = [[1,0]] 输出：[0,1] 解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。 示例 2： 输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] 输出：[0,2,1,3] 解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。 因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。 示例 3： 输入：numCourses = 1, prerequisites = [] 输出：[0] 提示： * 1 <= numCourses <= 2000 * 0 <= prerequisites.length <= numCourses * (numCourses - 1) * prerequisites[i].length == 2 * 0 <= ai, bi < numCourses * ai != bi * 所有[ai, bi] 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 拓扑排序，返回课程学习顺序

算法步骤:
1. 构建邻接表和入度数组
2. 使用队列进行拓扑排序
3. 将入度为0的节点加入队列
4. 每次出队一个节点，将其加入结果，并更新其邻接节点的入度
5. 如果所有节点都被访问，返回结果；否则返回空数组

关键点:
- 使用拓扑排序（Kahn算法）
- 时间复杂度O(V+E)，空间复杂度O(V+E)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(V+E) - V为课程数，E为先修关系数
空间复杂度: O(V+E) - 邻接表和队列空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import collections
from leetcode_solutions.utils.solution import create_solution


def course_schedule_ii(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    函数式接口 - 课程表II
    
    实现思路:
    拓扑排序，返回课程学习顺序。
    
    Args:
        numCourses: 课程总数
        prerequisites: 先修课程列表
        
    Returns:
        课程学习顺序，如果无法完成返回空数组
        
    Example:
        >>> course_schedule_ii(2, [[1, 0]])
        [0, 1]
    """
    adj = collections.defaultdict(list)
    indegree = [0] * numCourses
    
    for course, prereq in prerequisites:
        adj[prereq].append(course)
        indegree[course] += 1
    
    queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == numCourses else []


# 自动生成Solution类（无需手动编写）
Solution = create_solution(course_schedule_ii)
