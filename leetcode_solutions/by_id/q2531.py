# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2531
标题: Create Components With Same Value
难度: hard
链接: https://leetcode.cn/problems/create-components-with-same-value/
题目类型: 树、深度优先搜索、数组、数学、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2440. 创建价值相同的连通块 - 有一棵 n 个节点的无向树，节点编号为 0 到 n - 1 。 给你一个长度为 n 下标从 0 开始的整数数组 nums ，其中 nums[i] 表示第 i 个节点的值。同时给你一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 与 bi 之间有一条边。 你可以 删除 一些边，将这棵树分成几个连通块。一个连通块的 价值 定义为这个连通块中 所有 节点 i 对应的 nums[i] 之和。 你需要删除一些边，删除后得到的各个连通块的价值都相等。请返回你可以删除的边数 最多 为多少。 示例 1： [https://assets.leetcode.com/uploads/2022/08/26/diagramdrawio.png] 输入：nums = [6,2,2,2,6], edges = [[0,1],[1,2],[1,3],[3,4]] 输出：2 解释：上图展示了我们可以删除边 [0,1] 和 [3,4] 。得到的连通块为 [0] ，[1,2,3] 和 [4] 。每个连通块的价值都为 6 。可以证明没有别的更好的删除方案存在了，所以答案为 2 。 示例 2： 输入：nums = [2], edges = [] 输出：0 解释：没有任何边可以删除。 提示： * 1 <= n <= 2 * 104 * nums.length == n * 1 <= nums[i] <= 50 * edges.length == n - 1 * edges[i].length == 2 * 0 <= edges[i][0], edges[i][1] <= n - 1 * edges 表示一棵合法的树。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来计算每个子树的总和，并检查是否可以将其分割成多个相同价值的连通块。

算法步骤:
1. 计算所有节点值的总和 total_sum。
2. 构建树的邻接表表示。
3. 使用 DFS 遍历树，计算每个子树的总和。
4. 检查每个子树的总和是否是 total_sum 的因子，如果是，则可以将其分割成多个相同价值的连通块。
5. 记录可以删除的边数。

关键点:
- 使用 DFS 计算子树的总和。
- 检查子树的总和是否是 total_sum 的因子。
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

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], edges: List[List[int]]) -> int:
    """
    函数式接口 - 返回可以删除的边数，使得每个连通块的价值都相等。
    """
    n = len(nums)
    if n == 1:
        return 0

    # 构建邻接表
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    total_sum = sum(nums)
    max_edges = 0

    def dfs(node: int, parent: int) -> int:
        nonlocal max_edges
        subtree_sum = nums[node]
        for neighbor in adj_list[node]:
            if neighbor != parent:
                child_sum = dfs(neighbor, node)
                if child_sum % total_sum == 0:
                    max_edges += 1
                subtree_sum += child_sum
        return subtree_sum

    dfs(0, -1)
    return max_edges


Solution = create_solution(solution_function_name)