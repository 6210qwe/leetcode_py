# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100315
标题: 验证二叉搜索树的后序遍历序列
难度: medium
链接: https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
题目类型: 栈、树、二叉搜索树、递归、数组、二叉树、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 152. 验证二叉搜索树的后序遍历序列 - 请实现一个函数来判断整数数组 postorder 是否为二叉搜索树的后序遍历结果。 示例 1： [https://pic.leetcode.cn/1706665328-rfvWhs-%E6%88%AA%E5%B1%8F2024-01-31%2009.41.48.png] 输入: postorder = [4,9,6,5,8] 输出: false 解释：从上图可以看出这不是一颗二叉搜索树 示例 2： [https://pic.leetcode.cn/1694762510-vVpTic-%E5%89%91%E6%8C%8733.png] 输入: postorder = [4,6,5,9,8] 输出: true 解释：可构建的二叉搜索树如上图 提示： * 数组长度 <= 1000 * postorder 中无重复数字
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 利用二叉搜索树的性质，后序遍历的最后一个元素是根节点，左子树的所有节点都小于根节点，右子树的所有节点都大于根节点。

算法步骤:
1. 找到第一个大于根节点的位置，划分左右子树。
2. 递归验证左子树和右子树是否满足二叉搜索树的性质。

关键点:
- 通过递归验证每个子树是否满足二叉搜索树的性质。
- 使用辅助函数来简化递归逻辑。
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
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def verify_postorder(postorder: List[int]) -> bool:
    """
    函数式接口 - 验证给定的后序遍历序列是否为二叉搜索树的后序遍历结果
    """
    def verify(start: int, end: int) -> bool:
        if start >= end:
            return True
        
        root = postorder[end]
        split = start
        while split < end and postorder[split] < root:
            split += 1
        
        for i in range(split, end):
            if postorder[i] < root:
                return False
        
        return verify(start, split - 1) and verify(split, end - 1)
    
    return verify(0, len(postorder) - 1)


Solution = create_solution(verify_postorder)