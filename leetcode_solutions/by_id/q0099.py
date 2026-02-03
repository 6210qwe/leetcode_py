# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 99
标题: Recover Binary Search Tree
难度: medium
链接: https://leetcode.cn/problems/recover-binary-search-tree/
题目类型: 树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
99. 恢复二叉搜索树 - 给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。 示例 1： [https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg] 输入：root = [1,3,null,null,2] 输出：[3,1,null,null,2] 解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。 示例 2： [https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg] 输入：root = [3,1,4,null,null,2] 输出：[2,1,4,null,null,3] 解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。 提示： * 树上节点的数目在范围 [2, 1000] 内 * -231 <= Node.val <= 231 - 1 进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用 O(1) 空间的解决方案吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 中序遍历找到两个错误节点，然后交换它们的值

算法步骤:
1. 使用中序遍历遍历BST
2. 找到第一个错误节点：当前节点值 < 前一个节点值
3. 找到第二个错误节点：继续遍历，找到最后一个当前节点值 < 前一个节点值的位置
4. 交换两个错误节点的值

关键点:
- BST中序遍历应该是严格递增的
- 如果两个节点相邻，只会找到一对错误
- 如果两个节点不相邻，会找到两对错误，第二个错误节点是第二对的第一个节点
- 时间复杂度O(n)，空间复杂度O(h)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历树一次
空间复杂度: O(h) - 递归栈深度或迭代栈的大小，h为树的高度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def recover_tree(root: Optional[TreeNode]) -> None:
    """
    函数式接口 - 中序遍历找错误节点
    
    实现思路:
    使用中序遍历找到两个错误节点，然后交换它们的值。
    
    Args:
        root: 二叉搜索树的根节点，原地修改
        
    Returns:
        None（原地修改树）
        
    Example:
        >>> root = TreeNode.from_list([1, 3, None, None, 2])
        >>> recover_tree(root)
        >>> # 树被恢复
    """
    stack = []
    current = root
    prev = None
    first = None  # 第一个错误节点
    second = None  # 第二个错误节点
    
    while current or stack:
        # 一直向左走
        while current:
            stack.append(current)
            current = current.left
        
        # 访问节点
        current = stack.pop()
        
        # 检查是否违反BST性质
        if prev and prev.val > current.val:
            if first is None:
                first = prev
            second = current
        
        prev = current
        current = current.right
    
    # 交换两个错误节点的值
    if first and second:
        first.val, second.val = second.val, first.val


# 自动生成Solution类（无需手动编写）
Solution = create_solution(recover_tree)
