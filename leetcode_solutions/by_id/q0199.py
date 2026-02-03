# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 199
标题: Binary Tree Right Side View
难度: medium
链接: https://leetcode.cn/problems/binary-tree-right-side-view/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
199. 二叉树的右视图 - 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 示例 1： 输入：root = [1,2,3,null,5,null,4] 输出：[1,3,4] 解释： [https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png] 示例 2： 输入：root = [1,2,3,4,null,null,null,5] 输出：[1,3,4,5] 解释： [https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png] 示例 3： 输入：root = [1,null,3] 输出：[1,3] 示例 4： 输入：root = [] 输出：[] 提示: * 二叉树的节点个数的范围是 [0,100] * -100 <= Node.val <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: BFS层序遍历，每层取最后一个节点

算法步骤:
1. 使用BFS层序遍历二叉树
2. 每层遍历时，记录最后一个节点
3. 将每层的最后一个节点加入结果

关键点:
- 使用BFS层序遍历
- 时间复杂度O(n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要访问每个节点一次
空间复杂度: O(n) - 队列存储节点
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import deque
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def binary_tree_right_side_view(root: Optional[TreeNode]) -> List[int]:
    """
    函数式接口 - 二叉树的右视图
    
    实现思路:
    使用BFS层序遍历，每层取最后一个节点。
    
    Args:
        root: 二叉树的根节点
        
    Returns:
        从右侧看到的节点值列表
        
    Example:
        >>> root = TreeNode.from_list([1, 2, 3, None, 5, None, 4])
        >>> binary_tree_right_side_view(root)
        [1, 3, 4]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(binary_tree_right_side_view)
