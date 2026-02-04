# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000220
标题: 电动车游城市
难度: hard
链接: https://leetcode.cn/problems/DFPeFJ/
题目类型: 图、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 35. 电动车游城市 - 小明的电动车电量充满时可行驶距离为 cnt，每行驶 1 单位距离消耗 1 单位电量，且花费 1 单位时间。小明想选择电动车作为代步工具。地图上共有 N 个景点，景点编号为 0 ~ N-1。他将地图信息以 [城市 A 编号,城市 B 编号,两城市间距离] 格式整理在在二维数组 paths，表示城市 A、B 间存在双向通路。初始状态，电动车电量为 0。每个城市都设有充电桩，charge[i] 表示第 i 个城市每充 1 单位电量需要花费的单位时间。请返回小明最少需要花费多少单位时间从起点城市 start 抵达终点城市 end。 示例 1： 输入：paths = [[1,3,3],[3,2,1],[2,1,3],[0,1,4],[3,0,5]], cnt = 6, start = 1, end = 0, charge = [2,10,4,1] 输出：43 解释：最佳路线为：1->3->0。 在城市 1 仅充 3 单位电至城市 3，然后在城市 3 充 5 单位电，行驶至城市 0。 充电用时共 3*10 + 5*1= 35 行驶用时 3 + 5 = 8，此时总用时最短 43。 image.png [https://pic.leetcode.cn/1616125304-mzVxIV-image.png] 示例 2： 输入：paths = [[0,4,2],[4,3,5],[3,0,5],[0,1,5],[3,2,4],[1,2,8]], cnt = 8, start = 0, end = 2, charge = [4,1,1,3,2] 输出：38 解释：最佳路线为：0->4->3->2。 城市 0 充电 2 单位，行驶至城市 4 充电 8 单位，行驶至城市 3 充电 1 单位，最终行驶至城市 2。 充电用时 4*2+2*8+3*1 = 27 行驶用时 2+5+4 = 11，总用时最短 38。 提示： * 1 <= paths.length <= 200 * paths[i].length == 3 * 2 <= charge.length == n <= 100 * 0 <= path[i][0],path[i][1],start,end < n * 1 <= cnt <= 100 * 1 <= path[i][2] <= cnt * 1 <= charge[i] <= 100 * 题目保证所有城市相互可以到达
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法结合优先队列来解决这个问题。我们需要考虑每个城市的充电时间和行驶时间，并且要维护一个二维的 dp 数组来记录每个城市在不同电量下的最小时间。

算法步骤:
1. 构建图的邻接表表示。
2. 初始化 dp 数组和优先队列。
3. 使用 Dijkstra 算法遍历图，更新 dp 数组中的最小时间。
4. 返回 dp[end][cnt] 作为结果。

关键点:
- 使用优先队列来优化 Dijkstra 算法。
- 维护一个二维 dp 数组来记录每个城市在不同电量下的最小时间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log E + V * cnt)，其中 E 是路径的数量，V 是城市的数量，cnt 是电动车的最大电量。
空间复杂度: O(V * cnt)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq

def electric_car_plan(paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:
    """
    函数式接口 - 计算从起点到终点的最小时间
    """
    n = len(charge)
    graph = [[] for _ in range(n)]
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # dp[i][j] 表示到达城市 i 且电量为 j 时的最小时间
    dp = [[float('inf')] * (cnt + 1) for _ in range(n)]
    dp[start][0] = 0

    # 优先队列，(时间, 当前城市, 当前电量)
    pq = [(0, start, 0)]
    while pq:
        time, city, power = heapq.heappop(pq)

        if time > dp[city][power]:
            continue

        if city == end:
            return time

        # 充电
        for new_power in range(power + 1, min(cnt, power + 1 + charge[city])):
            new_time = time + (new_power - power) * charge[city]
            if new_time < dp[city][new_power]:
                dp[city][new_power] = new_time
                heapq.heappush(pq, (new_time, city, new_power))

        # 行驶
        for next_city, distance in graph[city]:
            if power >= distance:
                new_time = time + distance
                new_power = power - distance
                if new_time < dp[next_city][new_power]:
                    dp[next_city][new_power] = new_time
                    heapq.heappush(pq, (new_time, next_city, new_power))

    return -1

Solution = create_solution(electric_car_plan)