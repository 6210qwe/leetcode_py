# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2201
标题: Valid Arrangement of Pairs
难度: hard
链接: https://leetcode.cn/problems/valid-arrangement-of-pairs/
题目类型: 深度优先搜索、图、欧拉回路
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2097. 合法重新排列数对 - 给你一个下标从 0 开始的二维整数数组 pairs ，其中 pairs[i] = [starti, endi] 。如果 pairs 的一个重新排列，满足对每一个下标 i （ 1 <= i < pairs.length ）都有 endi-1 == starti ，那么我们就认为这个重新排列是 pairs 的一个 合法重新排列 。 请你返回 任意一个 pairs 的合法重新排列。 注意：数据保证至少存在一个 pairs 的合法重新排列。 示例 1： 输入：pairs = [[5,1],[4,5],[11,9],[9,4]] 输出：[[11,9],[9,4],[4,5],[5,1]] 解释： 输出的是一个合法重新排列，因为每一个 endi-1 都等于 starti 。 end0 = 9 == 9 = start1 end1 = 4 == 4 = start2 end2 = 5 == 5 = start3 示例 2： 输入：pairs = [[1,3],[3,2],[2,1]] 输出：[[1,3],[3,2],[2,1]] 解释： 输出的是一个合法重新排列，因为每一个 endi-1 都等于 starti 。 end0 = 3 == 3 = start1 end1 = 2 == 2 = start2 重新排列后的数组 [[2,1],[1,3],[3,2]] 和 [[3,2],[2,1],[1,3]] 都是合法的。 示例 3： 输入：pairs = [[1,2],[1,3],[2,1]] 输出：[[1,2],[2,1],[1,3]] 解释： 输出的是一个合法重新排列，因为每一个 endi-1 都等于 starti 。 end0 = 2 == 2 = start1 end1 = 1 == 1 = start2 提示： * 1 <= pairs.length <= 105 * pairs[i].length == 2 * 0 <= starti, endi <= 109 * starti != endi * pairs 中不存在一模一样的数对。 * 至少 存在 一个合法的 pairs 重新排列。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用欧拉路径（Eulerian Path）来解决这个问题。通过构建一个有向图，并找到一个欧拉路径，可以得到一个合法的重新排列。

算法步骤:
1. 构建有向图，记录每个节点的入度和出度。
2. 找到起点（出度比入度多1的节点）或任意一个节点作为起点。
3. 使用深度优先搜索（DFS）遍历图，构建欧拉路径。
4. 反转路径以得到正确的顺序。

关键点:
- 构建有向图时，使用字典来存储每个节点的邻居。
- 使用DFS遍历时，确保每个节点都被访问。
- 反转路径以得到正确的顺序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 pairs 的长度。构建图和DFS遍历的时间复杂度都是 O(n)。
空间复杂度: O(n)，用于存储图和路径。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(pairs: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 实现合法重新排列数对
    """
    from collections import defaultdict, deque

    # 构建有向图
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for u, v in pairs:
        graph[u].append(v)
        in_degree[v] += 1
        out_degree[u] += 1

    # 找到起点
    start = next((u for u in out_degree if out_degree[u] - in_degree[u] == 1), pairs[0][0])

    # 深度优先搜索构建欧拉路径
    path = []
    stack = [start]
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        path.append(stack.pop())

    # 反转路径以得到正确的顺序
    path.reverse()
    return [[path[i], path[i + 1]] for i in range(len(path) - 1)]


Solution = create_solution(solution_function_name)