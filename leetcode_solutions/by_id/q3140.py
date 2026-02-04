# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3140
标题: Count Visited Nodes in a Directed Graph
难度: hard
链接: https://leetcode.cn/problems/count-visited-nodes-in-a-directed-graph/
题目类型: 图、记忆化搜索、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2876. 有向图访问计数 - 现有一个有向图，其中包含 n 个节点，节点编号从 0 到 n - 1 。此外，该图还包含了 n 条有向边。 给你一个下标从 0 开始的数组 edges ，其中 edges[i] 表示存在一条从节点 i 到节点 edges[i] 的边。 想象在图上发生以下过程： * 你从节点 x 开始，通过边访问其他节点，直到你在 此过程 中再次访问到之前已经访问过的节点。 返回数组 answer 作为答案，其中 answer[i] 表示如果从节点 i 开始执行该过程，你可以访问到的不同节点数。 示例 1： [https://assets.leetcode.com/uploads/2023/08/31/graaphdrawio-1.png] 输入：edges = [1,2,0,0] 输出：[3,3,3,4] 解释：从每个节点开始执行该过程，记录如下： - 从节点 0 开始，访问节点 0 -> 1 -> 2 -> 0 。访问的不同节点数是 3 。 - 从节点 1 开始，访问节点 1 -> 2 -> 0 -> 1 。访问的不同节点数是 3 。 - 从节点 2 开始，访问节点 2 -> 0 -> 1 -> 2 。访问的不同节点数是 3 。 - 从节点 3 开始，访问节点 3 -> 0 -> 1 -> 2 -> 0 。访问的不同节点数是 4 。 示例 2： [https://assets.leetcode.com/uploads/2023/08/31/graaph2drawio.png] 输入：edges = [1,2,3,4,0] 输出：[5,5,5,5,5] 解释：无论从哪个节点开始，在这个过程中，都可以访问到图中的每一个节点。 提示： * n == edges.length * 2 <= n <= 105 * 0 <= edges[i] <= n - 1 * edges[i] != i
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 和记忆化来计算每个节点可以访问的不同节点数。

算法步骤:
1. 初始化结果数组 `answer` 和一个 `visited` 数组来记录访问状态。
2. 对于每个节点，使用 DFS 访问其所有可达节点，并记录访问路径。
3. 如果遇到已经访问过的节点，根据环的长度更新结果数组。
4. 使用记忆化来避免重复计算。

关键点:
- 使用 `visited` 数组来记录访问状态和环的长度。
- 使用 `memo` 字典来存储已经计算过的结果，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是节点数。每个节点最多访问一次。
空间复杂度: O(n)，用于存储 `visited` 数组和 `memo` 字典。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def count_visited_nodes(edges: List[int]) -> List[int]:
    n = len(edges)
    answer = [0] * n
    visited = [0] * n  # 0: 未访问, 1: 访问中, 2: 已访问
    memo = {}

    def dfs(node: int) -> int:
        if node in memo:
            return memo[node]
        
        if visited[node] == 1:
            # 找到环
            cycle_length = 0
            current = node
            while True:
                cycle_length += 1
                visited[current] = 2
                memo[current] = cycle_length
                current = edges[current]
                if current == node:
                    break
            return cycle_length
        
        if visited[node] == 2:
            return memo[node]
        
        visited[node] = 1
        next_node = edges[node]
        result = 1 + dfs(next_node)
        visited[node] = 2
        memo[node] = result
        return result

    for i in range(n):
        if visited[i] == 0:
            dfs(i)

    for i in range(n):
        if visited[i] == 2:
            answer[i] = memo[i]

    return answer

Solution = create_solution(count_visited_nodes)