# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2068
标题: Maximum Genetic Difference Query
难度: hard
链接: https://leetcode.cn/problems/maximum-genetic-difference-query/
题目类型: 位运算、深度优先搜索、字典树、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1938. 查询最大基因差 - 给你一棵 n 个节点的有根树，节点编号从 0 到 n - 1 。每个节点的编号表示这个节点的 独一无二的基因值 （也就是说节点 x 的基因值为 x）。两个基因值的 基因差 是两者的 异或和 。给你整数数组 parents ，其中 parents[i] 是节点 i 的父节点。如果节点 x 是树的 根 ，那么 parents[x] == -1 。 给你查询数组 queries ，其中 queries[i] = [nodei, vali] 。对于查询 i ，请你找到 vali 和 pi 的 最大基因差 ，其中 pi 是节点 nodei 到根之间的任意节点（包含 nodei 和根节点）。更正式的，你想要最大化 vali XOR pi 。 请你返回数组 ans ，其中 ans[i] 是第 i 个查询的答案。 示例 1： [https://assets.leetcode.com/uploads/2021/06/29/c1.png] 输入：parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]] 输出：[2,3,7] 解释：查询数组处理如下： - [0,2]：最大基因差的对应节点为 0 ，基因差为 2 XOR 0 = 2 。 - [3,2]：最大基因差的对应节点为 1 ，基因差为 2 XOR 1 = 3 。 - [2,5]：最大基因差的对应节点为 2 ，基因差为 5 XOR 2 = 7 。 示例 2： [https://assets.leetcode.com/uploads/2021/06/29/c2.png] 输入：parents = [3,7,-1,2,0,7,0,2], queries = [[4,6],[1,15],[0,5]] 输出：[6,14,7] 解释：查询数组处理如下： - [4,6]：最大基因差的对应节点为 0 ，基因差为 6 XOR 0 = 6 。 - [1,15]：最大基因差的对应节点为 1 ，基因差为 15 XOR 1 = 14 。 - [0,5]：最大基因差的对应节点为 2 ，基因差为 5 XOR 2 = 7 。 提示： * 2 <= parents.length <= 105 * 对于每个 不是 根节点的 i ，有 0 <= parents[i] <= parents.length - 1 。 * parents[root] == -1 * 1 <= queries.length <= 3 * 104 * 0 <= nodei <= parents.length - 1 * 0 <= vali <= 2 * 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Trie 树来存储从根节点到当前节点的路径，并在 DFS 过程中更新查询结果。

算法步骤:
1. 构建树结构。
2. 初始化 Trie 树。
3. 对每个查询，记录查询节点及其对应的值。
4. 使用 DFS 遍历树，在遍历过程中插入和删除节点到 Trie 树，并更新查询结果。

关键点:
- 使用 Trie 树来高效地计算最大异或值。
- 在 DFS 过程中动态维护 Trie 树。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q * log(max_val))，其中 n 是节点数，q 是查询数，max_val 是查询值的最大值。
空间复杂度: O(n * log(max_val))，Trie 树的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int):
        node = self.root
        for i in range(17, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.count += 1

    def delete(self, num: int):
        node = self.root
        nodes = [node]
        for i in range(17, -1, -1):
            bit = (num >> i) & 1
            node = node.children[bit]
            nodes.append(node)
            node.count -= 1
        for i in range(18, -1, -1):
            if nodes[i].count == 0:
                del nodes[i - 1].children[(num >> (17 - i)) & 1]

    def query(self, num: int) -> int:
        node = self.root
        result = 0
        for i in range(17, -1, -1):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit
            if toggled_bit in node.children:
                result |= (1 << i)
                node = node.children[toggled_bit]
            else:
                node = node.children[bit]
        return result

def dfs(node: int, tree: List[List[int]], queries: List[List[int]], results: List[int], trie: Trie):
    for query in queries[node]:
        results[query[0]] = trie.query(query[1])
    trie.insert(node)
    for child in tree[node]:
        dfs(child, tree, queries, results, trie)
    trie.delete(node)

def solution_function_name(parents: List[int], queries: List[List[int]]) -> List[int]:
    n = len(parents)
    tree = [[] for _ in range(n)]
    root = -1
    for i, p in enumerate(parents):
        if p != -1:
            tree[p].append(i)
        else:
            root = i

    query_map = [[] for _ in range(n)]
    for i, (node, val) in enumerate(queries):
        query_map[node].append((i, val))

    results = [0] * len(queries)
    trie = Trie()
    dfs(root, tree, query_map, results, trie)
    return results

Solution = create_solution(solution_function_name)