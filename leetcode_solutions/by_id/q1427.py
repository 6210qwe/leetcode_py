# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1427
标题: All Elements in Two Binary Search Trees
难度: medium
链接: https://leetcode.cn/problems/all-elements-in-two-binary-search-trees/
题目类型: 树、深度优先搜索、二叉搜索树、二叉树、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1305. 两棵二叉搜索树中的所有元素 - 给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。. 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/12/29/q2-e1.png] 输入：root1 = [2,1,4], root2 = [1,0,3] 输出：[0,1,1,2,3,4] 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/12/29/q2-e5-.png] 输入：root1 = [1,null,8], root2 = [8,1] 输出：[1,1,8,8] 提示： * 每棵树的节点数在 [0, 5000] 范围内 * -105 <= Node.val <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用中序遍历分别获取两棵树的有序数组，然后合并这两个有序数组。

算法步骤:
1. 对两棵树分别进行中序遍历，得到两个有序数组。
2. 合并两个有序数组。

关键点:
- 中序遍历二叉搜索树可以得到有序数组。
- 合并两个有序数组的时间复杂度为 O(n + m)，其中 n 和 m 分别是两个数组的长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是两棵树的节点数。
空间复杂度: O(n + m)，存储两个有序数组和最终结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """中序遍历二叉搜索树，返回有序数组"""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    """合并两个有序数组"""
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

def solution_function_name(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
    """
    函数式接口 - 返回两棵二叉搜索树中的所有元素，并按升序排序
    """
    # 中序遍历两棵树，得到两个有序数组
    arr1 = inorder_traversal(root1)
    arr2 = inorder_traversal(root2)
    
    # 合并两个有序数组
    return merge_sorted_arrays(arr1, arr2)

Solution = create_solution(solution_function_name)