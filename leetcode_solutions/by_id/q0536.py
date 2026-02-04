# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 536
标题: Construct Binary Tree from String
难度: medium
链接: https://leetcode.cn/problems/construct-binary-tree-from-string/
题目类型: 栈、树、深度优先搜索、字符串、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
536. 从字符串生成二叉树 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈来构建二叉树。遍历字符串，根据字符的不同情况来处理节点的创建和连接。

算法步骤:
1. 初始化一个空栈。
2. 遍历字符串，使用一个临时变量 `num` 来存储当前数字。
3. 当遇到数字时，将其添加到 `num` 中。
4. 当遇到左括号 `(` 时，将当前节点压入栈，并开始处理新的子节点。
5. 当遇到右括号 `)` 时，弹出栈顶节点。
6. 当遇到 `-` 时，表示当前数字结束，创建一个新的 `TreeNode` 节点，并根据栈顶节点的情况决定是左子节点还是右子节点。
7. 最后返回根节点。

关键点:
- 使用栈来管理当前节点和其父节点的关系。
- 通过遍历字符串来逐步构建二叉树。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。每个字符只被处理一次。
空间复杂度: O(n)，最坏情况下栈的深度为 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def str2tree(s: str) -> Optional[TreeNode]:
    if not s:
        return None
    
    stack = []
    num = ''
    root = None
    
    for char in s:
        if char.isdigit() or char == '-':
            num += char
        elif char == '(':
            if num:
                node = TreeNode(int(num))
                num = ''
                if not root:
                    root = node
                if stack and stack[-1].left is None:
                    stack[-1].left = node
                elif stack and stack[-1].right is None:
                    stack[-1].right = node
                stack.append(node)
        elif char == ')':
            if num:
                node = TreeNode(int(num))
                num = ''
                if stack and stack[-1].left is None:
                    stack[-1].left = node
                elif stack and stack[-1].right is None:
                    stack[-1].right = node
                stack.pop()
    
    if num:
        return TreeNode(int(num))
    
    return root

Solution = create_solution(str2tree)