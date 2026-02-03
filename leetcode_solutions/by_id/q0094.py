# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 94
标题: Binary Tree Inorder Traversal
难度: easy
链接: https://leetcode.cn/problems/binary-tree-inorder-traversal/
题目类型: 栈、树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
94. 二叉树的中序遍历 - 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。 示例 1： [https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg] 输入：root = [1,null,2,3] 输出：[1,3,2] 示例 2： 输入：root = [] 输出：[] 示例 3： 输入：root = [1] 输出：[1] 提示： * 树中节点数目在范围 [0, 100] 内 * -100 <= Node.val <= 100 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 迭代实现中序遍历，使用栈模拟递归

算法步骤:
1. 使用栈存储节点
2. 从根节点开始，一直向左走，将所有左子节点入栈
3. 弹出栈顶节点，访问它
4. 将当前节点设为右子节点，重复步骤2-3
5. 直到栈为空且当前节点为None

关键点:
- 中序遍历：左->根->右
- 使用栈模拟递归过程
- 时间复杂度O(n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要访问每个节点一次
空间复杂度: O(n) - 栈的大小最多为树的高度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    函数式接口 - 迭代实现
    
    实现思路:
    使用栈迭代实现二叉树的中序遍历。
    
    Args:
        root: 二叉树的根节点
        
    Returns:
        中序遍历的结果列表
        
    Example:
        >>> root = TreeNode.from_list([1, None, 2, 3])
        >>> inorder_traversal(root)
        [1, 3, 2]
    """
    result = []
    stack = []
    current = root
    
    while current or stack:
        # 一直向左走，将所有左子节点入栈
        while current:
            stack.append(current)
            current = current.left
        
        # 弹出栈顶节点并访问
        current = stack.pop()
        result.append(current.val)
        
        # 转向右子树
        current = current.right
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(inorder_traversal)
