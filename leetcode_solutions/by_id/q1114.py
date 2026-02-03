# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1114
标题: Binary Search Tree to Greater Sum Tree
难度: medium
链接: https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/
题目类型: 树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1038. 从二叉搜索树到更大和树 - 给定一个二叉搜索树 root (BST)，请将它的每个节点的值替换成树中大于或者等于该节点值的所有节点值之和。 提醒一下， 二叉搜索树 满足下列约束条件： * 节点的左子树仅包含键 小于 节点键的节点。 * 节点的右子树仅包含键 大于 节点键的节点。 * 左右子树也必须是二叉搜索树。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/05/03/tree.png] 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8] 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8] 示例 2： 输入：root = [0,null,1] 输出：[1,null,1] 提示： * 树中的节点数在 [1, 100] 范围内。 * 0 <= Node.val <= 100 * 树中的所有值均 不重复 。 注意：该题目与 538: https://leetcode.cn/problems/convert-bst-to-greater-tree/ [https://leetcode.cn/problems/convert-bst-to-greater-tree/]相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
