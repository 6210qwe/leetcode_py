# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000315
标题: 把二叉搜索树转换为累加树
难度: medium
链接: https://leetcode.cn/problems/w6cpku/
题目类型: 树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 054. 把二叉搜索树转换为累加树 - 给定一个二叉搜索树，请将它的每个节点的值替换成树中大于或者等于该节点值的所有节点值之和。 提醒一下，二叉搜索树满足下列约束条件： * 节点的左子树仅包含键 小于 节点键的节点。 * 节点的右子树仅包含键 大于 节点键的节点。 * 左右子树也必须是二叉搜索树。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/05/03/tree.png] 输入：root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8] 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8] 示例 2： 输入：root = [0,null,1] 输出：[1,null,1] 示例 3： 输入：root = [1,0,2] 输出：[3,3,2] 示例 4： 输入：root = [3,2,4,1] 输出：[7,9,4,10] 提示： * 树中的节点数介于 0 和 104 之间。 * 每个节点的值介于 -104 和 104 之间。 * 树中的所有值 互不相同 。 * 给定的树为二叉搜索树。 注意： * 本题与主站 538 题相同： https://leetcode.cn/problems/convert-bst-to-greater-tree/ [https://leetcode.cn/problems/convert-bst-to-greater-tree/] * 本题与主站 1038 题相同：https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/ [https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用反向中序遍历（右-根-左）来累积节点值。

算法步骤:
1. 初始化一个全局变量 `total` 为 0。
2. 定义一个递归函数 `dfs`，进行反向中序遍历：
   - 递归遍历右子树。
   - 更新当前节点的值为 `total + node.val`，并更新 `total`。
   - 递归遍历左子树。
3. 调用 `dfs` 函数从根节点开始遍历。

关键点:
- 反向中序遍历确保了节点值按降序访问。
- 使用全局变量 `total` 来累积节点值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def convert_bst(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    将二叉搜索树转换为累加树
    """
    total = 0

    def dfs(node: Optional[TreeNode]):
        nonlocal total
        if not node:
            return
        # 先遍历右子树
        dfs(node.right)
        # 更新当前节点的值
        total += node.val
        node.val = total
        # 再遍历左子树
        dfs(node.left)

    dfs(root)
    return root

Solution = create_solution(convert_bst)