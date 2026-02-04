# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1650
标题: Find Root of N-Ary Tree
难度: medium
链接: https://leetcode.cn/problems/find-root-of-n-ary-tree/
题目类型: 位运算、树、深度优先搜索、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1506. 找到 N 叉树的根节点 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用异或运算找到根节点。由于每个节点的值在所有子节点中出现一次，在根节点中出现一次，因此所有节点值的异或结果就是根节点的值。

算法步骤:
1. 初始化一个变量 `root_val` 为 0。
2. 遍历所有节点，对每个节点的值进行异或运算。
3. 最终 `root_val` 的值即为根节点的值。
4. 在节点列表中找到值为 `root_val` 的节点并返回。

关键点:
- 异或运算的性质：a ^ a = 0, a ^ 0 = a
- 根节点的值在所有节点值中只出现一次
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是节点的数量。需要遍历所有节点。
空间复杂度: O(1)，只需要常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def find_root(tree: List['Node']) -> 'Node':
    """
    函数式接口 - 找到 N 叉树的根节点
    """
    root_val = 0
    for node in tree:
        root_val ^= node.val
        for child in node.children:
            root_val ^= child.val
    
    for node in tree:
        if node.val == root_val:
            return node

Solution = create_solution(find_root)