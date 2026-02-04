# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2246
标题: Maximum Employees to Be Invited to a Meeting
难度: hard
链接: https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/
题目类型: 深度优先搜索、图、拓扑排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2127. 参加会议的最多员工数 - 一个公司准备组织一场会议，邀请名单上有 n 位员工。公司准备了一张 圆形 的桌子，可以坐下 任意数目 的员工。 员工编号为 0 到 n - 1 。每位员工都有一位 喜欢 的员工，每位员工 当且仅当 他被安排在喜欢员工的旁边，他才会参加会议。每位员工喜欢的员工 不会 是他自己。 给你一个下标从 0 开始的整数数组 favorite ，其中 favorite[i] 表示第 i 位员工喜欢的员工。请你返回参加会议的 最多员工数目 。 示例 1： [https://assets.leetcode.com/uploads/2021/12/14/ex1.png] 输入：favorite = [2,2,1,2] 输出：3 解释： 上图展示了公司邀请员工 0，1 和 2 参加会议以及他们在圆桌上的座位。 没办法邀请所有员工参与会议，因为员工 2 没办法同时坐在 0，1 和 3 员工的旁边。 注意，公司也可以邀请员工 1，2 和 3 参加会议。 所以最多参加会议的员工数目为 3 。 示例 2： 输入：favorite = [1,2,0] 输出：3 解释： 每个员工都至少是另一个员工喜欢的员工。所以公司邀请他们所有人参加会议的前提是所有人都参加了会议。 座位安排同图 1 所示： - 员工 0 坐在员工 2 和 1 之间。 - 员工 1 坐在员工 0 和 2 之间。 - 员工 2 坐在员工 1 和 0 之间。 参与会议的最多员工数目为 3 。 示例 3： [https://assets.leetcode.com/uploads/2021/12/14/ex2.png] 输入：favorite = [3,0,1,4,1] 输出：4 解释： 上图展示了公司可以邀请员工 0，1，3 和 4 参加会议以及他们在圆桌上的座位。 员工 2 无法参加，因为他喜欢的员工 1 旁边的座位已经被占领了。 所以公司只能不邀请员工 2 。 参加会议的最多员工数目为 4 。 提示： * n == favorite.length * 2 <= n <= 105 * 0 <= favorite[i] <= n - 1 * favorite[i] != i
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 通过构建有向图来表示员工之间的喜欢关系。
- 使用深度优先搜索 (DFS) 来找到所有的环和链。
- 计算每个环的长度，并计算每个节点的最长链长度。
- 最终结果是最大的环长度或两个链的长度之和。

算法步骤:
1. 构建有向图和反向图。
2. 使用 DFS 找到所有的环和链。
3. 计算每个环的长度。
4. 计算每个节点的最长链长度。
5. 返回最大值。

关键点:
- 使用 DFS 来遍历图并记录路径。
- 通过反向图来计算最长链。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_employees_to_meeting(favorite: List[int]) -> int:
    n = len(favorite)
    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]
    
    # 构建有向图和反向图
    for i, f in enumerate(favorite):
        graph[i].append(f)
        reverse_graph[f].append(i)
    
    def dfs(node, visited, path):
        if node in visited:
            return
        visited.add(node)
        path.append(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited, path)
    
    def find_longest_chain(node, memo):
        if node in memo:
            return memo[node]
        if not reverse_graph[node]:
            return 0
        max_chain = 0
        for neighbor in reverse_graph[node]:
            max_chain = max(max_chain, 1 + find_longest_chain(neighbor, memo))
        memo[node] = max_chain
        return max_chain
    
    max_cycle_length = 0
    max_chain_sum = 0
    visited = set()
    
    for i in range(n):
        if i not in visited:
            path = []
            dfs(i, visited, path)
            if len(path) > 1 and path[0] in graph[path[-1]]:
                cycle_length = len(path)
                max_cycle_length = max(max_cycle_length, cycle_length)
            else:
                for node in path:
                    longest_chain = find_longest_chain(node, {})
                    max_chain_sum = max(max_chain_sum, longest_chain)
    
    return max(max_cycle_length, max_chain_sum)


Solution = create_solution(max_employees_to_meeting)