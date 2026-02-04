# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3191
标题: Maximum Score After Applying Operations on a Tree
难度: medium
链接: https://leetcode.cn/problems/maximum-score-after-applying-operations-on-a-tree/
题目类型: 树、深度优先搜索、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2925. 在树上执行操作以后得到的最大分数 - 有一棵 n 个节点的无向树，节点编号为 0 到 n - 1 ，根节点编号为 0 。给你一个长度为 n - 1 的二维整数数组 edges 表示这棵树，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 有一条边。 同时给你一个长度为 n 下标从 0 开始的整数数组 values ，其中 values[i] 表示第 i 个节点的值。 一开始你的分数为 0 ，每次操作中，你将执行： * 选择节点 i 。 * 将 values[i] 加入你的分数。 * 将 values[i] 变为 0 。 如果从根节点出发，到任意叶子节点经过的路径上的节点值之和都不等于 0 ，那么我们称这棵树是 健康的 。 你可以对这棵树执行任意次操作，但要求执行完所有操作以后树是 健康的 ，请你返回你可以获得的 最大分数 。 示例 1： [https://assets.leetcode.com/uploads/2023/10/11/graph-13-1.png] 输入：edges = [[0,1],[0,2],[0,3],[2,4],[4,5]], values = [5,2,5,2,1,1] 输出：11 解释：我们可以选择节点 1 ，2 ，3 ，4 和 5 。根节点的值是非 0 的。所以从根出发到任意叶子节点路径上节点值之和都不为 0 。所以树是健康的。你的得分之和为 values[1] + values[2] + values[3] + values[4] + values[5] = 11 。 11 是你对树执行任意次操作以后可以获得的最大得分之和。 示例 2： [https://assets.leetcode.com/uploads/2023/10/11/graph-14-2.png] 输入：edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [20,10,9,7,4,3,5] 输出：40 解释：我们选择节点 0 ，2 ，3 和 4 。 - 从 0 到 4 的节点值之和为 10 。 - 从 0 到 3 的节点值之和为 10 。 - 从 0 到 5 的节点值之和为 3 。 - 从 0 到 6 的节点值之和为 5 。 所以树是健康的。你的得分之和为 values[0] + values[2] + values[3] + values[4] = 40 。 40 是你对树执行任意次操作以后可以获得的最大得分之和。 提示： * 2 <= n <= 2 * 104 * edges.length == n - 1 * edges[i].length == 2 * 0 <= ai, bi < n * values.length == n * 1 <= values[i] <= 109 * 输入保证 edges 构成一棵合法的树。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历树，并在每个节点上计算两种情况下的最大得分：
1. 不选择当前节点，保留其值。
2. 选择当前节点，将其值加入得分。

算法步骤:
1. 构建树的邻接表表示。
2. 定义一个递归的 DFS 函数，计算每个子树的最大得分。
3. 在每个节点上，计算两种情况下的最大得分，并返回。
4. 最终结果是从根节点开始的 DFS 结果。

关键点:
- 使用 DFS 递归地处理每个子树。
- 在每个节点上，计算两种情况下的最大得分。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是节点数。每个节点只被访问一次。
空间复杂度: O(n)，用于存储树的邻接表和递归调用栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def max_score_after_operations(edges: List[List[int]], values: List[int]) -> int:
    # 构建树的邻接表表示
    n = len(values)
    tree = [[] for _ in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    def dfs(node: int, parent: int) -> int:
        # 计算不选择当前节点的情况下的子树最大得分
        score_without_current = sum(dfs(child, node) for child in tree[node] if child != parent)
        
        # 计算选择当前节点的情况下的子树最大得分
        score_with_current = values[node]
        for child in tree[node]:
            if child != parent:
                score_with_current += sum(values[sub_child] for sub_child in tree[child] if sub_child != node)
        
        # 返回两种情况下的最大得分
        return max(score_without_current, score_with_current - values[node])

    # 从根节点开始的 DFS 结果
    return sum(values) - dfs(0, -1)

Solution = create_solution(max_score_after_operations)