# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100289
标题: 判断对称二叉树
难度: easy
链接: https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 145. 判断对称二叉树 - 请设计一个函数判断一棵二叉树是否 轴对称 。 示例 1： [https://pic.leetcode.cn/1694689008-JaaRdV-%E8%BD%B4%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%911.png] 输入：root = [6,7,7,8,9,9,8] 输出：true 解释：从图中可看出树是轴对称的。 示例 2： [https://pic.leetcode.cn/1694689054-vENzHe-%E8%BD%B4%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%912.png] 输入：root = [1,2,2,null,3,null,3] 输出：false 解释：从图中可看出最后一层的节点不对称。 提示： 0 <= 节点个数 <= 1000 注意：本题与主站 101 题相同：https://leetcode.cn/problems/symmetric-tree/ [https://leetcode.cn/problems/symmetric-tree/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归方法，比较左子树和右子树是否镜像对称。

算法步骤:
1. 定义一个辅助函数 `is_mirror`，用于判断两个子树是否镜像对称。
2. 在 `is_mirror` 函数中，如果两个子树都为空，则返回 True；如果其中一个为空，则返回 False。
3. 如果两个子树的根节点值相等，则递归比较左子树的左子节点和右子树的右子节点，以及左子树的右子节点和右子树的左子节点。
4. 最终调用 `is_mirror` 函数，传入根节点的左右子树进行比较。

关键点:
- 递归地比较两棵子树是否镜像对称。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数。每个节点最多被访问一次。
空间复杂度: O(h)，其中 h 是二叉树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def is_symmetric(root: Optional[TreeNode]) -> bool:
    def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))
    
    return is_mirror(root, root)

Solution = create_solution(is_symmetric)