# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000319
标题: 两数之和 IV - 输入二叉搜索树
难度: easy
链接: https://leetcode.cn/problems/opLdQZ/
题目类型: 数组、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 056. 两数之和 IV - 输入二叉搜索树 - 给定一个二叉搜索树的 根节点 root 和一个整数 k , 请判断该二叉搜索树中是否存在两个节点它们的值之和等于 k 。假设二叉搜索树中节点的值均唯一。 示例 1： 输入: root = [8,6,10,5,7,9,11], k = 12 输出: true 解释: 节点 5 和节点 7 之和等于 12 示例 2： 输入: root = [8,6,10,5,7,9,11], k = 22 输出: false 解释: 不存在两个节点值之和为 22 的节点 提示： * 二叉树的节点个数的范围是 [1, 104]. * -104 <= Node.val <= 104 * root 为二叉搜索树 * -105 <= k <= 105 注意：本题与主站 653 题相同： https://leetcode.cn/problems/two-sum-iv-input-is-a-bst/ [https://leetcode.cn/problems/two-sum-iv-input-is-a-bst/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用中序遍历将二叉搜索树转换为有序数组，然后使用双指针法查找两数之和。

算法步骤:
1. 中序遍历二叉搜索树，将节点值存储到有序数组中。
2. 使用双指针法在有序数组中查找两数之和等于 k 的两个节点。

关键点:
- 中序遍历二叉搜索树可以得到一个有序数组。
- 双指针法可以在 O(n) 时间内找到两数之和。
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

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_target(root: Optional[TreeNode], k: int) -> bool:
    """
    函数式接口 - 判断二叉搜索树中是否存在两个节点它们的值之和等于 k
    """
    # 中序遍历二叉搜索树
    def inorder_traversal(node: Optional[TreeNode]) -> List[int]:
        if not node:
            return []
        return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

    # 将二叉搜索树转换为有序数组
    nums = inorder_traversal(root)
    
    # 使用双指针法查找两数之和
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == k:
            return True
        elif current_sum < k:
            left += 1
        else:
            right -= 1
    
    return False

Solution = create_solution(find_target)