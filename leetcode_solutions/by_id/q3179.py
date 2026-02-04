# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3179
标题: Maximum Points After Collecting Coins From All Nodes
难度: hard
链接: https://leetcode.cn/problems/maximum-points-after-collecting-coins-from-all-nodes/
题目类型: 位运算、树、深度优先搜索、记忆化搜索、数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2920. 收集所有金币可获得的最大积分 - 有一棵由 n 个节点组成的无向树，以 0 为根节点，节点编号从 0 到 n - 1 。给你一个长度为 n - 1 的二维 整数 数组 edges ，其中 edges[i] = [ai, bi] 表示在树上的节点 ai 和 bi 之间存在一条边。另给你一个下标从 0 开始、长度为 n 的数组 coins 和一个整数 k ，其中 coins[i] 表示节点 i 处的金币数量。 从根节点开始，你必须收集所有金币。要想收集节点上的金币，必须先收集该节点的祖先节点上的金币。 节点 i 上的金币可以用下述方法之一进行收集： * 收集所有金币，得到共计 coins[i] - k 点积分。如果 coins[i] - k 是负数，你将会失去 abs(coins[i] - k) 点积分。 * 收集所有金币，得到共计 floor(coins[i] / 2) 点积分。如果采用这种方法，节点 i 子树中所有节点 j 的金币数 coins[j] 将会减少至 floor(coins[j] / 2) 。 返回收集 所有 树节点的金币之后可以获得的最大积分。 示例 1： [https://assets.leetcode.com/uploads/2023/09/18/ex1-copy.png] 输入：edges = [[0,1],[1,2],[2,3]], coins = [10,10,3,3], k = 5 输出：11 解释： 使用第一种方法收集节点 0 上的所有金币。总积分 = 10 - 5 = 5 。 使用第一种方法收集节点 1 上的所有金币。总积分 = 5 + (10 - 5) = 10 。 使用第二种方法收集节点 2 上的所有金币。所以节点 3 上的金币将会变为 floor(3 / 2) = 1 ，总积分 = 10 + floor(3 / 2) = 11 。 使用第二种方法收集节点 3 上的所有金币。总积分 = 11 + floor(1 / 2) = 11. 可以证明收集所有节点上的金币能获得的最大积分是 11 。 示例 2： [https://assets.leetcode.com/uploads/2023/09/18/ex2.png] 输入：edges = [[0,1],[0,2]], coins = [8,4,4], k = 0 输出：16 解释： 使用第一种方法收集所有节点上的金币，因此，总积分 = (8 - 0) + (4 - 0) + (4 - 0) = 16 。 提示： * n == coins.length * 2 <= n <= 105 * 0 <= coins[i] <= 104 * edges.length == n - 1 * 0 <= edges[i][0], edges[i][1] < n * 0 <= k <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）和记忆化搜索来解决这个问题。我们可以通过递归地处理每个节点及其子树，并使用记忆化来避免重复计算。

算法步骤:
1. 构建树的邻接表表示。
2. 定义一个递归函数 `dfs`，该函数接受当前节点、父节点、金币数组和剩余的减半操作次数作为参数。
3. 在 `dfs` 函数中，计算两种收集金币的方法的得分，并选择最大值。
4. 使用记忆化来存储已经计算过的状态，以避免重复计算。
5. 从根节点开始调用 `dfs` 函数，返回最终的最大积分。

关键点:
- 使用记忆化搜索来优化时间复杂度。
- 通过递归处理每个节点及其子树。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log(max(coins)))，其中 n 是节点数，log(max(coins)) 是金币减半操作的最大次数。
空间复杂度: O(n * log(max(coins)))，用于存储记忆化搜索的结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from functools import lru_cache

def maxPoints(edges: List[List[int]], coins: List[int], k: int) -> int:
    # 构建树的邻接表表示
    tree = [[] for _ in range(len(coins))]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    @lru_cache(None)
    def dfs(node: int, parent: int, remaining_halves: int) -> int:
        # 计算当前节点的金币数
        current_coins = coins[node] >> remaining_halves
        if current_coins == 0:
            return 0

        # 选择第一种方法收集金币
        points1 = current_coins - k
        for child in tree[node]:
            if child != parent:
                points1 += dfs(child, node, remaining_halves)

        # 选择第二种方法收集金币
        points2 = current_coins // 2
        if remaining_halves < 14:  # 最多可以减半 14 次
            for child in tree[node]:
                if child != parent:
                    points2 += dfs(child, node, remaining_halves + 1)

        # 返回两种方法中的最大值
        return max(points1, points2)

    # 从根节点开始调用 dfs 函数
    return dfs(0, -1, 0)

Solution = create_solution(maxPoints)