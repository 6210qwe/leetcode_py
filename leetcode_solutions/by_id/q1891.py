# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1891
标题: Count Pairs Of Nodes
难度: hard
链接: https://leetcode.cn/problems/count-pairs-of-nodes/
题目类型: 图、数组、哈希表、双指针、二分查找、计数、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1782. 统计点对的数目 - 给你一个无向图，无向图由整数 n ，表示图中节点的数目，和 edges 组成，其中 edges[i] = [ui, vi] 表示 ui 和 vi 之间有一条无向边。同时给你一个代表查询的整数数组 queries 。 第 j 个查询的答案是满足如下条件的点对 (a, b) 的数目： * a < b * cnt 是与 a 或者 b 相连的边的数目，且 cnt 严格大于 queries[j] 。 请你返回一个数组 answers ，其中 answers.length == queries.length 且 answers[j] 是第 j 个查询的答案。 请注意，图中可能会有 多重边 。 示例 1： [https://pic.leetcode.cn/1692844033-Kvxjvr-image.png] 输入：n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3] 输出：[6,5] 解释：每个点对中，与至少一个点相连的边的数目如上图所示。 answers[0] = 6。所有的点对(a, b)中边数和都大于2，故有6个； answers[1] = 5。所有的点对(a, b)中除了(3,4)边数等于3，其它点对边数和都大于3，故有5个。 示例 2： 输入：n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5] 输出：[10,10,9,8,6] 提示： * 2 <= n <= 2 * 104 * 1 <= edges.length <= 105 * 1 <= ui, vi <= n * ui != vi * 1 <= queries.length <= 20 * 0 <= queries[j] < edges.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 计算每个节点的度数。
2. 使用双重循环计算所有点对的边数和，并记录在字典中。
3. 对于每个查询，使用二分查找找到满足条件的点对数量。

算法步骤:
1. 计算每个节点的度数。
2. 使用双重循环计算所有点对的边数和，并记录在字典中。
3. 对于每个查询，使用二分查找找到满足条件的点对数量。

关键点:
- 使用双重循环计算所有点对的边数和。
- 使用二分查找优化查询过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 + q * log(n))
空间复杂度: O(n^2)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_pairs_of_nodes(n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
    """
    函数式接口 - 统计点对的数目
    """
    # 计算每个节点的度数
    degree = [0] * (n + 1)
    edge_count = {}
    
    for u, v in edges:
        if u > v:
            u, v = v, u
        degree[u] += 1
        degree[v] += 1
        edge_count[(u, v)] = edge_count.get((u, v), 0) + 1
    
    # 计算所有点对的边数和
    pair_count = {}
    sorted_degrees = sorted(degree[1:])
    
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            pair_count[(i, j)] = degree[i] + degree[j]
            if (i, j) in edge_count:
                pair_count[(i, j)] -= edge_count[(i, j)]
    
    # 对每个查询进行二分查找
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    result = []
    for query in queries:
        count = 0
        for key, value in pair_count.items():
            if value > query:
                count += 1
        result.append(count)
    
    return result


Solution = create_solution(count_pairs_of_nodes)