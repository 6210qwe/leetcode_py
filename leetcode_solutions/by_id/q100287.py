# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100287
标题: 子结构判断
难度: medium
链接: https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 143. 子结构判断 - 给定两棵二叉树 tree1 和 tree2，判断 tree2 是否以 tree1 的某个节点为根的子树具有 相同的结构和节点值 。 注意，空树 不会是以 tree1 的某个节点为根的子树具有 相同的结构和节点值 。 示例 1： [https://pic.leetcode.cn/1694684670-vwyIgY-two_tree.png] 输入：tree1 = [1,7,5], tree2 = [6,1] 输出：false 解释：tree2 与 tree1 的一个子树没有相同的结构和节点值。 示例 2： [https://pic.leetcode.cn/1694685602-myWXCv-two_tree_2.png] 输入：tree1 = [3,6,7,1,8], tree2 = [6,1] 输出：true 解释：tree2 与 tree1 的一个子树拥有相同的结构和节点值。即 6 - > 1。 提示： 0 <= 节点个数 <= 10000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归方法来判断树 B 是否是树 A 的子结构。

算法步骤:
1. 如果树 A 或树 B 为空，则返回 False。
2. 定义一个辅助函数 `is_subtree`，用于判断从当前节点开始，树 B 是否是树 A 的子结构。
3. 在主函数中，首先检查当前节点是否满足条件，如果满足则返回 True。
4. 如果不满足，则递归检查左子树和右子树。
5. 辅助函数 `is_subtree` 用于逐节点比较树 A 和树 B 的节点值，如果所有节点都匹配则返回 True。

关键点:
- 递归地检查每个节点及其子树。
- 使用辅助函数来简化逻辑。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 是树 A 的节点数，n 是树 B 的节点数。在最坏情况下，需要对树 A 的每个节点都进行一次完整的树 B 的子结构匹配。
空间复杂度: O(h)，其中 h 是树 A 的高度。递归调用栈的深度最多为树 A 的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def is_subtree(A: TreeNode, B: TreeNode) -> bool:
    if not B:
        return True
    if not A or A.val != B.val:
        return False
    return is_subtree(A.left, B.left) and is_subtree(A.right, B.right)

def solution_function_name(A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:
    """
    函数式接口 - 判断树 B 是否是树 A 的子结构
    """
    if not A or not B:
        return False
    if is_subtree(A, B):
        return True
    return solution_function_name(A.left, B) or solution_function_name(A.right, B)

Solution = create_solution(solution_function_name)