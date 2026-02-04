# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3863
标题: Power Grid Maintenance
难度: medium
链接: https://leetcode.cn/problems/power-grid-maintenance/
题目类型: 深度优先搜索、广度优先搜索、并查集、图、数组、哈希表、有序集合、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3607. 电网维护 - 给你一个整数 c，表示 c 个电站，每个电站有一个唯一标识符 id，从 1 到 c 编号。 这些电站通过 n 条 双向 电缆互相连接，表示为一个二维数组 connections，其中每个元素 connections[i] = [ui, vi] 表示电站 ui 和电站 vi 之间的连接。直接或间接连接的电站组成了一个 电网 。 最初，所有 电站均处于在线（正常运行）状态。 另给你一个二维数组 queries，其中每个查询属于以下 两种类型之一 ： * [1, x]：请求对电站 x 进行维护检查。如果电站 x 在线，则它自行解决检查。如果电站 x 已离线，则检查由与 x 同一 电网 中 编号最小 的在线电站解决。如果该电网中 不存在 任何 在线 电站，则返回 -1。 * [2, x]：电站 x 离线（即变为非运行状态）。 返回一个整数数组，表示按照查询中出现的顺序，所有类型为 [1, x] 的查询结果。 注意：电网的结构是固定的；离线（非运行）的节点仍然属于其所在的电网，且离线操作不会改变电网的连接性。 示例 1： 输入： c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]] 输出： [3,2,3] 解释： [https://assets.leetcode.com/uploads/2025/04/15/powergrid.jpg] * 最初，所有电站 {1, 2, 3, 4, 5} 都在线，并组成一个电网。 * 查询 [1,3]：电站 3 在线，因此维护检查由电站 3 自行解决。 * 查询 [2,1]：电站 1 离线。剩余在线电站为 {2, 3, 4, 5}。 * 查询 [1,1]：电站 1 离线，因此检查由电网中编号最小的在线电站解决，即电站 2。 * 查询 [2,2]：电站 2 离线。剩余在线电站为 {3, 4, 5}。 * 查询 [1,2]：电站 2 离线，因此检查由电网中编号最小的在线电站解决，即电站 3。 示例 2： 输入： c = 3, connections = [], queries = [[1,1],[2,1],[1,1]] 输出： [1,-1] 解释： * 没有连接，因此每个电站是一个独立的电网。 * 查询 [1,1]：电站 1 在线，且属于其独立电网，因此维护检查由电站 1 自行解决。 * 查询 [2,1]：电站 1 离线。 * 查询 [1,1]：电站 1 离线，且其电网中没有其他电站，因此结果为 -1。 提示： * 1 <= c <= 105 * 0 <= n == connections.length <= min(105, c * (c - 1) / 2) * connections[i].length == 2 * 1 <= ui, vi <= c * ui != vi * 1 <= queries.length <= 2 * 105 * queries[i].length == 2 * queries[i][0] 为 1 或 2。 * 1 <= queries[i][1] <= c
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来管理电网的连通性，并使用有序集合来快速找到电网中编号最小的在线电站。

算法步骤:
1. 构建并查集，将所有电站初始化为在线状态。
2. 对于每个查询：
   - 如果是 [1, x] 类型的查询，检查电站 x 是否在线。如果在线，则返回 x；否则，查找该电网中编号最小的在线电站。
   - 如果是 [2, x] 类型的查询，将电站 x 标记为离线。

关键点:
- 使用并查集来高效管理电网的连通性。
- 使用有序集合来快速找到电网中编号最小的在线电站。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((n + q) * α(c))，其中 n 是 connections 的长度，q 是 queries 的长度，α 是反阿克曼函数。
空间复杂度: O(c)，其中 c 是电站的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import collections
import sortedcontainers

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def power_grid_maintenance(c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
    # 构建并查集
    uf = UnionFind(c + 1)
    for u, v in connections:
        uf.union(u, v)
    
    # 初始化在线电站
    online_stations = sortedcontainers.SortedSet(range(1, c + 1))
    
    result = []
    for query in queries:
        if query[0] == 1:
            station = query[1]
            if station in online_stations:
                result.append(station)
            else:
                root = uf.find(station)
                smallest_online = online_stations.bisect_left(root)
                if smallest_online < len(online_stations) and uf.find(online_stations[smallest_online]) == root:
                    result.append(online_stations[smallest_online])
                else:
                    result.append(-1)
        elif query[0] == 2:
            station = query[1]
            online_stations.discard(station)
    
    return result

Solution = create_solution(power_grid_maintenance)