# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000041
标题: Rank from Stream LCCI
难度: medium
链接: https://leetcode.cn/problems/rank-from-stream-lcci/
题目类型: 设计、树状数组、二分查找、数据流
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 10.10. 数字流的秩 - 假设你正在读取一串整数。每隔一段时间，你希望能找出数字 x 的秩(小于或等于 x 的值的个数)。请实现数据结构和算法来支持这些操作，也就是说： 实现 track(int x) 方法，每读入一个数字都会调用该方法； 实现 getRankOfNumber(int x) 方法，返回小于或等于 x 的值的个数。 注意：本题相对原题稍作改动 示例： 输入： ["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"] [[], [1], [0], [0]] 输出： [null,0,null,1] 提示： * x <= 50000 * track 和 getRankOfNumber 方法的调用次数均不超过 2000 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用平衡二叉搜索树（如 AVL 树）来存储读入的数字，并维护每个节点的子树大小。

算法步骤:
1. 初始化一个空的 AVL 树。
2. 在 track 方法中，将新数字插入到 AVL 树中，并更新节点的子树大小。
3. 在 getRankOfNumber 方法中，通过二分查找的方式找到小于或等于 x 的值的个数。

关键点:
- 使用 AVL 树来保持树的平衡，确保插入和查询操作的时间复杂度为 O(log n)。
- 维护每个节点的子树大小，以便快速计算秩。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n)，其中 n 是已经读入的数字数量。
空间复杂度: O(n)，需要存储所有读入的数字。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1  # 子树大小

class AVLTree:
    def __init__(self):
        self.root = None

    def _get_height(self, node: Optional[Node]) -> int:
        if not node:
            return 0
        return max(self._get_height(node.left), self._get_height(node.right)) + 1

    def _get_balance(self, node: Optional[Node]) -> int:
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, y: Node) -> Node:
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.size = 1 + self._get_size(y.left) + self._get_size(y.right)
        x.size = 1 + self._get_size(x.left) + self._get_size(x.right)
        return x

    def _left_rotate(self, x: Node) -> Node:
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.size = 1 + self._get_size(x.left) + self._get_size(x.right)
        y.size = 1 + self._get_size(y.left) + self._get_size(y.right)
        return y

    def _get_size(self, node: Optional[Node]) -> int:
        if not node:
            return 0
        return node.size

    def _insert(self, root: Optional[Node], key: int) -> Node:
        if not root:
            return Node(key)
        if key < root.val:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        root.size = 1 + self._get_size(root.left) + self._get_size(root.right)
        balance = self._get_balance(root)
        if balance > 1 and key < root.left.val:
            return self._right_rotate(root)
        if balance < -1 and key > root.right.val:
            return self._left_rotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)
        return root

    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)

    def _get_rank(self, node: Optional[Node], key: int) -> int:
        if not node:
            return 0
        if key == node.val:
            return self._get_size(node.left)
        elif key < node.val:
            return self._get_rank(node.left, key)
        else:
            return 1 + self._get_size(node.left) + self._get_rank(node.right, key)

    def get_rank(self, key: int) -> int:
        return self._get_rank(self.root, key)

class StreamRank:
    def __init__(self):
        self.tree = AVLTree()

    def track(self, x: int) -> None:
        self.tree.insert(x)

    def getRankOfNumber(self, x: int) -> int:
        return self.tree.get_rank(x)

Solution = create_solution(StreamRank)