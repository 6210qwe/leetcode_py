# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 114
标题: Flatten Binary Tree to Linked List
难度: medium
链接: https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
题目类型: 栈、树、深度优先搜索、链表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
114. 二叉树展开为链表 - 给你二叉树的根结点 root ，请你将它展开为一个单链表： * 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。 * 展开后的单链表应该与二叉树 先序遍历 [https://baike.baidu.com/item/%E5%85%88%E5%BA%8F%E9%81%8D%E5%8E%86/6442839?fr=aladdin] 顺序相同。 示例 1： [https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg] 输入：root = [1,2,5,3,4,null,6] 输出：[1,null,2,null,3,null,4,null,5,null,6] 示例 2： 输入：root = [] 输出：[] 示例 3： 输入：root = [0] 输出：[0] 提示： * 树中结点数在范围 [0, 2000] 内 * -100 <= Node.val <= 100 进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用后序遍历，将左子树插入到根节点和右子树之间

算法步骤:
1. 如果节点为空，返回
2. 递归处理左子树和右子树
3. 将左子树的最右节点连接到右子树
4. 将根节点的右指针指向左子树，左指针置空

关键点:
- 原地修改，O(1)空间复杂度
- 时间复杂度O(n)，空间复杂度O(h)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要访问每个节点一次
空间复杂度: O(h) - 递归栈深度，h为树的高度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def flatten_binary_tree_to_linked_list(root: Optional[TreeNode]) -> None:
    """
    函数式接口 - 将二叉树展开为链表（原地修改）
    
    实现思路:
    使用后序遍历，将左子树插入到根节点和右子树之间，实现原地展开。
    
    Args:
        root: 二叉树的根节点（原地修改）
        
    Returns:
        None（原地修改）
        
    Example:
        >>> root = TreeNode.from_list([1, 2, 5, 3, 4, None, 6])
        >>> flatten_binary_tree_to_linked_list(root)
        >>> # root被展开为链表
    """
    if not root:
        return
    
    flatten_binary_tree_to_linked_list(root.left)
    flatten_binary_tree_to_linked_list(root.right)
    
    if root.left:
        # 找到左子树的最右节点
        rightmost = root.left
        while rightmost.right:
            rightmost = rightmost.right
        
        # 将左子树插入到根节点和右子树之间
        rightmost.right = root.right
        root.right = root.left
        root.left = None


# 自动生成Solution类（无需手动编写）
Solution = create_solution(flatten_binary_tree_to_linked_list)
