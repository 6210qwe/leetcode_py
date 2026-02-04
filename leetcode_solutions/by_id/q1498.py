# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1498
标题: Find a Corresponding Node of a Binary Tree in a Clone of That Tree
难度: easy
链接: https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1379. 找出克隆二叉树中的相同节点 - 给你两棵二叉树，原始树 original 和克隆树 cloned，以及一个位于原始树 original 中的目标节点 target。 其中，克隆树 cloned 是原始树 original 的一个 副本 。 请找出在树 cloned 中，与 target 相同 的节点，并返回对该节点的引用（在 C/C++ 等有指针的语言中返回 节点指针，其他语言返回节点本身）。 注意：你 不能 对两棵二叉树，以及 target 节点进行更改。只能 返回对克隆树 cloned 中已有的节点的引用。 示例 1: [https://assets.leetcode.com/uploads/2020/02/21/e1.png] 输入: tree = [7,4,3,null,null,6,19], target = 3 输出: 3 解释: 上图画出了树 original 和 cloned。target 节点在树 original 中，用绿色标记。答案是树 cloned 中的黄颜色的节点（其他示例类似）。 示例 2: [https://assets.leetcode.com/uploads/2020/02/21/e2.png] 输入: tree = [7], target = 7 输出: 7 示例 3: [https://assets.leetcode.com/uploads/2020/02/21/e3.png] 输入: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4 输出: 4 提示： * 树中节点的数量范围为 [1, 104] 。 * 同一棵树中，没有值相同的节点。 * target 节点是树 original 中的一个节点，并且不会是 null 。 进阶：如果树中允许出现值相同的节点，将如何解答？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 在克隆树中找到与目标节点相同的节点。

算法步骤:
1. 定义一个递归函数 `find_target`，该函数接受当前节点和目标值作为参数。
2. 如果当前节点为空，返回 None。
3. 如果当前节点的值等于目标值，返回当前节点。
4. 递归调用 `find_target` 检查左子树和右子树。
5. 返回左子树或右子树中找到的目标节点。

关键点:
- 使用递归进行深度优先搜索。
- 通过比较节点值来找到目标节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。最坏情况下需要遍历所有节点。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的空间复杂度取决于树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_target(node: Optional[TreeNode], target_val: int) -> Optional[TreeNode]:
    if not node:
        return None
    if node.val == target_val:
        return node
    left_result = find_target(node.left, target_val)
    if left_result:
        return left_result
    return find_target(node.right, target_val)

def solution_function_name(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    """
    函数式接口 - 在克隆树中找到与目标节点相同的节点
    """
    target_val = target.val
    return find_target(cloned, target_val)

Solution = create_solution(solution_function_name)