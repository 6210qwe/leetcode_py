# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1729
标题: Binary Search Tree Iterator II
难度: medium
链接: https://leetcode.cn/problems/binary-search-tree-iterator-ii/
题目类型: 栈、树、设计、二叉搜索树、二叉树、迭代器
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
实现一个二叉搜索树迭代器类BSTIterator，表示一个按中序遍历的二叉搜索树。此外，该类还支持以下操作：
- next()：返回迭代器当前元素，并将指针移动到下一个元素。
- hasNext()：如果存在下一个元素，则返回True；否则返回False。
- hasPrev()：如果存在前一个元素，则返回True；否则返回False。
- prev()：返回迭代器当前元素，并将指针移动到前一个元素。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈来模拟中序遍历，并使用双端队列来存储已经访问过的节点值。

算法步骤:
1. 初始化时，使用栈进行中序遍历，将所有左子节点压入栈中。
2. next() 方法：弹出栈顶元素，将其右子树的所有左子节点压入栈中，并将当前节点值加入双端队列。
3. prev() 方法：从双端队列的尾部取出上一个节点值。
4. hasNext() 和 hasPrev() 方法：分别检查栈是否为空和双端队列的长度。

关键点:
- 使用栈进行中序遍历。
- 使用双端队列存储已经访问过的节点值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) 对于 next(), prev(), hasNext(), hasPrev() 操作。
空间复杂度: O(h + n) 其中 h 是树的高度，n 是已经访问过的节点数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from collections import deque
from leetcode_solutions.utils.tree import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.history = deque()
        self._push_left(root)

    def _push_left(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration
        node = self.stack.pop()
        self.history.append(node.val)
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def hasPrev(self) -> bool:
        return len(self.history) > 1

    def prev(self) -> int:
        if not self.hasPrev():
            raise StopIteration
        self.history.pop()
        return self.history[-1]


# 示例用法
if __name__ == "__main__":
    # 构建示例二叉搜索树
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    # 创建迭代器
    iterator = BSTIterator(root)

    # 测试 next() 和 hasNext()
    while iterator.hasNext():
        print(iterator.next())

    # 测试 prev() 和 hasPrev()
    while iterator.hasPrev():
        print(iterator.prev())