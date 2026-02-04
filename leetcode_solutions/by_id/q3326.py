# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3326
标题: Count Pairs of Connectable Servers in a Weighted Tree Network
难度: medium
链接: https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/
题目类型: 树、深度优先搜索、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3067. 在带权树网络中统计可连接服务器对数目 - 给你一棵无根带权树，树中总共有 n 个节点，分别表示 n 个服务器，服务器从 0 到 n - 1 编号。同时给你一个数组 edges ，其中 edges[i] = [ai, bi, weighti] 表示节点 ai 和 bi 之间有一条双向边，边的权值为 weighti 。再给你一个整数 signalSpeed 。 如果两台服务器 a 和 b 是通过服务器 c 可连接的，则： * a < b ，a != c 且 b != c 。 * 从 c 到 a 的距离是可以被 signalSpeed 整除的。 * 从 c 到 b 的距离是可以被 signalSpeed 整除的。 * 从 c 到 b 的路径与从 c 到 a 的路径没有任何公共边。 请你返回一个长度为 n 的整数数组 count ，其中 count[i] 表示通过服务器 i 可连接 的服务器对的 数目 。 示例 1： [https://assets.leetcode.com/uploads/2024/01/21/example22.png] 输入：edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1 输出：[0,4,6,6,4,0] 解释：由于 signalSpeed 等于 1 ，count[c] 等于所有从 c 开始且没有公共边的路径对数目。 在输入图中，count[c] 等于服务器 c 左边服务器数目乘以右边服务器数目。 示例 2： [https://assets.leetcode.com/uploads/2024/01/21/example11.png] 输入：edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]], signalSpeed = 3 输出：[2,0,0,0,0,0,2] 解释：通过服务器 0 ，有 2 个可连接服务器对(4, 5) 和 (4, 6) 。 通过服务器 6 ，有 2 个可连接服务器对 (4, 5) 和 (0, 5) 。 所有服务器对都必须通过服务器 0 或 6 才可连接，所以其他服务器对应的可连接服务器对数目都为 0 。 提示： * 2 <= n <= 1000 * edges.length == n - 1 * edges[i].length == 3 * 0 <= ai, bi < n * edges[i] = [ai, bi, weighti] * 1 <= weighti <= 106 * 1 <= signalSpeed <= 106 * 输入保证 edges 构成一棵合法的树。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来计算每个节点到其子节点的距离，并统计满足条件的服务器对。

算法步骤:
1. 构建图的邻接表表示。
2. 定义一个递归函数 dfs(node, parent, distance) 来计算从当前节点到其子节点的距离，并统计满足条件的服务器对。
3. 对于每个节点，调用 dfs 函数，并更新结果数组。

关键点:
- 使用 DFS 来遍历树，并记录每个节点到其子节点的距离。
- 通过信号速度来判断是否满足条件。
- 通过计数器来统计满足条件的服务器对。
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

def count_pairs_of_connectable_servers(edges: List[List[int]], signalSpeed: int) -> List[int]:
    n = len(edges) + 1
    graph = [[] for _ in range(n)]
    
    # 构建图的邻接表表示
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    def dfs(node: int, parent: int, distance: int) -> int:
        count = 0
        valid_count = 0
        
        for neighbor, weight in graph[node]:
            if neighbor == parent:
                continue
            new_distance = distance + weight
            if new_distance % signalSpeed == 0:
                valid_count += 1
            count += dfs(neighbor, node, new_distance)
        
        result[node] += valid_count * (valid_count - 1) // 2
        return valid_count
    
    result = [0] * n
    for i in range(n):
        dfs(i, -1, 0)
    
    return result

Solution = create_solution(count_pairs_of_connectable_servers)