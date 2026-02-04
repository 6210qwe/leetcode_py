# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 863
标题: Sum of Distances in Tree
难度: hard
链接: https://leetcode.cn/problems/sum-of-distances-in-tree/
题目类型: 树、深度优先搜索、图、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
834. 树中距离之和 - 给定一个无向、连通的树。树中有 n 个标记为 0...n-1 的节点以及 n-1 条边 。 给定整数 n 和数组 edges ， edges[i] = [ai, bi]表示树中的节点 ai 和 bi 之间有一条边。 返回长度为 n 的数组 answer ，其中 answer[i] 是树中第 i 个节点与所有其他节点之间的距离之和。 示例 1: [https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg] 输入: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]] 输出: [8,12,6,10,10,10] 解释: 树如图所示。 我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5) 也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。 示例 2: [https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist2.jpg] 输入: n = 1, edges = [] 输出: [0] 示例 3: [https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist3.jpg] 输入: n = 2, edges = [[1,0]] 输出: [1,1] 提示: * 1 <= n <= 3 * 104 * edges.length == n - 1 * edges[i].length == 2 * 0 <= ai, bi < n * ai != bi * 给定的输入保证为有效的树
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两次深度优先搜索（DFS）来计算每个节点到其他所有节点的距离之和。

算法步骤:
1. 构建树的邻接表表示。
2. 第一次DFS：从根节点开始，计算每个子树的大小和根节点到该子树的距离之和。
3. 第二次DFS：利用第一次DFS的结果，通过换根DP的方法，计算每个节点到其他所有节点的距离之和。

关键点:
- 第一次DFS用于计算以某个节点为根的子树的大小和距离之和。
- 第二次DFS用于更新每个节点的距离之和，通过换根的方式。
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

def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]

    # 构建邻接表
    tree = [[] for _ in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # 第一次DFS，计算子树大小和根节点到子树的距离之和
    size = [1] * n
    dp = [0] * n

    def dfs(node: int, parent: int):
        for child in tree[node]:
            if child == parent:
                continue
            dfs(child, node)
            size[node] += size[child]
            dp[node] += dp[child] + size[child]

    # 第二次DFS，计算每个节点到其他所有节点的距离之和
    ans = [0] * n

    def dfs2(node: int, parent: int):
        ans[node] = dp[node]
        for child in tree[node]:
            if child == parent:
                continue
            prev_dp_node = dp[node]
            prev_dp_child = dp[child]

            dp[node] -= dp[child] + size[child]
            size[child] += size[node] - size[child]
            dp[child] += dp[node] + size[node] - size[child]

            dfs2(child, node)

            dp[node] = prev_dp_node
            dp[child] = prev_dp_child
            size[child] = n - size[node]

    dfs(0, -1)
    dfs2(0, -1)

    return ans

Solution = sumOfDistancesInTree