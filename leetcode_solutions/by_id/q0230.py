# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 230
标题: Kth Smallest Element in a BST
难度: medium
链接: https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
题目类型: 树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
230. 二叉搜索树中第 K 小的元素 - 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（k 从 1 开始计数）。 示例 1： [https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg] 输入：root = [3,1,4,null,2], k = 1 输出：1 示例 2： [https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg] 输入：root = [5,3,6,2,4,null,null,1], k = 3 输出：3 提示： * 树中的节点数为 n 。 * 1 <= k <= n <= 104 * 0 <= Node.val <= 104 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 中序遍历BST，第k个访问的节点就是第k小的元素

算法步骤:
1. 使用中序遍历（递归或迭代）
2. 维护一个计数器，记录访问的节点数
3. 当计数器等于k时，返回当前节点值

关键点:
- 利用BST中序遍历的有序性
- 时间复杂度O(h+k)，空间复杂度O(h)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(h+k) - h为树的高度，k为要查找的位置
空间复杂度: O(h) - 递归栈深度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def kth_smallest_element_in_a_bst(root: Optional[TreeNode], k: int) -> int:
    """
    函数式接口 - 二叉搜索树中第K小的元素
    
    实现思路:
    中序遍历BST，第k个访问的节点就是第k小的元素。
    
    Args:
        root: 二叉搜索树的根节点
        k: 要查找的位置（从1开始）
        
    Returns:
        第k小的元素值
        
    Example:
        >>> root = TreeNode.from_list([3, 1, 4, None, 2])
        >>> kth_smallest_element_in_a_bst(root, 1)
        1
    """
    stack = []
    current = root
    count = 0
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        count += 1
        
        if count == k:
            return current.val
        
        current = current.right
    
    return -1  # 不应该到达这里


# 自动生成Solution类（无需手动编写）
Solution = create_solution(kth_smallest_element_in_a_bst)
