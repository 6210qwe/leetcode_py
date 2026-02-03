# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 98
标题: Validate Binary Search Tree
难度: medium
链接: https://leetcode.cn/problems/validate-binary-search-tree/
题目类型: 树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
98. 验证二叉搜索树 - 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。 有效 二叉搜索树定义如下： * 节点的左子树只包含 严格小于 当前节点的数。 * 节点的右子树只包含 严格大于 当前节点的数。 * 所有左子树和右子树自身必须也是二叉搜索树。 示例 1： [https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg] 输入：root = [2,1,3] 输出：true 示例 2： [https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg] 输入：root = [5,1,4,null,null,3,6] 输出：false 解释：根节点的值是 5 ，但是右子节点的值是 4 。 提示： * 树中节点数目范围在[1, 104] 内 * -231 <= Node.val <= 231 - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 中序遍历，BST的中序遍历结果应该是严格递增的

算法步骤:
1. 使用中序遍历遍历BST
2. 记录前一个访问的节点值
3. 如果当前节点值 <= 前一个节点值，返回False
4. 遍历完成，返回True

关键点:
- BST的中序遍历结果是严格递增的
- 使用迭代实现，空间复杂度O(h)，h为树的高度
- 也可以使用递归，但需要传递上下界
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要访问每个节点一次
空间复杂度: O(h) - 递归栈深度或迭代栈的大小，h为树的高度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    函数式接口 - 中序遍历
    
    实现思路:
    使用中序遍历，BST的中序遍历结果应该是严格递增的。
    
    Args:
        root: 二叉树的根节点
        
    Returns:
        如果是有效的二叉搜索树返回True，否则返回False
        
    Example:
        >>> root = TreeNode.from_list([2, 1, 3])
        >>> is_valid_bst(root)
        True
    """
    stack = []
    current = root
    prev = None
    
    while current or stack:
        # 一直向左走
        while current:
            stack.append(current)
            current = current.left
        
        # 访问节点
        current = stack.pop()
        if prev is not None and current.val <= prev:
            return False
        prev = current.val
        
        # 转向右子树
        current = current.right
    
    return True


# 自动生成Solution类（无需手动编写）
Solution = create_solution(is_valid_bst)
