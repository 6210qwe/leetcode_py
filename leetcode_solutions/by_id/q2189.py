# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2189
标题: Maximum Path Quality of a Graph
难度: hard
链接: https://leetcode.cn/problems/maximum-path-quality-of-a-graph/
题目类型: 图、数组、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2065. 最大化一张图中的路径价值 - 给你一张 无向 图，图中有 n 个节点，节点编号从 0 到 n - 1 （都包括）。同时给你一个下标从 0 开始的整数数组 values ，其中 values[i] 是第 i 个节点的 价值 。同时给你一个下标从 0 开始的二维整数数组 edges ，其中 edges[j] = [uj, vj, timej] 表示节点 uj 和 vj 之间有一条需要 timej 秒才能通过的无向边。最后，给你一个整数 maxTime 。 合法路径 指的是图中任意一条从节点 0 开始，最终回到节点 0 ，且花费的总时间 不超过 maxTime 秒的一条路径。你可以访问一个节点任意次。一条合法路径的 价值 定义为路径中 不同节点 的价值 之和 （每个节点的价值 至多 算入价值总和中一次）。 请你返回一条合法路径的 最大 价值。 注意：每个节点 至多 有 四条 边与之相连。 示例 1： [https://assets.leetcode.com/uploads/2021/10/19/ex1drawio.png] 输入：values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49 输出：75 解释： 一条可能的路径为：0 -> 1 -> 0 -> 3 -> 0 。总花费时间为 10 + 10 + 10 + 10 = 40 <= 49 。 访问过的节点为 0 ，1 和 3 ，最大路径价值为 0 + 32 + 43 = 75 。 示例 2： [https://assets.leetcode.com/uploads/2021/10/19/ex2drawio.png] 输入：values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30 输出：25 解释： 一条可能的路径为：0 -> 3 -> 0 。总花费时间为 10 + 10 = 20 <= 30 。 访问过的节点为 0 和 3 ，最大路径价值为 5 + 20 = 25 。 示例 3： [https://assets.leetcode.com/uploads/2021/10/19/ex31drawio.png] 输入：values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50 输出：7 解释： 一条可能的路径为：0 -> 1 -> 3 -> 1 -> 0 。总花费时间为 10 + 13 + 13 + 10 = 46 <= 50 。 访问过的节点为 0 ，1 和 3 ，最大路径价值为 1 + 2 + 4 = 7 。 示例 4： [https://assets.leetcode.com/uploads/2021/10/21/ex4drawio.png] 输入：values = [0,1,2], edges = [[1,2,10]], maxTime = 10 输出：0 解释： 唯一一条路径为 0 。总花费时间为 0 。 唯一访问过的节点为 0 ，最大路径价值为 0 。 提示： * n == values.length * 1 <= n <= 1000 * 0 <= values[i] <= 108 * 0 <= edges.length <= 2000 * edges[j].length == 3 * 0 <= uj < vj <= n - 1 * 10 <= timej, maxTime <= 100 * [uj, vj] 所有节点对 互不相同 。 * 每个节点 至多有四条 边。 * 图可能不连通。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来遍历所有可能的路径，并记录路径的最大价值。

算法步骤:
1. 构建图的邻接表表示。
2. 使用DFS从节点0开始遍历，记录当前路径的时间和价值。
3. 在DFS过程中，如果回到节点0且时间不超过maxTime，更新最大路径价值。
4. 使用一个集合来记录已经访问过的节点，避免重复计算节点的价值。

关键点:
- 使用DFS遍历所有可能的路径。
- 使用集合记录已经访问过的节点，确保每个节点的价值只计算一次。
- 递归过程中，更新最大路径价值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n)，其中n是节点数。最坏情况下，每个节点都可以选择访问或不访问。
空间复杂度: O(n)，递归调用栈的深度最多为n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(values: List[int], edges: List[List[int]], maxTime: int) -> int:
    """
    函数式接口 - 实现最大化一张图中的路径价值
    """
    n = len(values)
    graph = [[] for _ in range(n)]
    
    # 构建图的邻接表
    for u, v, time in edges:
        graph[u].append((v, time))
        graph[v].append((u, time))
    
    max_value = 0
    
    def dfs(node: int, visited: set, current_time: int, current_value: int):
        nonlocal max_value
        
        if node == 0 and current_time <= maxTime:
            max_value = max(max_value, current_value)
        
        for neighbor, time in graph[node]:
            if current_time + time <= maxTime:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, visited, current_time + time, current_value + values[neighbor])
                    visited.remove(neighbor)
                else:
                    dfs(neighbor, visited, current_time + time, current_value)
    
    # 从节点0开始DFS
    dfs(0, {0}, 0, values[0])
    
    return max_value

Solution = create_solution(solution_function_name)