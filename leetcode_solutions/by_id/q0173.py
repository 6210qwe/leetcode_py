# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 173
标题: Binary Search Tree Iterator
难度: medium
链接: https://leetcode.cn/problems/binary-search-tree-iterator/
题目类型: 栈、树、设计、二叉搜索树、二叉树、迭代器
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
173. 二叉搜索树迭代器 - 实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器： * BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。 * boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。 * int next()将指针向右移动，然后返回指针处的数字。 注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。 示例： [https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png] 输入 ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"] [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []] 输出 [null, 3, 7, true, 9, true, 15, true, 20, false] 解释 BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]); bSTIterator.next(); // 返回 3 bSTIterator.next(); // 返回 7 bSTIterator.hasNext(); // 返回 True bSTIterator.next(); // 返回 9 bSTIterator.hasNext(); // 返回 True bSTIterator.next(); // 返回 15 bSTIterator.hasNext(); // 返回 True bSTIterator.next(); // 返回 20 bSTIterator.hasNext(); // 返回 False 提示： * 树中节点的数目在范围 [1, 105] 内 * 0 <= Node.val <= 106 * 最多调用 105 次 hasNext 和 next 操作 进阶： * 你可以设计一个满足下述条件的解决方案吗？next() 和 hasNext() 操作均摊时间复杂度为 O(1) ，并使用 O(h) 内存。其中 h 是树的高度。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈实现中序遍历，按需加载节点

算法步骤:
1. 初始化时将根节点及其所有左子节点入栈
2. next操作：弹出栈顶节点，将其右子节点及其所有左子节点入栈
3. hasNext操作：检查栈是否为空

关键点:
- 使用栈实现中序遍历，按需加载
- next和hasNext均摊时间复杂度O(1)，空间复杂度O(h)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: next和hasNext均摊O(1)
空间复杂度: O(h) - h为树的高度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class BSTIterator:
    """
    二叉搜索树迭代器实现类
    """
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)
    
    def _push_left(self, node: Optional[TreeNode]):
        """将节点及其所有左子节点入栈"""
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self) -> int:
        """返回下一个最小的数"""
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val
    
    def hasNext(self) -> bool:
        """判断是否还有下一个数"""
        return len(self.stack) > 0


def binary_search_tree_iterator(root: Optional[TreeNode]) -> BSTIterator:
    """
    函数式接口 - 创建二叉搜索树迭代器
    
    实现思路:
    使用栈实现中序遍历，按需加载节点。
    
    Args:
        root: 二叉搜索树的根节点
        
    Returns:
        BSTIterator实例
        
    Example:
        >>> root = TreeNode.from_list([7, 3, 15, None, None, 9, 20])
        >>> iterator = binary_search_tree_iterator(root)
        >>> iterator.next()
        3
    """
    return BSTIterator(root)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(binary_search_tree_iterator)
