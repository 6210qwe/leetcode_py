# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 572
标题: Subtree of Another Tree
难度: easy
链接: https://leetcode.cn/problems/subtree-of-another-tree/
题目类型: 树、深度优先搜索、二叉树、字符串匹配、哈希函数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
572. 另一棵树的子树 - 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。 示例 1： [https://pic.leetcode.cn/1724998676-cATjhe-image.png] 输入：root = [3,4,5,1,2], subRoot = [4,1,2] 输出：true 示例 2： [https://pic.leetcode.cn/1724998698-sEJWnq-image.png] 输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] 输出：false 提示： * root 树上的节点数量范围是 [1, 2000] * subRoot 树上的节点数量范围是 [1, 1000] * -104 <= root.val <= 104 * -104 <= subRoot.val <= 104
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
