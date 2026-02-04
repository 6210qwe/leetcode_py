# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 833
标题: Bus Routes
难度: hard
链接: https://leetcode.cn/problems/bus-routes/
题目类型: 广度优先搜索、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
815. 公交路线 - 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。 * 例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。 现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。 求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。 示例 1： 输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6 输出：2 解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。 示例 2： 输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12 输出：-1 提示： * 1 <= routes.length <= 500. * 1 <= routes[i].length <= 105 * routes[i] 中的所有值 互不相同 * sum(routes[i].length) <= 105 * 0 <= routes[i][j] < 106 * 0 <= source, target < 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来找到从起点到终点的最短路径。

算法步骤:
1. 构建一个图，其中节点是车站，边表示公交车线路。
2. 使用 BFS 从起点开始搜索，记录已经访问过的车站和公交车线路。
3. 如果在搜索过程中到达目标车站，则返回乘坐的公交车数量。
4. 如果搜索完毕仍未到达目标车站，则返回 -1。

关键点:
- 使用字典来存储每个车站可以到达的公交车线路。
- 使用队列来进行 BFS，并记录当前乘坐的公交车数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N + R)，其中 N 是所有车站的数量，R 是所有公交车线路的数量。
空间复杂度: O(N + R)，用于存储图结构和 BFS 的队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import defaultdict, deque

def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    if source == target:
        return 0

    # 构建图
    station_to_buses = defaultdict(set)
    for bus, stations in enumerate(routes):
        for station in stations:
            station_to_buses[station].add(bus)

    # 初始化 BFS
    queue = deque([(source, 0)])  # (当前车站, 乘坐的公交车数量)
    visited_stations = set([source])
    visited_buses = set()

    while queue:
        current_station, bus_count = queue.popleft()
        for bus in station_to_buses[current_station]:
            if bus in visited_buses:
                continue
            visited_buses.add(bus)
            for next_station in routes[bus]:
                if next_station in visited_stations:
                    continue
                if next_station == target:
                    return bus_count + 1
                visited_stations.add(next_station)
                queue.append((next_station, bus_count + 1))

    return -1

Solution = create_solution(numBusesToDestination)