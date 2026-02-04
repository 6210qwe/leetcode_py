# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 955
标题: Complete Binary Tree Inserter
难度: medium
链接: https://leetcode.cn/problems/complete-binary-tree-inserter/
题目类型: 树、广度优先搜索、设计、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
919. 完全二叉树插入器 - 完全二叉树 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。 设计一种算法，将一个新节点插入到一棵完全二叉树中，并在插入后保持其完整。 实现 CBTInserter 类: * CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构； * CBTInserter.insert(int v) 向树中插入一个值为 Node.val == val的新节点 TreeNode。使树保持完全二叉树的状态，并返回插入节点 TreeNode 的父节点的值； * CBTInserter.get_root() 将返回树的头节点。 示例 1： [https://assets.leetcode.com/uploads/2021/08/03/lc-treeinsert.jpg] 输入 ["CBTInserter", "insert", "insert", "get_root"] [[[1, 2]], [3], [4], []] 输出 [null, 1, 2, [1, 2, 3, 4]] 解释 CBTInserter cBTInserter = new CBTInserter([1, 2]); cBTInserter.insert(3); // 返回 1 cBTInserter.insert(4); // 返回 2 cBTInserter.get_root(); // 返回 [1, 2, 3, 4] 提示： * 树中节点数量范围为 [1, 1000] * 0 <= Node.val <= 5000 * root 是完全二叉树 * 0 <= val <= 5000 * 每个测试用例最多调用 insert 和 get_root 操作 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用队列进行层次遍历，找到第一个不完全的节点作为插入点。

算法步骤:
1. 初始化时，使用队列进行层次遍历，找到所有未满的节点。
2. 插入时，找到队列中的第一个未满节点，插入新节点并更新队列。
3. 如果插入后该节点满了，则将其从队列中移除。

关键点:
- 使用队列维护未满节点，确保插入操作的时间复杂度为 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 插入和获取根节点的操作都是常数时间。
空间复杂度: O(n) - 最坏情况下，队列中可能包含所有节点。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node.left or not node.right:
                self.queue.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, v: int) -> int:
        parent = self.queue[0]
        new_node = TreeNode(v)
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.queue.pop(0)
        self.queue.append(new_node)
        return parent.val

    def get_root(self) -> TreeNode:
        return self.root

Solution = create_solution(CBTInserter)