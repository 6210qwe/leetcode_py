# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 144
标题: Binary Tree Preorder Traversal
难度: easy
链接: https://leetcode.cn/problems/binary-tree-preorder-traversal/
题目类型: 栈、树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
144. 二叉树的前序遍历 - 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。 示例 1： 输入：root = [1,null,2,3] 输出：[1,2,3] 解释： [https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png] 示例 2： 输入：root = [1,2,3,4,5,null,8,null,null,6,7,9] 输出：[1,2,4,5,6,7,3,8,9] 解释： [https://assets.leetcode.com/uploads/2024/08/29/tree_2.png] 示例 3： 输入：root = [] 输出：[] 示例 4： 输入：root = [1] 输出：[1] 提示： * 树中节点数目在范围 [0, 100] 内 * -100 <= Node.val <= 100 进阶：递归算法很简单，你可以通过迭代算法完成吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈实现迭代前序遍历，先访问根节点，再访问左子树，最后访问右子树

算法步骤:
1. 使用栈存储节点
2. 先将根节点入栈
3. 每次出栈一个节点，访问它，然后先右后左入栈子节点

关键点:
- 使用栈实现迭代
- 时间复杂度O(n)，空间复杂度O(h)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历所有节点
空间复杂度: O(h) - h为树的高度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def binary_tree_preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    函数式接口 - 二叉树的前序遍历
    
    实现思路:
    使用栈实现迭代前序遍历，先访问根节点，再访问左子树，最后访问右子树。
    
    Args:
        root: 二叉树根节点
        
    Returns:
        前序遍历结果
        
    Example:
        >>> root = TreeNode.from_list([1,None,2,3])
        >>> binary_tree_preorder_traversal(root)
        [1, 2, 3]
    """
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(binary_tree_preorder_traversal)
