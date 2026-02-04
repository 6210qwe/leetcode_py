# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3561
标题: Remove Methods From Project
难度: medium
链接: https://leetcode.cn/problems/remove-methods-from-project/
题目类型: 深度优先搜索、广度优先搜索、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3310. 移除可疑的方法 - 你正在维护一个项目，该项目有 n 个方法，编号从 0 到 n - 1。 给你两个整数 n 和 k，以及一个二维整数数组 invocations，其中 invocations[i] = [ai, bi] 表示方法 ai 调用了方法 bi。 已知如果方法 k 存在一个已知的 bug。那么方法 k 以及它直接或间接调用的任何方法都被视为 可疑方法 ，我们需要从项目中移除这些方法。 只有当一组方法没有被这组之外的任何方法调用时，这组方法才能被移除。 返回一个数组，包含移除所有 可疑方法 后剩下的所有方法。你可以以任意顺序返回答案。如果无法移除 所有 可疑方法，则 不 移除任何方法。 示例 1: 输入: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]] 输出: [0,1,2,3] 解释: [https://assets.leetcode.com/uploads/2024/07/18/graph-2.png] 方法 2 和方法 1 是可疑方法，但它们分别直接被方法 3 和方法 0 调用。由于方法 3 和方法 0 不是可疑方法，我们无法移除任何方法，故返回所有方法。 示例 2: 输入: n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]] 输出: [3,4] 解释: [https://assets.leetcode.com/uploads/2024/07/18/graph-3.png] 方法 0、方法 1 和方法 2 是可疑方法，且没有被任何其他方法直接调用。我们可以移除它们。 示例 3: 输入: n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]] 输出: [] 解释: [https://assets.leetcode.com/uploads/2024/07/20/graph.png] 所有方法都是可疑方法。我们可以移除它们。 提示: * 1 <= n <= 105 * 0 <= k <= n - 1 * 0 <= invocations.length <= 2 * 105 * invocations[i] == [ai, bi] * 0 <= ai, bi <= n - 1 * ai != bi * invocations[i] != invocations[j]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来标记所有可疑方法，并检查是否有非可疑方法调用了这些可疑方法。

算法步骤:
1. 构建反向图，记录每个方法被哪些方法调用。
2. 使用 DFS 从可疑方法 k 开始，标记所有可疑方法。
3. 检查每个可疑方法是否被非可疑方法调用，如果有则返回所有方法。
4. 如果没有非可疑方法调用可疑方法，则返回剩余的方法。

关键点:
- 使用反向图来快速查找调用关系。
- 使用 DFS 标记可疑方法。
- 检查可疑方法是否可以被移除。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是方法的数量，m 是调用关系的数量。
空间复杂度: O(n + m)，用于存储反向图和访问标记。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(n: int, k: int, invocations: List[List[int]]) -> List[int]:
    """
    函数式接口 - 实现最优解法
    """
    # 构建反向图
    reverse_graph = [[] for _ in range(n)]
    for a, b in invocations:
        reverse_graph[b].append(a)

    # 标记可疑方法
    suspicious = [False] * n
    def dfs(node: int):
        if suspicious[node]:
            return
        suspicious[node] = True
        for neighbor in reverse_graph[node]:
            dfs(neighbor)

    dfs(k)

    # 检查可疑方法是否可以被移除
    can_remove = True
    for i in range(n):
        if not suspicious[i]:
            for neighbor in reverse_graph[i]:
                if suspicious[neighbor]:
                    can_remove = False
                    break
        if not can_remove:
            break

    if not can_remove:
        return list(range(n))
    else:
        return [i for i in range(n) if not suspicious[i]]


Solution = create_solution(solution_function_name)