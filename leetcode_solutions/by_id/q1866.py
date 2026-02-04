# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1866
标题: Restore the Array From Adjacent Pairs
难度: medium
链接: https://leetcode.cn/problems/restore-the-array-from-adjacent-pairs/
题目类型: 深度优先搜索、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1743. 从相邻元素对还原数组 - 存在一个由 n 个不同元素组成的整数数组 nums ，但你已经记不清具体内容。好在你还记得 nums 中的每一对相邻元素。 给你一个二维整数数组 adjacentPairs ，大小为 n - 1 ，其中每个 adjacentPairs[i] = [ui, vi] 表示元素 ui 和 vi 在 nums 中相邻。 题目数据保证所有由元素 nums[i] 和 nums[i+1] 组成的相邻元素对都存在于 adjacentPairs 中，存在形式可能是 [nums[i], nums[i+1]] ，也可能是 [nums[i+1], nums[i]] 。这些相邻元素对可以 按任意顺序 出现。 返回 原始数组 nums 。如果存在多种解答，返回 其中任意一个 即可。 示例 1： 输入：adjacentPairs = [[2,1],[3,4],[3,2]] 输出：[1,2,3,4] 解释：数组的所有相邻元素对都在 adjacentPairs 中。 特别要注意的是，adjacentPairs[i] 只表示两个元素相邻，并不保证其 左-右 顺序。 示例 2： 输入：adjacentPairs = [[4,-2],[1,4],[-3,1]] 输出：[-2,4,1,-3] 解释：数组中可能存在负数。 另一种解答是 [-3,1,4,-2] ，也会被视作正确答案。 示例 3： 输入：adjacentPairs = [[100000,-100000]] 输出：[100000,-100000] 提示： * nums.length == n * adjacentPairs.length == n - 1 * adjacentPairs[i].length == 2 * 2 <= n <= 105 * -105 <= nums[i], ui, vi <= 105 * 题目数据保证存在一些以 adjacentPairs 作为元素对的数组 nums
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用图的深度优先搜索（DFS）来重构数组。

算法步骤:
1. 构建邻接表表示图。
2. 找到起始节点（只有一个邻居的节点）。
3. 从起始节点开始进行深度优先搜索，构建数组。

关键点:
- 使用字典构建邻接表。
- 通过邻居数量找到起始节点。
- 使用集合记录访问过的节点，避免重复访问。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。构建邻接表和 DFS 都是线性时间复杂度。
空间复杂度: O(n)，存储邻接表和访问集合所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def restore_array(adjacent_pairs: List[List[int]]) -> List[int]:
    """
    从相邻元素对还原数组
    """
    # 构建邻接表
    graph = {}
    for u, v in adjacent_pairs:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    # 找到起始节点（只有一个邻居的节点）
    start_node = None
    for node, neighbors in graph.items():
        if len(neighbors) == 1:
            start_node = node
            break

    # 深度优先搜索构建数组
    result = []
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start_node)
    return result


Solution = create_solution(restore_array)