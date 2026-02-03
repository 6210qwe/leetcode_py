# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 108
标题: Convert Sorted Array to Binary Search Tree
难度: easy
链接: https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
题目类型: 树、二叉搜索树、数组、分治、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
108. 将有序数组转换为二叉搜索树 - 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。 示例 1： [https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg] 输入：nums = [-10,-3,0,5,9] 输出：[0,-3,9,-10,null,5] 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案： [https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg] 示例 2： [https://assets.leetcode.com/uploads/2021/02/18/btree.jpg] 输入：nums = [1,3] 输出：[3,1] 解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。 提示： * 1 <= nums.length <= 104 * -104 <= nums[i] <= 104 * nums 按 严格递增 顺序排列
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用分治法，每次选择中间元素作为根节点

算法步骤:
1. 如果数组为空，返回None
2. 选择数组中间位置的元素作为根节点
3. 递归构建左子树（左半部分）和右子树（右半部分）
4. 返回根节点

关键点:
- 选择中间元素保证平衡
- 时间复杂度O(n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要访问每个元素一次
空间复杂度: O(n) - 递归栈深度和树的空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def convert_sorted_array_to_binary_search_tree(nums: List[int]) -> Optional[TreeNode]:
    """
    函数式接口 - 将有序数组转换为平衡BST
    
    实现思路:
    使用分治法，每次选择中间元素作为根节点，递归构建左右子树。
    
    Args:
        nums: 有序整数数组
        
    Returns:
        平衡二叉搜索树的根节点
        
    Example:
        >>> root = convert_sorted_array_to_binary_search_tree([-10, -3, 0, 5, 9])
        >>> root.val
        0
    """
    if not nums:
        return None
    
    def build(left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        
        return root
    
    return build(0, len(nums) - 1)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(convert_sorted_array_to_binary_search_tree)
