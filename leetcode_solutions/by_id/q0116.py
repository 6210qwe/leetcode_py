# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 116
标题: Populating Next Right Pointers in Each Node
难度: medium
链接: https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/
题目类型: 树、深度优先搜索、广度优先搜索、链表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
116. 填充每个节点的下一个右侧节点指针 - 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下： struct Node { int val; Node *left; Node *right; Node *next; } 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。 初始状态下，所有 next 指针都被设置为 NULL。 示例 1： [https://assets.leetcode.com/uploads/2019/02/14/116_sample.png] 输入：root = [1,2,3,4,5,6,7] 输出：[1,#,2,3,#,4,5,6,7,#] 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。 示例 2: 输入：root = [] 输出：[] 提示： * 树中节点的数量在 [0, 212 - 1] 范围内 * -1000 <= node.val <= 1000 进阶： * 你只能使用常量级额外空间。 * 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用已建立的next指针连接下一层，实现O(1)空间复杂度

算法步骤:
1. 从根节点开始，逐层处理
2. 对于每一层，使用已建立的next指针遍历
3. 连接下一层的节点：左子节点的next指向右子节点
4. 如果当前节点有next，右子节点的next指向next节点的左子节点

关键点:
- 利用完美二叉树的性质
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要访问每个节点一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


# 扩展TreeNode以支持next指针
class Node(TreeNode):
    def __init__(self, val: int = 0, left: Optional['Node'] = None, 
                 right: Optional['Node'] = None, next: Optional['Node'] = None):
        super().__init__(val, left, right)
        self.next = next


def populating_next_right_pointers_in_each_node(root: Optional[Node]) -> Optional[Node]:
    """
    函数式接口 - 填充每个节点的下一个右侧节点指针
    
    实现思路:
    使用已建立的next指针连接下一层，实现O(1)空间复杂度。
    
    Args:
        root: 完美二叉树的根节点
        
    Returns:
        修改后的根节点
        
    Example:
        >>> # 需要先创建Node类型的树
        >>> root = Node(1, Node(2), Node(3))
        >>> populating_next_right_pointers_in_each_node(root)
    """
    if not root:
        return root
    
    leftmost = root
    
    while leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
            head = head.next
        leftmost = leftmost.left
    
    return root


# 自动生成Solution类（无需手动编写）
Solution = create_solution(populating_next_right_pointers_in_each_node)
