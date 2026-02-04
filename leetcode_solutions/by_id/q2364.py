# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2364
标题: Longest Path With Different Adjacent Characters
难度: hard
链接: https://leetcode.cn/problems/longest-path-with-different-adjacent-characters/
题目类型: 树、深度优先搜索、图、拓扑排序、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2246. 相邻字符不同的最长路径 - 给你一棵 树（即一个连通、无向、无环图），根节点是节点 0 ，这棵树由编号从 0 到 n - 1 的 n 个节点组成。用下标从 0 开始、长度为 n 的数组 parent 来表示这棵树，其中 parent[i] 是节点 i 的父节点，由于节点 0 是根节点，所以 parent[0] == -1 。 另给你一个字符串 s ，长度也是 n ，其中 s[i] 表示分配给节点 i 的字符。 请你找出路径上任意一对相邻节点都没有分配到相同字符的 最长路径 ，并返回该路径的长度。 示例 1： [https://assets.leetcode.com/uploads/2022/03/25/testingdrawio.png] 输入：parent = [-1,0,0,1,1,2], s = "abacbe" 输出：3 解释：任意一对相邻节点字符都不同的最长路径是：0 -> 1 -> 3 。该路径的长度是 3 ，所以返回 3 。 可以证明不存在满足上述条件且比 3 更长的路径。 示例 2： [https://assets.leetcode.com/uploads/2022/03/25/graph2drawio.png] 输入：parent = [-1,0,0,0], s = "aabc" 输出：3 解释：任意一对相邻节点字符都不同的最长路径是：2 -> 0 -> 3 。该路径的长度为 3 ，所以返回 3 。 提示： * n == parent.length == s.length * 1 <= n <= 105 * 对所有 i >= 1 ，0 <= parent[i] <= n - 1 均成立 * parent[0] == -1 * parent 表示一棵有效的树 * s 仅由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历树，并在每个节点处计算以该节点为根的最长路径。

算法步骤:
1. 构建树的邻接表表示。
2. 定义一个递归函数 dfs(node)，用于计算以 node 为根的最长路径。
3. 在每个节点处，计算其子节点中的两条最长路径，并更新全局最长路径。
4. 返回以当前节点为根的最长路径。

关键点:
- 使用 DFS 遍历树。
- 在每个节点处维护两个最长路径，以便计算经过该节点的最长路径。
- 更新全局最长路径时，确保路径上的相邻节点字符不同。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是节点数。每个节点和边只访问一次。
空间复杂度: O(n)，递归调用栈的深度最多为 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def longest_path(parent: List[int], s: str) -> int:
    def build_tree(parent):
        tree = [[] for _ in range(len(parent))]
        for i in range(1, len(parent)):
            tree[parent[i]].append(i)
        return tree

    def dfs(node):
        nonlocal max_length
        if not tree[node]:
            return 1
        
        longest, second_longest = 0, 0
        for child in tree[node]:
            length = dfs(child)
            if s[child] != s[node]:
                if length > longest:
                    second_longest = longest
                    longest = length
                elif length > second_longest:
                    second_longest = length
        
        max_length = max(max_length, longest + second_longest + 1)
        return longest + 1

    tree = build_tree(parent)
    max_length = 1
    dfs(0)
    return max_length

Solution = create_solution(longest_path)