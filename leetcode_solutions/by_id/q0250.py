# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 250
标题: Count Univalue Subtrees
难度: medium
链接: https://leetcode.cn/problems/count-univalue-subtrees/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
250. 统计同值子树 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: DFS后序遍历，判断子树是否为同值子树

算法步骤:
1. 后序遍历，先处理左右子树
2. 如果左右子树都是同值子树，且值与当前节点相同，则当前子树也是同值子树
3. 统计同值子树数量

关键点:
- DFS后序遍历
- 时间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历所有节点
空间复杂度: O(h) - 递归栈空间，h为树高
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_unival_subtrees(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 统计同值子树
    
    实现思路:
    DFS后序遍历，判断子树是否为同值子树。
    
    Args:
        root: 二叉树根节点
        
    Returns:
        同值子树的数量
        
    Example:
        >>> root = TreeNode(5)
        >>> root.left = TreeNode(1)
        >>> root.right = TreeNode(5)
        >>> count_unival_subtrees(root)
        4
    """
    count = 0
    
    def dfs(node: Optional[TreeNode]) -> bool:
        """返回子树是否为同值子树"""
        nonlocal count
        
        if not node:
            return True
        
        left_uni = dfs(node.left)
        right_uni = dfs(node.right)
        
        # 检查左右子树是否都是同值子树，且值与当前节点相同
        if left_uni and right_uni:
            if (not node.left or node.left.val == node.val) and \
               (not node.right or node.right.val == node.val):
                count += 1
                return True
        
        return False
    
    dfs(root)
    return count


# 自动生成Solution类（无需手动编写）
Solution = create_solution(count_unival_subtrees)
