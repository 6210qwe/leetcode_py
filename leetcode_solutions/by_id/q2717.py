# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2717
标题: Collect Coins in a Tree
难度: hard
链接: https://leetcode.cn/problems/collect-coins-in-a-tree/
题目类型: 树、图、拓扑排序、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2603. 收集树中金币 - 给你一个 n 个节点的无向无根树，节点编号从 0 到 n - 1 。给你整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。再给你一个长度为 n 的数组 coins ，其中 coins[i] 可能为 0 也可能为 1 ，1 表示节点 i 处有一个金币。 一开始，你需要选择树中任意一个节点出发。你可以执行下述操作任意次： * 收集距离当前节点距离为 2 以内的所有金币，或者 * 移动到树中一个相邻节点。 你需要收集树中所有的金币，并且回到出发节点，请你返回最少经过的边数。 如果你多次经过一条边，每一次经过都会给答案加一。 示例 1： [https://assets.leetcode.com/uploads/2023/03/01/graph-2.png] 输入：coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]] 输出：2 解释：从节点 2 出发，收集节点 0 处的金币，移动到节点 3 ，收集节点 5 处的金币，然后移动回节点 2 。 示例 2： [https://assets.leetcode.com/uploads/2023/03/02/graph-4.png] 输入：coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]] 输出：2 解释：从节点 0 出发，收集节点 4 和 3 处的金币，移动到节点 2 处，收集节点 7 处的金币，移动回节点 0 。 提示： * n == coins.length * 1 <= n <= 3 * 104 * 0 <= coins[i] <= 1 * edges.length == n - 1 * edges[i].length == 2 * 0 <= ai, bi < n * ai != bi * edges 表示一棵合法的树。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两次深度优先搜索（DFS）来确定需要删除的叶子节点，从而减少不必要的边。

算法步骤:
1. 构建树的邻接表表示。
2. 从没有金币的叶子节点开始，进行一次DFS，删除这些叶子节点及其边。
3. 再进行一次DFS，删除剩余的叶子节点及其边。
4. 计算剩余的边数并返回结果。

关键点:
- 通过两次DFS删除不必要的叶子节点，确保只保留必要的边。
- 通过拓扑排序的思想，逐步删除叶子节点。
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

from typing import List

def collectTheCoins(coins: List[int], edges: List[List[int]]) -> int:
    n = len(coins)
    if n == 1:
        return 0

    # 构建邻接表
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # 删除没有金币的叶子节点
    def remove_leaf_nodes():
        leaves = []
        for node in range(n):
            if len(adj_list[node]) == 1 and coins[node] == 0:
                leaves.append(node)
        for leaf in leaves:
            neighbor = adj_list[leaf][0]
            adj_list[neighbor].remove(leaf)
            adj_list[leaf].clear()

    remove_leaf_nodes()

    # 删除剩余的叶子节点
    def remove_remaining_leaves():
        leaves = []
        for node in range(n):
            if len(adj_list[node]) == 1:
                leaves.append(node)
        for _ in range(2):
            new_leaves = []
            for leaf in leaves:
                if adj_list[leaf]:
                    neighbor = adj_list[leaf][0]
                    adj_list[neighbor].remove(leaf)
                    adj_list[leaf].clear()
                    if len(adj_list[neighbor]) == 1:
                        new_leaves.append(neighbor)
            leaves = new_leaves

    remove_remaining_leaves()

    # 计算剩余的边数
    remaining_edges = sum(len(adj_list[node]) for node in range(n)) // 2
    return remaining_edges

Solution = create_solution(collectTheCoins)