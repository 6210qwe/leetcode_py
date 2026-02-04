# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100283
标题: 推理二叉树
难度: medium
链接: https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/
题目类型: 树、数组、哈希表、分治、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 124. 推理二叉树 - 某二叉树的先序遍历结果记录于整数数组 preorder，它的中序遍历结果记录于整数数组 inorder。请根据 preorder 和 inorder 的提示构造出这棵二叉树并返回其根节点。 注意：preorder 和 inorder 中均不含重复数字。 示例 1： [https://assets.leetcode.com/uploads/2021/02/19/tree.jpg] 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] 输出: [3,9,20,null,null,15,7] 示例 2: 输入: preorder = [-1], inorder = [-1] 输出: [-1] 提示: * 1 <= preorder.length <= 3000 * inorder.length == preorder.length * -3000 <= preorder[i], inorder[i] <= 3000 * inorder 均出现在 preorder * preorder 保证 为二叉树的前序遍历序列 * inorder 保证 为二叉树的中序遍历序列 注意：本题与主站 105 题重复：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ [https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过前序遍历和中序遍历构建二叉树。前序遍历的第一个元素是根节点，然后在中序遍历中找到该根节点的位置，从而确定左子树和右子树的范围。

算法步骤:
1. 使用哈希表存储中序遍历的值及其索引，以便快速查找。
2. 递归地构建二叉树：
   - 从前序遍历中获取当前子树的根节点。
   - 在中序遍历中找到根节点的位置，从而确定左子树和右子树的范围。
   - 递归地构建左子树和右子树。

关键点:
- 使用哈希表存储中序遍历的值及其索引，以减少查找时间。
- 递归地构建子树，并传递正确的索引范围。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是节点的数量。每个节点只访问一次。
空间复杂度: O(n)，用于存储哈希表和递归调用栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    def build(pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
        if pre_start > pre_end:
            return None
        
        root_val = preorder[pre_start]
        root_index = in_map[root_val]
        
        left_size = root_index - in_start
        right_size = in_end - root_index
        
        root = TreeNode(root_val)
        root.left = build(pre_start + 1, pre_start + left_size, in_start, root_index - 1)
        root.right = build(pre_start + left_size + 1, pre_end, root_index + 1, in_end)
        
        return root
    
    in_map = {val: idx for idx, val in enumerate(inorder)}
    return build(0, len(preorder) - 1, 0, len(inorder) - 1)

Solution = create_solution(build_tree)