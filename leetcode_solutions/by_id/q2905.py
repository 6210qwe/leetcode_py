# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2905
标题: Count Paths That Can Form a Palindrome in a Tree
难度: hard
链接: https://leetcode.cn/problems/count-paths-that-can-form-a palindrome-in-a-tree/
题目类型: 位运算、树、深度优先搜索、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2791. 树中可以形成回文的路径数 - 给你一棵 树（即，一个连通、无向且无环的图），根 节点为 0 ，由编号从 0 到 n - 1 的 n 个节点组成。这棵树用一个长度为 n 、下标从 0 开始的数组 parent 表示，其中 parent[i] 为节点 i 的父节点，由于节点 0 为根节点，所以 parent[0] == -1 。 另给你一个长度为 n 的字符串 s ，其中 s[i] 是分配给 i 和 parent[i] 之间的边的字符。s[0] 可以忽略。 找出满足 u < v ，且从 u 到 v 的路径上分配的字符可以 重新排列 形成 回文 的所有节点对 (u, v) ，并返回节点对的数目。 如果一个字符串正着读和反着读都相同，那么这个字符串就是一个 回文 。 示例 1： [https://assets.leetcode.com/uploads/2023/07/15/treedrawio-8drawio.png] 输入：parent = [-1,0,0,1,1,2], s = "acaabc" 输出：8 解释：符合题目要求的节点对分别是： - (0,1)、(0,2)、(1,3)、(1,4) 和 (2,5) ，路径上只有一个字符，满足回文定义。 - (2,3)，路径上字符形成的字符串是 "aca" ，满足回文定义。 - (1,5)，路径上字符形成的字符串是 "cac" ，满足回文定义。 - (3,5)，路径上字符形成的字符串是 "acac" ，可以重排形成回文 "acca" 。 示例 2： 输入：parent = [-1,0,0,0,0], s = "aaaaa" 输出：10 解释：任何满足 u < v 的节点对 (u,v) 都符合题目要求。 提示： * n == parent.length == s.length * 1 <= n <= 105 * 对于所有 i >= 1 ，0 <= parent[i] <= n - 1 均成立 * parent[0] == -1 * parent 表示一棵有效的树 * s 仅由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用位运算和DFS来记录每个节点到根节点的路径状态，并使用哈希表统计每种状态出现的次数。

算法步骤:
1. 构建树的邻接表表示。
2. 使用DFS遍历树，同时使用位运算记录从根节点到当前节点的路径状态。
3. 使用哈希表记录每种路径状态出现的次数。
4. 在DFS过程中，计算当前路径状态与之前路径状态的异或结果，如果结果是一个回文路径，则计数。

关键点:
- 使用位运算记录路径状态，通过异或操作判断是否可以形成回文。
- 使用哈希表记录每种路径状态出现的次数，以便快速查找。
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


def count_palindromic_paths(parent: List[int], s: str) -> int:
    def dfs(node: int, state: int) -> None:
        nonlocal count
        # 计算当前状态的回文路径数量
        count += freq[state]
        for char in range(26):
            new_state = state ^ (1 << char)
            count += freq[new_state]
        # 更新当前状态的频率
        freq[state] += 1
        # 递归处理子节点
        for child in tree[node]:
            edge_char = ord(s[child]) - ord('a')
            dfs(child, state ^ (1 << edge_char))
        # 回溯时减少当前状态的频率
        freq[state] -= 1

    n = len(parent)
    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[parent[i]].append(i)

    count = 0
    freq = [0] * (1 << 26)
    freq[0] = 1  # 空路径状态
    dfs(0, 0)
    return count


Solution = create_solution(count_palindromic_paths)