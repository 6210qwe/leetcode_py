# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100346
标题: 求二叉搜索树的最近公共祖先
难度: easy
链接: https://leetcode.cn/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
题目类型: 树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 193. 二叉搜索树的最近公共祖先 - 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。 百度百科 [https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin]中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。” 例如，给定如下二叉搜索树: root = [6,2,8,0,4,7,9,null,null,3,5] [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/binarysearchtree_improved.png] 示例 1： 输入：root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8 输出：6 解释：节点 2 和节点 8 的最近公共祖先是 6。 示例 2： 输入：root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4 输出：2 解释：节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。 说明： * 所有节点的值都是唯一的。 * p、q 为不同节点且均存在于给定的二叉搜索树中。 注意：本题与主站 235 题相同：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/ [https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/]
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
