# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 925
标题: Construct Binary Tree from Preorder and Postorder Traversal
难度: medium
链接: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
题目类型: 树、数组、哈希表、分治、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
889. 根据前序和后序遍历构造二叉树 - 给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。 如果存在多个答案，您可以返回其中 任何 一个。 示例 1： [https://assets.leetcode.com/uploads/2021/07/24/lc-prepost.jpg] 输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1] 输出：[1,2,3,4,5,6,7] 示例 2: 输入: preorder = [1], postorder = [1] 输出: [1] 提示： * 1 <= preorder.length <= 30 * 1 <= preorder[i] <= preorder.length * preorder 中所有值都 不同 * postorder.length == preorder.length * 1 <= postorder[i] <= postorder.length * postorder 中所有值都 不同 * 保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归方法，通过前序遍历的第一个元素找到根节点，然后在后序遍历中找到左子树和右子树的边界。

算法步骤:
1. 初始化前序和后序遍历的索引。
2. 从前序遍历中获取根节点。
3. 在后序遍历中找到左子树的边界。
4. 递归构建左子树和右子树。

关键点:
- 通过前序遍历的第一个元素找到根节点。
- 在后序遍历中找到左子树的边界。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def build_tree(preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def construct(pre_start, pre_end, post_start, post_end):
        if pre_start > pre_end:
            return None
        
        # 前序遍历的第一个元素是根节点
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        
        if pre_start == pre_end:
            return root
        
        # 在后序遍历中找到左子树的边界
        left_root_val = preorder[pre_start + 1]
        left_size = postorder.index(left_root_val) - post_start + 1
        
        # 递归构建左子树和右子树
        root.left = construct(pre_start + 1, pre_start + left_size, post_start, post_start + left_size - 1)
        root.right = construct(pre_start + left_size + 1, pre_end, post_start + left_size, post_end - 1)
        
        return root
    
    return construct(0, len(preorder) - 1, 0, len(postorder) - 1)

Solution = create_solution(build_tree)