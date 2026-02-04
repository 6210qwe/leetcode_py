# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 501
标题: Find Mode in Binary Search Tree
难度: easy
链接: https://leetcode.cn/problems/find-mode-in-binary-search-tree/
题目类型: 树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
501. 二叉搜索树中的众数 - 给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数 [https://baike.baidu.com/item/%E4%BC%97%E6%95%B0/44796]（即，出现频率最高的元素）。 如果树中有不止一个众数，可以按 任意顺序 返回。 假定 BST 满足如下定义： * 结点左子树中所含节点的值 小于等于 当前节点的值 * 结点右子树中所含节点的值 大于等于 当前节点的值 * 左子树和右子树都是二叉搜索树 示例 1： [https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg] 输入：root = [1,null,2,2] 输出：[2] 示例 2： 输入：root = [0] 输出：[0] 提示： * 树中节点的数目在范围 [1, 104] 内 * -105 <= Node.val <= 105 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用中序遍历（Inorder Traversal）来遍历二叉搜索树，并记录每个节点值的频率。由于二叉搜索树的中序遍历结果是有序的，因此可以轻松地找到众数。

算法步骤:
1. 定义一个辅助函数 `inorder_traversal` 来进行中序遍历。
2. 在遍历过程中，使用两个变量 `current_val` 和 `current_count` 来记录当前节点值及其出现次数。
3. 使用 `max_count` 来记录当前最大出现次数，并使用 `modes` 列表来存储所有出现次数为 `max_count` 的节点值。
4. 更新 `current_val` 和 `current_count`，并在需要时更新 `max_count` 和 `modes`。

关键点:
- 通过中序遍历，我们可以确保节点值是按升序访问的。
- 通过比较相邻节点值，可以高效地统计每个节点值的频率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点恰好被访问一次。
空间复杂度: O(1)，假设由递归产生的隐式调用栈的开销不被计算在内。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_mode(root: Optional[TreeNode]) -> List[int]:
    """
    函数式接口 - 找出二叉搜索树中的众数
    """
    def inorder_traversal(node: Optional[TreeNode]):
        nonlocal current_val, current_count, max_count, modes
        if not node:
            return
        inorder_traversal(node.left)
        
        # Update the current value and count
        if node.val == current_val:
            current_count += 1
        else:
            current_val = node.val
            current_count = 1
        
        # Update the modes list
        if current_count > max_count:
            max_count = current_count
            modes = [current_val]
        elif current_count == max_count:
            modes.append(current_val)
        
        inorder_traversal(node.right)

    current_val = None
    current_count = 0
    max_count = 0
    modes = []
    inorder_traversal(root)
    return modes

Solution = create_solution(find_mode)