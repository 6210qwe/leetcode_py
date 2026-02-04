# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1093
标题: Recover a Tree From Preorder Traversal
难度: hard
链接: https://leetcode.cn/problems/recover-a-tree-from-preorder-traversal/
题目类型: 树、深度优先搜索、字符串、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1028. 从先序遍历还原二叉树 - 我们从二叉树的根节点 root 开始进行深度优先搜索。 在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。 如果节点只有一个子节点，那么保证该子节点为左子节点。 给出遍历输出 S，还原树并返回其根节点 root。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/04/12/recover-a-tree-from-preorder-traversal.png] 输入："1-2--3--4-5--6--7" 输出：[1,2,5,3,4,6,7] 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/04/12/screen-shot-2019-04-10-at-114101-pm.png] 输入："1-2--3---4-5--6---7" 输出：[1,2,5,3,null,6,null,4,null,7] 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/04/12/screen-shot-2019-04-10-at-114955-pm.png] 输入："1-401--349---90--88" 输出：[1,401,null,349,88,90] 提示： * 原始树中的节点数介于 1 和 1000 之间。 * 每个节点的值介于 1 和 10 ^ 9 之间。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈来恢复树结构。通过遍历字符串，解析出每个节点的深度和值，然后根据深度将节点插入到正确的位置。

算法步骤:
1. 初始化一个栈，用于存储当前路径上的节点。
2. 遍历输入字符串，解析出每个节点的深度和值。
3. 根据深度调整栈，确保栈顶元素是当前节点的父节点。
4. 将当前节点插入到父节点的左子节点或右子节点。
5. 返回根节点。

关键点:
- 使用栈来维护当前路径上的节点。
- 通过深度来确定当前节点的位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是输入字符串的长度。每个字符最多被处理一次。
空间复杂度: O(h)，其中 h 是树的高度。栈的最大深度为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def recoverFromPreorder(traversal: str) -> Optional[TreeNode]:
    if not traversal:
        return None

    def get_depth_and_value(s: str, start: int) -> (int, int, int):
        depth = 0
        while s[start] == '-':
            depth += 1
            start += 1
        value_start = start
        while start < len(s) and s[start].isdigit():
            start += 1
        value = int(s[value_start:start])
        return depth, value, start

    root = TreeNode(int(traversal.split('-')[0]))
    stack = [(0, root)]
    i = len(str(root.val))

    while i < len(traversal):
        depth, value, next_i = get_depth_and_value(traversal, i)
        node = TreeNode(value)

        while stack[-1][0] >= depth:
            stack.pop()

        if not stack[-1][1].left:
            stack[-1][1].left = node
        else:
            stack[-1][1].right = node

        stack.append((depth, node))
        i = next_i

    return root


Solution = create_solution(recoverFromPreorder)