# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000313
标题: 二叉搜索树中的中序后继
难度: medium
链接: https://leetcode.cn/problems/P5rCT8/
题目类型: 树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 053. 二叉搜索树中的中序后继 - 给定一棵二叉搜索树和其中的一个节点 p ，找到该节点在树中的中序后继。如果节点没有中序后继，请返回 null 。 节点 p 的后继是值比 p.val 大的节点中键值最小的节点，即按中序遍历的顺序节点 p 的下一个节点。 示例 1： [https://assets.leetcode.com/uploads/2019/01/23/285_example_1.PNG] 输入：root = [2,1,3], p = 1 输出：2 解释：这里 1 的中序后继是 2。请注意 p 和返回值都应是 TreeNode 类型。 示例 2： [https://assets.leetcode.com/uploads/2019/01/23/285_example_2.PNG] 输入：root = [5,3,6,2,4,null,null,1], p = 6 输出：null 解释：因为给出的节点没有中序后继，所以答案就返回 null 了。 提示： * 树中节点的数目在范围 [1, 104] 内。 * -105 <= Node.val <= 105 * 树中各节点的值均保证唯一。 注意：本题与主站 285 题相同： https://leetcode.cn/problems/inorder-successor-in-bst/ [https://leetcode.cn/problems/inorder-successor-in-bst/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 利用二叉搜索树的性质，通过比较节点值来找到中序后继。

算法步骤:
1. 如果 p 有右子树，则中序后继是右子树中最左边的节点。
2. 如果 p 没有右子树，则从根节点开始，利用二叉搜索树的性质，逐步向下查找，记录大于 p.val 的最小节点。

关键点:
- 利用二叉搜索树的性质，通过比较节点值来缩小查找范围。
- 如果 p 有右子树，直接找右子树中最左边的节点。
- 如果 p 没有右子树，从根节点开始查找。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(h)，其中 h 是树的高度。在最坏情况下，树的高度为 n（退化成链表），因此时间复杂度为 O(n)。在最好情况下，树的高度为 log n（完全平衡树），因此时间复杂度为 O(log n)。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def inorder_successor(root: Optional[TreeNode], p: TreeNode) -> Optional[TreeNode]:
    """
    函数式接口 - 找到二叉搜索树中节点 p 的中序后继
    """
    # 如果 p 有右子树，则中序后继是右子树中最左边的节点
    if p.right:
        successor = p.right
        while successor.left:
            successor = successor.left
        return successor
    
    # 如果 p 没有右子树，从根节点开始查找
    successor = None
    current = root
    while current:
        if current.val > p.val:
            successor = current
            current = current.left
        else:
            current = current.right
    
    return successor

Solution = create_solution(inorder_successor)