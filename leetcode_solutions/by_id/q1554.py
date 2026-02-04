# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1554
标题: Minimum Time to Collect All Apples in a Tree
难度: medium
链接: https://leetcode.cn/problems/minimum-time-to-collect-all-apples-in-a-tree/
题目类型: 树、深度优先搜索、广度优先搜索、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1443. 收集树上所有苹果的最少时间 - 给你一棵有 n 个节点的无向树，节点编号为 0 到 n-1 ，它们中有一些节点有苹果。通过树上的一条边，需要花费 1 秒钟。你从 节点 0 出发，请你返回最少需要多少秒，可以收集到所有苹果，并回到节点 0 。 无向树的边由 edges 给出，其中 edges[i] = [fromi, toi] ，表示有一条边连接 from 和 toi 。除此以外，还有一个布尔数组 hasApple ，其中 hasApple[i] = true 代表节点 i 有一个苹果，否则，节点 i 没有苹果。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/10/min_time_collect_apple_1.png] 输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false] 输出：8 解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/10/min_time_collect_apple_2.png] 输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false] 输出：6 解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。 示例 3： 输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false] 输出：0 提示： * 1 <= n <= 10^5 * edges.length == n - 1 * edges[i].length == 2 * 0 <= ai < bi <= n - 1 * hasApple.length == n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历树，计算从根节点到每个有苹果的节点的路径长度。

算法步骤:
1. 构建树的邻接表表示。
2. 从根节点 (0) 开始进行 DFS 遍历。
3. 对于每个节点，如果它或其子节点有苹果，则计算从该节点到根节点的路径长度。
4. 返回总路径长度。

关键点:
- 使用邻接表来表示树结构。
- 通过 DFS 递归地遍历树，并计算路径长度。
- 只有当节点或其子节点有苹果时，才计入路径长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是节点数。每个节点和边都只访问一次。
空间复杂度: O(n)，用于存储邻接表和递归调用栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional

def minTime(n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    # 构建邻接表
    tree = [[] for _ in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    def dfs(node: int, parent: int) -> int:
        total_time = 0
        for child in tree[node]:
            if child != parent:
                child_time = dfs(child, node)
                if child_time > 0 or hasApple[child]:
                    total_time += child_time + 2
        return total_time

    return dfs(0, -1)

Solution = create_solution(minTime)