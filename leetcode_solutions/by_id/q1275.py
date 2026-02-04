# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1275
标题: Validate Binary Tree Nodes
难度: medium
链接: https://leetcode.cn/problems/validate-binary-tree-nodes/
题目类型: 树、深度优先搜索、广度优先搜索、并查集、图、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1361. 验证二叉树 - 二叉树上有 n 个节点，按从 0 到 n - 1 编号，其中节点 i 的两个子节点分别是 leftChild[i] 和 rightChild[i]。 只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true；否则返回 false。 如果节点 i 没有左子节点，那么 leftChild[i] 就等于 -1。右子节点也符合该规则。 注意：节点没有值，本问题中仅仅使用节点编号。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/23/1503_ex1.png] 输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1] 输出：true 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/23/1503_ex2.png] 输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1] 输出：false 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/23/1503_ex3.png] 输入：n = 2, leftChild = [1,0], rightChild = [-1,-1] 输出：false 提示： * n == leftChild.length == rightChild.length * 1 <= n <= 104 * -1 <= leftChild[i], rightChild[i] <= n - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来检查是否有环，并确保只有一个根节点。

算法步骤:
1. 初始化并查集。
2. 遍历每个节点的左右子节点，如果子节点已经被访问过，则说明存在环，返回 False。
3. 如果当前节点已经有父节点，也说明存在环，返回 False。
4. 合并当前节点和其子节点。
5. 最后检查是否只有一个根节点，如果有多个根节点则返回 False。

关键点:
- 使用并查集来高效地检查环。
- 确保只有一个根节点。
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

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def validate_binary_tree_nodes(n: int, left_child: List[int], right_child: List[int]) -> bool:
    uf = UnionFind(n)
    in_degree = [0] * n
    
    for i in range(n):
        left, right = left_child[i], right_child[i]
        if left != -1:
            if in_degree[left] == 1:
                return False
            in_degree[left] += 1
            if uf.find(i) == uf.find(left):
                return False
            uf.union(i, left)
        if right != -1:
            if in_degree[right] == 1:
                return False
            in_degree[right] += 1
            if uf.find(i) == uf.find(right):
                return False
            uf.union(i, right)
    
    return sum(1 for i in range(n) if uf.find(i) == i and in_degree[i] == 0) == 1

Solution = create_solution(validate_binary_tree_nodes)