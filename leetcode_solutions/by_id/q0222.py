# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 222
标题: Count Complete Tree Nodes
难度: easy
链接: https://leetcode.cn/problems/count-complete-tree-nodes/
题目类型: 位运算、树、二分查找、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
222. 完全二叉树的节点个数 - 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。 完全二叉树 [https://baike.baidu.com/item/%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91/7773232?fr=aladdin] 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层（从第 0 层开始），则该层包含 1~ 2h 个节点。 示例 1： [https://assets.leetcode.com/uploads/2021/01/14/complete.jpg] 输入：root = [1,2,3,4,5,6] 输出：6 示例 2： 输入：root = [] 输出：0 示例 3： 输入：root = [1] 输出：1 提示： * 树中节点的数目范围是[0, 5 * 104] * 0 <= Node.val <= 5 * 104 * 题目数据保证输入的树是 完全二叉树 进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 利用完全二叉树的性质，计算左右子树高度，判断最后一层是否完整

算法步骤:
1. 计算左子树和右子树的高度
2. 如果高度相同，说明左子树是满的，节点数为2^h-1，递归计算右子树
3. 如果高度不同，说明右子树是满的，节点数为2^(h-1)-1，递归计算左子树

关键点:
- 利用完全二叉树的性质优化
- 时间复杂度O(log^2 n)，空间复杂度O(log n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log^2 n) - 每次递归计算高度O(log n)，递归深度O(log n)
空间复杂度: O(log n) - 递归栈深度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_complete_tree_nodes(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 完全二叉树的节点个数
    
    实现思路:
    利用完全二叉树的性质，计算左右子树高度，判断最后一层是否完整。
    
    Args:
        root: 完全二叉树的根节点
        
    Returns:
        树的节点个数
        
    Example:
        >>> root = TreeNode.from_list([1, 2, 3, 4, 5, 6])
        >>> count_complete_tree_nodes(root)
        6
    """
    if not root:
        return 0
    
    def get_height(node):
        """计算树的高度"""
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    
    if left_height == right_height:
        # 左子树是满的
        return (1 << left_height) + count_complete_tree_nodes(root.right)
    else:
        # 右子树是满的
        return (1 << right_height) + count_complete_tree_nodes(root.left)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(count_complete_tree_nodes)
