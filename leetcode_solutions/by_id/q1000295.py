# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000295
标题: 完全二叉树插入器
难度: medium
链接: https://leetcode.cn/problems/NaqhDT/
题目类型: 树、广度优先搜索、设计、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 043. 完全二叉树插入器 - 完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大，第 n 层有 2n-1 个节点）的，并且所有的节点都尽可能地集中在左侧。 设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作： * CBTInserter(TreeNode root) 使用根节点为 root 的给定树初始化该数据结构； * CBTInserter.insert(int v) 向树中插入一个新节点，节点类型为 TreeNode，值为 v 。使树保持完全二叉树的状态，并返回插入的新节点的父节点的值； * CBTInserter.get_root() 将返回树的根节点。 示例 1： 输入：inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]] 输出：[null,1,[1,2]] 示例 2： 输入：inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]] 输出：[null,3,4,[1,2,3,4,5,6,7,8]] 提示： * 最初给定的树是完全二叉树，且包含 1 到 1000 个节点。 * 每个测试用例最多调用 CBTInserter.insert 操作 10000 次。 * 给定节点或插入节点的每个值都在 0 到 5000 之间。 注意：本题与主站 919 题相同： https://leetcode.cn/problems/complete-binary-tree-inserter/ [https://leetcode.cn/problems/complete-binary-tree-inserter/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用队列来存储当前层的所有非满节点，以便在插入新节点时找到合适的父节点。

算法步骤:
1. 初始化时，使用广度优先搜索将所有非满节点加入队列。
2. 插入新节点时，从队列中取出第一个节点作为父节点，如果该节点左子节点为空，则插入左子节点；否则插入右子节点，并将该节点从队列中移除，同时将左右子节点加入队列。
3. 返回插入新节点的父节点的值。
4. 获取根节点时，直接返回根节点。

关键点:
- 使用队列来存储当前层的所有非满节点，确保插入操作的时间复杂度为 O(1)。
- 在插入新节点时，维护队列中的节点顺序，确保树的完全性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 
- 初始化: O(n)，其中 n 是树中节点的数量。
- 插入: O(1)。
- 获取根节点: O(1)。

空间复杂度: 
- 初始化: O(n)，队列中最多存储 n 个节点。
- 插入和获取根节点: O(1)。
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
        new_node = TreeNode(v)
        parent = self.queue[0]
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.queue.pop(0)
            self.queue.append(parent.left)
            self.queue.append(parent.right)
        return parent.val

    def get_root(self) -> TreeNode:
        return self.root


Solution = create_solution(CBTInserter)