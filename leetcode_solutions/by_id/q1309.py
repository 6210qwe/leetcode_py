# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1309
标题: Sort Items by Groups Respecting Dependencies
难度: hard
链接: https://leetcode.cn/problems/sort-items-by-groups-respecting-dependencies/
题目类型: 深度优先搜索、广度优先搜索、图、拓扑排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1203. 项目管理 - 有 n 个项目，每个项目或者不属于任何小组，或者属于 m 个小组之一。group[i] 表示第 i 个项目所属的小组，如果第 i 个项目不属于任何小组，则 group[i] 等于 -1。项目和小组都是从零开始编号的。可能存在小组不负责任何项目，即没有任何项目属于这个小组。 请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表： * 同一小组的项目，排序后在列表中彼此相邻。 * 项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个项目左侧）应该完成的所有项目。 如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 空列表 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/09/22/1359_ex1.png] 输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]] 输出：[6,3,4,1,5,2,0,7] 示例 2： 输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]] 输出：[] 解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。 提示： * 1 <= m <= n <= 3 * 104 * group.length == beforeItems.length == n * -1 <= group[i] <= m - 1 * 0 <= beforeItems[i].length <= n - 1 * 0 <= beforeItems[i][j] <= n - 1 * i != beforeItems[i][j] * beforeItems[i] 不含重复元素
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序对项目和组进行排序。

算法步骤:
1. 构建项目和组的图。
2. 对每个组内的项目进行拓扑排序。
3. 对所有组进行拓扑排序。
4. 将组内排序后的项目合并成最终结果。

关键点:
- 使用拓扑排序确保依赖关系得到满足。
- 分别对项目和组进行拓扑排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m + E)，其中 n 是项目数，m 是组数，E 是依赖关系的数量。
空间复杂度: O(n + m + E)，用于存储图和入度数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict, deque

def sort_items(n: int, m: int, group: List[int], before_items: List[List[int]]) -> List[int]:
    def topological_sort(graph, in_degree):
        queue = deque([node for node in graph if in_degree[node] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == len(graph) else []

    # 给没有组的项目分配新的组
    for i in range(n):
        if group[i] == -1:
            group[i] = m
            m += 1

    # 构建项目图和组图
    item_graph = defaultdict(list)
    item_in_degree = defaultdict(int)
    group_graph = defaultdict(list)
    group_in_degree = defaultdict(int)

    for i in range(n):
        for j in before_items[i]:
            item_graph[j].append(i)
            item_in_degree[i] += 1
            if group[i] != group[j]:
                group_graph[group[j]].append(group[i])
                group_in_degree[group[i]] += 1

    # 对每个组内的项目进行拓扑排序
    sorted_groups = topological_sort(group_graph, group_in_degree)
    if not sorted_groups:
        return []

    # 对所有组进行拓扑排序
    item_order = {}
    for g in sorted_groups:
        items_in_group = [i for i in range(n) if group[i] == g]
        sorted_items = topological_sort({i: item_graph[i] for i in items_in_group}, {i: item_in_degree[i] for i in items_in_group})
        if not sorted_items:
            return []
        item_order[g] = sorted_items

    # 合并组内排序后的项目
    result = []
    for g in sorted_groups:
        result.extend(item_order[g])

    return result

Solution = create_solution(sort_items)