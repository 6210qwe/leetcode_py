# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 881
标题: Loud and Rich
难度: medium
链接: https://leetcode.cn/problems/loud-and-rich/
题目类型: 深度优先搜索、图、拓扑排序、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
851. 喧闹和富有 - 有一组 n 个人作为实验对象，从 0 到 n - 1 编号，其中每个人都有不同数目的钱，以及不同程度的安静值（quietness）。为了方便起见，我们将编号为 x 的人简称为 "person x "。 给你一个数组 richer ，其中 richer[i] = [ai, bi] 表示 person ai 比 person bi 更有钱。另给你一个整数数组 quiet ，其中 quiet[i] 是 person i 的安静值。richer 中所给出的数据 逻辑自洽（也就是说，在 person x 比 person y 更有钱的同时，不会出现 person y 比 person x 更有钱的情况 ）。 现在，返回一个整数数组 answer 作为答案，其中 answer[x] = y 的前提是，在所有拥有的钱肯定不少于 person x 的人中，person y 是最不安静的人（也就是安静值 quiet[y] 最小的人）。 示例 1： 输入：richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0] 输出：[5,5,2,5,4,5,6,7] 解释： answer[0] = 5， person 5 比 person 3 有更多的钱，person 3 比 person 1 有更多的钱，person 1 比 person 0 有更多的钱。 唯一较为安静（有较低的安静值 quiet[x]）的人是 person 7， 但是目前还不清楚他是否比 person 0 更有钱。 answer[7] = 7， 在所有拥有的钱肯定不少于 person 7 的人中（这可能包括 person 3，4，5，6 以及 7）， 最安静（有较低安静值 quiet[x]）的人是 person 7。 其他的答案也可以用类似的推理来解释。 示例 2： 输入：richer = [], quiet = [0] 输出：[0] 提示： * n == quiet.length * 1 <= n <= 500 * 0 <= quiet[i] < n * quiet 的所有值 互不相同 * 0 <= richer.length <= n * (n - 1) / 2 * 0 <= ai, bi < n * ai != bi * richer 中的所有数对 互不相同 * 对 richer 的观察在逻辑上是一致的
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历图，并记录每个节点的最小安静值。

算法步骤:
1. 构建一个图，表示每个人之间的财富关系。
2. 初始化一个结果数组 `answer`，初始值为每个人的索引。
3. 定义一个递归函数 `dfs`，用于更新每个节点的最小安静值。
4. 遍历每个人，如果当前节点的安静值大于其邻居节点的安静值，则更新当前节点的安静值。
5. 返回结果数组 `answer`。

关键点:
- 使用图来表示财富关系。
- 使用 DFS 进行遍历并更新安静值。
- 使用缓存来避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是人数，m 是 richer 数组的长度。
空间复杂度: O(n + m)，存储图和递归调用栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def loud_and_rich(richer: List[List[int]], quiet: List[int]) -> List[int]:
    n = len(quiet)
    graph = [[] for _ in range(n)]
    for a, b in richer:
        graph[b].append(a)

    answer = list(range(n))

    def dfs(node: int) -> None:
        if answer[node] != node:
            return
        for neighbor in graph[node]:
            dfs(neighbor)
            if quiet[answer[neighbor]] < quiet[answer[node]]:
                answer[node] = answer[neighbor]

    for i in range(n):
        dfs(i)

    return answer


Solution = create_solution(loud_and_rich)