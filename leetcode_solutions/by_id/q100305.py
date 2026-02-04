# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100305
标题: 将二叉搜索树转化为排序的双向链表
难度: medium
链接: https://leetcode.cn/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
题目类型: 栈、树、深度优先搜索、二叉搜索树、链表、二叉树、双向链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 155. 将二叉搜索树转化为排序的双向链表 - 将一个 二叉搜索树 就地转化为一个 已排序的双向循环链表 。 对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。 特别地，我们希望可以 就地 完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中最小元素的指针。 示例 1： 输入：root = [4,2,5,1,3] [https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png] 输出：[1,2,3,4,5] 解释：下图显示了转化后的二叉搜索树，实线表示后继关系，虚线表示前驱关系。 [https://assets.leetcode.com/uploads/2018/10/12/bstdllreturnbst.png] 示例 2： 输入：root = [2,1,3] 输出：[1,2,3] 示例 3： 输入：root = [] 输出：[] 解释：输入是空树，所以输出也是空链表。 示例 4： 输入：root = [1] 输出：[1] 提示： * -1000 <= Node.val <= 1000 * Node.left.val < Node.val < Node.right.val * Node.val 的所有值都是独一无二的 * 0 <= Number of Nodes <= 2000 注意：本题与主站 426 题相同：https://leetcode.cn/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/ [https://leetcode.cn/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用中序遍历将二叉搜索树转化为排序的双向链表。

算法步骤:
1. 定义两个指针 `prev` 和 `head`，分别用于记录当前节点的前驱节点和双向链表的头节点。
2. 使用中序遍历（递归或迭代）遍历二叉搜索树：
   - 访问左子树。
   - 处理当前节点：将当前节点的左指针指向前驱节点，前驱节点的右指针指向当前节点，并更新前驱节点为当前节点。
   - 访问右子树。
3. 最后，将双向链表的头节点和尾节点连接起来，形成循环链表。

关键点:
- 中序遍历保证了节点按从小到大的顺序访问。
- 通过调整节点的左右指针，实现双向链表的构建。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉搜索树的节点数。每个节点仅被访问一次。
空间复杂度: O(h)，其中 h 是二叉搜索树的高度。递归调用栈的空间复杂度为 O(h)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Solution:
    def treeToDoublyList(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        self.prev = None
        self.head = None

        def inorder(node: TreeNode):
            if not node:
                return

            # 访问左子树
            inorder(node.left)

            # 处理当前节点
            if self.prev:
                self.prev.right = node
                node.left = self.prev
            else:
                self.head = node  # 找到头节点

            self.prev = node  # 更新前驱节点

            # 访问右子树
            inorder(node.right)

        inorder(root)

        # 连接头节点和尾节点
        self.head.left = self.prev
        self.prev.right = self.head

        return self.head


Solution = create_solution(Solution)