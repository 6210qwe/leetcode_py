# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 988
标题: Flip Equivalent Binary Trees
难度: medium
链接: https://leetcode.cn/problems/flip-equivalent-binary-trees/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
951. 翻转等价二叉树 - 我们可以为二叉树 T 定义一个 翻转操作 ，如下所示：选择任意节点，然后交换它的左子树和右子树。 只要经过一定次数的翻转操作后，能使 X 等于 Y，我们就称二叉树 X 翻转 等价 于二叉树 Y。 这些树由根节点 root1 和 root2 给出。如果两个二叉树是否是翻转 等价 的树，则返回 true ，否则返回 false 。 示例 1： Flipped Trees Diagram [https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png] 输入：root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7] 输出：true 解释：我们翻转值为 1，3 以及 5 的三个节点。 示例 2: 输入: root1 = [], root2 = [] 输出: true 示例 3: 输入: root1 = [], root2 = [1] 输出: false 提示： * 每棵树节点数在 [0, 100] 范围内 * 每棵树中的每个值都是唯一的、在 [0, 99] 范围内的整数
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归方法检查两棵树是否通过翻转操作等价。

算法步骤:
1. 如果两棵树的当前节点都为空，返回 True。
2. 如果其中一个节点为空而另一个不为空，返回 False。
3. 如果当前节点的值不相等，返回 False。
4. 递归检查以下两种情况之一：
   - 当前节点的左子树与另一棵树的左子树等价，并且当前节点的右子树与另一棵树的右子树等价。
   - 当前节点的左子树与另一棵树的右子树等价，并且当前节点的右子树与另一棵树的左子树等价。

关键点:
- 递归地检查所有可能的翻转情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 其中 n 是树中节点的数量，因为每个节点最多被访问一次。
空间复杂度: O(h) - 其中 h 是树的高度，这是递归调用栈的最大深度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_flip_equivalent(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    """
    判断两棵二叉树是否通过翻转操作等价。
    """
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    
    # 检查两种可能的翻转情况
    return (is_flip_equivalent(root1.left, root2.left) and is_flip_equivalent(root1.right, root2.right)) or \
           (is_flip_equivalent(root1.left, root2.right) and is_flip_equivalent(root1.right, root2.left))


Solution = create_solution(is_flip_equivalent)