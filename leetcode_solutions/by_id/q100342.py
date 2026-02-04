# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100342
标题: 判断是否为平衡二叉树
难度: easy
链接: https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 176. 判断是否为平衡二叉树 - 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。 示例 1： 输入：root = [3,9,20,null,null,15,7] 输出：true 解释：如下图 [https://pic.leetcode.cn/1695102431-vbmWJn-image.png] 示例 2： 输入：root = [1,2,2,3,3,null,null,4,4] 输出：false 解释：如下图 [https://pic.leetcode.cn/1695102434-WlaxCo-image.png] 提示： * 0 <= 树的结点个数 <= 10000 注意：本题与主站 110 题相同：https://leetcode.cn/problems/balanced-binary-tree/ [https://leetcode.cn/problems/balanced-binary-tree/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归的方法来判断每个节点的左右子树的高度差是否超过1。

算法步骤:
1. 定义一个辅助函数 `height` 来计算节点的高度。
2. 在主函数 `isBalanced` 中，对于每个节点，递归地检查其左右子树是否平衡，并且高度差不超过1。

关键点:
- 通过自底向上的递归方法，可以在计算高度的同时判断是否平衡，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为 h。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def isBalanced(root: Optional[TreeNode]) -> bool:
    def height(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
    
    return height(root) != -1

Solution = create_solution(isBalanced)