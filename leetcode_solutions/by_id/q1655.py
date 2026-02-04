# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1655
标题: Move Sub-Tree of N-Ary Tree
难度: hard
链接: https://leetcode.cn/problems/move-sub-tree-of-n-ary-tree/
题目类型: 树、深度优先搜索
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1516. 移动 N 叉树的子树 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过两次深度优先搜索（DFS）来找到目标节点和目标父节点，并将子树移动到新的位置。

算法步骤:
1. 使用 DFS 找到目标节点 `to_delete` 和其父节点 `parent_of_to_delete`。
2. 使用 DFS 找到目标父节点 `target_parent`。
3. 将 `to_delete` 从 `parent_of_to_delete` 的子节点列表中移除。
4. 将 `to_delete` 添加到 `target_parent` 的子节点列表中。

关键点:
- 使用递归的 DFS 来遍历树。
- 确保在移动子树时更新父节点引用。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点最多访问两次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的空间复杂度为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import Node

def move_sub_tree(root: 'Node', to_delete: int, target_parent: int) -> 'Node':
    """
    移动 N 叉树的子树
    :param root: 树的根节点
    :param to_delete: 要删除的节点值
    :param target_parent: 目标父节点值
    :return: 修改后的树的根节点
    """
    def find_node(node: 'Node', value: int, parent: 'Node' = None) -> (Optional['Node'], Optional['Node']):
        if node.val == value:
            return node, parent
        for child in node.children:
            found, found_parent = find_node(child, value, node)
            if found:
                return found, found_parent
        return None, None

    def remove_node(parent: 'Node', node: 'Node'):
        parent.children.remove(node)

    def add_node(parent: 'Node', node: 'Node'):
        parent.children.append(node)

    to_delete_node, parent_of_to_delete = find_node(root, to_delete)
    if not to_delete_node:
        return root

    target_parent_node, _ = find_node(root, target_parent)
    if not target_parent_node:
        return root

    if parent_of_to_delete:
        remove_node(parent_of_to_delete, to_delete_node)
    add_node(target_parent_node, to_delete_node)

    return root

Solution = create_solution(move_sub_tree)