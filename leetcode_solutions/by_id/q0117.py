# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 117
标题: Populating Next Right Pointers in Each Node II
难度: medium
链接: https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/
题目类型: 树、深度优先搜索、广度优先搜索、链表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
117. 填充每个节点的下一个右侧节点指针 II - 给定一个二叉树： struct Node { int val; Node *left; Node *right; Node *next; } 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。 初始状态下，所有 next 指针都被设置为 NULL 。 示例 1： [https://assets.leetcode.com/uploads/2019/02/15/117_sample.png] 输入：root = [1,2,3,4,5,null,7] 输出：[1,#,2,3,#,4,5,7,#] 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。 示例 2： 输入：root = [] 输出：[] 提示： * 树中的节点数在范围 [0, 6000] 内 * -100 <= Node.val <= 100 进阶： * 你只能使用常量级额外空间。 * 使用递归解题也符合要求，本题中递归程序的隐式栈空间不计入额外空间复杂度。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用虚拟头节点处理每一层，实现O(1)空间复杂度

算法步骤:
1. 从根节点开始，逐层处理
2. 使用虚拟头节点dummy连接下一层的第一个节点
3. 使用cur遍历当前层，连接下一层的节点
4. 移动到下一层继续处理

关键点:
- 使用虚拟头节点简化边界处理
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
from leetcode_solutions.utils.solution import create_solution


# 扩展TreeNode以支持next指针
class Node:
    def __init__(self, val: int = 0, left: Optional['Node'] = None, 
                 right: Optional['Node'] = None, next: Optional['Node'] = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def populating_next_right_pointers_in_each_node_ii(root: Optional[Node]) -> Optional[Node]:
    """
    函数式接口 - 填充每个节点的下一个右侧节点指针II
    
    实现思路:
    使用虚拟头节点处理每一层，实现O(1)空间复杂度。
    
    Args:
        root: 二叉树的根节点
        
    Returns:
        修改后的根节点
        
    Example:
        >>> # 需要先创建Node类型的树
        >>> root = Node(1, Node(2), Node(3))
        >>> populating_next_right_pointers_in_each_node_ii(root)
    """
    if not root:
        return root
    
    cur = root
    
    while cur:
        dummy = Node(0)
        tail = dummy
        
        while cur:
            if cur.left:
                tail.next = cur.left
                tail = tail.next
            if cur.right:
                tail.next = cur.right
                tail = tail.next
            cur = cur.next
        
        cur = dummy.next
    
    return root


# 自动生成Solution类（无需手动编写）
Solution = create_solution(populating_next_right_pointers_in_each_node_ii)
