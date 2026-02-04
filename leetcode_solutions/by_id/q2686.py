# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2686
标题: Minimum Cost of a Path With Special Roads
难度: medium
链接: https://leetcode.cn/problems/minimum-cost-of-a-path-with-special-roads/
题目类型: 图、数组、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2662. 前往目标的最小代价 - 给你一个数组 start ，其中 start = [startX, startY] 表示你的初始位置位于二维空间上的 (startX, startY) 。另给你一个数组 target ，其中 target = [targetX, targetY] 表示你的目标位置 (targetX, targetY) 。 从位置 (x1, y1) 到空间中任一其他位置 (x2, y2) 的 代价 是 |x2 - x1| + |y2 - y1| 。 给你一个二维数组 specialRoads ，表示空间中存在的一些 特殊路径。其中 specialRoads[i] = [x1i, y1i, x2i, y2i, costi] 表示第 i 条特殊路径可以从 (x1i, y1i) 到 (x2i, y2i) ，但成本等于 costi 。你可以使用每条特殊路径任意次数。 返回从 (startX, startY) 到 (targetX, targetY) 所需的 最小 代价。 示例 1： 输入：start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]] 输出：5 解释： 1. (1,1) 到 (1,2) 花费为 |1 - 1| + |2 - 1| = 1。 2. (1,2) 到 (3,3)。使用 specialRoads[0] 花费为 2。 3. (3,3) 到 (3,4) 花费为 |3 - 3| + |4 - 3| = 1。 4. (3,4) 到 (4,5)。使用 specialRoads[1] 花费为 1。 所以总花费是 1 + 2 + 1 + 1 = 5。 示例 2： 输入：start = [3,2], target = [5,7], specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]] 输出：7 解释： 不使用任何特殊路径，直接从开始到结束位置是最优的，花费为 |5 - 3| + |7 - 2| = 7。 注意 specialRoads[0] 直接从 (5,7) 到 (3,2)。 示例 3： 输入：start = [1,1], target = [10,4], specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]] 输出：8 解释： 1. (1,1) 到 (1,2) 花费为 |1 - 1| + |2 - 1| = 1。 2. (1,2) 到 (7,4)。使用 specialRoads[1] 花费为 4。 3. (7,4) 到 (10,4) 花费为 |10 - 7| + |4 - 4| = 3。 提示： * start.length == target.length == 2 * 1 <= startX <= targetX <= 105 * 1 <= startY <= targetY <= 105 * 1 <= specialRoads.length <= 200 * specialRoads[i].length == 5 * startX <= x1i, x2i <= targetX * startY <= y1i, y2i <= targetY * 1 <= costi <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法来找到从起点到终点的最短路径。

算法步骤:
1. 初始化一个优先队列，将起点加入队列，距离为 0。
2. 初始化一个字典来记录每个点的最小距离。
3. 从优先队列中取出当前距离最小的点，更新其相邻点的距离。
4. 如果当前点是终点，返回其距离。
5. 如果当前点不是终点，继续处理优先队列中的下一个点。

关键点:
- 使用优先队列来保证每次处理的都是当前距离最小的点。
- 更新相邻点的距离时，考虑普通路径和特殊路径两种情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log V)，其中 E 是边的数量，V 是顶点的数量。
空间复杂度: O(V + E)，存储图和优先队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Tuple
import heapq

def min_cost_path(start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
    # 定义曼哈顿距离函数
    def manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    # 初始化优先队列和距离字典
    pq = [(0, tuple(start))]
    distances = {tuple(start): 0}
    
    while pq:
        current_distance, current_point = heapq.heappop(pq)
        
        if current_point == tuple(target):
            return current_distance
        
        for x1, y1, x2, y2, cost in specialRoads:
            start_point = (x1, y1)
            end_point = (x2, y2)
            
            # 计算通过特殊路径到达终点的距离
            special_road_distance = current_distance + manhattan_distance(current_point, start_point) + cost
            
            # 如果通过特殊路径到达终点的距离更小，更新距离并加入优先队列
            if special_road_distance < distances.get(end_point, float('inf')):
                distances[end_point] = special_road_distance
                heapq.heappush(pq, (special_road_distance, end_point))
        
        # 计算直接到达终点的距离
        direct_distance = current_distance + manhattan_distance(current_point, tuple(target))
        
        # 如果直接到达终点的距离更小，更新距离并加入优先队列
        if direct_distance < distances.get(tuple(target), float('inf')):
            distances[tuple(target)] = direct_distance
            heapq.heappush(pq, (direct_distance, tuple(target)))

    return distances[tuple(target)]

Solution = create_solution(min_cost_path)