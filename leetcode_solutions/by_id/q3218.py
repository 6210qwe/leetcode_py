# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3218
标题: Find Number of Coins to Place in Tree Nodes
难度: hard
链接: https://leetcode.cn/problems/find-number-of-coins-to-place-in-tree-nodes/
题目类型: 树、深度优先搜索、动态规划、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2973. 树中每个节点放置的金币数目 - 给你一棵 n 个节点的 无向 树，节点编号为 0 到 n - 1 ，树的根节点在节点 0 处。同时给你一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。 给你一个长度为 n 下标从 0 开始的整数数组 cost ，其中 cost[i] 是第 i 个节点的 开销 。 你需要在树中每个节点都放置金币，在节点 i 处的金币数目计算方法如下： * 如果节点 i 对应的子树中的节点数目小于 3 ，那么放 1 个金币。 * 否则，计算节点 i 对应的子树内 3 个不同节点的开销乘积的 最大值 ，并在节点 i 处放置对应数目的金币。如果最大乘积是 负数 ，那么放置 0 个金币。 请你返回一个长度为 n 的数组 coin ，coin[i]是节点 i 处的金币数目。 示例 1： [https://assets.leetcode.com/uploads/2023/11/09/screenshot-2023-11-10-012641.png] 输入：edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6] 输出：[120,1,1,1,1,1] 解释：在节点 0 处放置 6 * 5 * 4 = 120 个金币。所有其他节点都是叶子节点，子树中只有 1 个节点，所以其他每个节点都放 1 个金币。 示例 2： [https://assets.leetcode.com/uploads/2023/11/09/screenshot-2023-11-10-012614.png] 输入：edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2] 输出：[280,140,32,1,1,1,1,1,1] 解释：每个节点放置的金币数分别为： - 节点 0 处放置 8 * 7 * 5 = 280 个金币。 - 节点 1 处放置 7 * 5 * 4 = 140 个金币。 - 节点 2 处放置 8 * 2 * 2 = 32 个金币。 - 其他节点都是叶子节点，子树内节点数目为 1 ，所以其他每个节点都放 1 个金币。 示例 3： [https://assets.leetcode.com/uploads/2023/11/09/screenshot-2023-11-10-012513.png] 输入：edges = [[0,1],[0,2]], cost = [1,2,-2] 输出：[0,1,1] 解释：节点 1 和 2 都是叶子节点，子树内节点数目为 1 ，各放置 1 个金币。节点 0 处唯一的开销乘积是 2 * 1 * -2 = -4 。所以在节点 0 处放置 0 个金币。 提示： * 2 <= n <= 2 * 104 * edges.length == n - 1 * edges[i].length == 2 * 0 <= ai, bi < n * cost.length == n * 1 <= |cost[i]| <= 104 * edges 一定是一棵合法的树。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用深度优先搜索 (DFS) 来遍历树，并在每个节点处计算其子树的节点数和开销。
- 对于每个节点，如果子树节点数小于 3，则放置 1 个金币；否则，选择子树中最大的 3 个开销来计算金币数。

算法步骤:
1. 构建树的邻接表表示。
2. 定义一个 DFS 函数，该函数返回子树的节点数和开销列表。
3. 在 DFS 函数中，递归地计算每个子树的节点数和开销，并合并结果。
4. 计算每个节点的金币数，并返回结果。

关键点:
- 使用堆（优先队列）来维护子树中最大的 3 个开销。
- 通过递归 DFS 来高效地遍历树并计算每个节点的金币数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是节点数。每个节点的处理时间是 O(log n)，因为需要维护一个大小为 3 的堆。
空间复杂度: O(n)，存储树的邻接表和递归栈的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

def find_number_of_coins_to_place_in_tree_nodes(edges: List[List[int]], cost: List[int]) -> List[int]:
    n = len(cost)
    tree = [[] for _ in range(n)]
    
    # 构建树的邻接表表示
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    def dfs(node: int, parent: int) -> (int, List[int]):
        total_nodes = 1
        node_costs = [cost[node]]
        
        for child in tree[node]:
            if child != parent:
                child_nodes, child_costs = dfs(child, node)
                total_nodes += child_nodes
                node_costs.extend(child_costs)
        
        # 维护一个大小为 3 的堆
        largest_three = heapq.nlargest(3, node_costs)
        
        return total_nodes, largest_three
    
    coins = [0] * n
    
    def calculate_coins(node: int, parent: int):
        total_nodes, largest_three = dfs(node, parent)
        
        if total_nodes < 3:
            coins[node] = 1
        else:
            product = 1
            for c in largest_three:
                product *= c
            coins[node] = max(0, product)
    
    calculate_coins(0, -1)
    return coins

Solution = create_solution(find_number_of_coins_to_place_in_tree_nodes)