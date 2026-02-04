# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 508
标题: Most Frequent Subtree Sum
难度: medium
链接: https://leetcode.cn/problems/most-frequent-subtree-sum/
题目类型: 树、深度优先搜索、哈希表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
508. 出现次数最多的子树元素和 - 给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。 一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。 示例 1： [https://assets.leetcode.com/uploads/2021/04/24/freq1-tree.jpg] 输入: root = [5,2,-3] 输出: [2,-3,4] 示例 2： [https://assets.leetcode.com/uploads/2021/04/24/freq2-tree.jpg] 输入: root = [5,2,-5] 输出: [2] 提示: * 节点数在 [1, 104] 范围内 * -105 <= Node.val <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 计算每个节点的子树元素和，并使用哈希表记录每个子树元素和的出现次数。

算法步骤:
1. 定义一个递归函数 `dfs`，用于计算以当前节点为根的子树元素和。
2. 在递归过程中，更新哈希表中每个子树元素和的出现次数。
3. 遍历哈希表，找到出现次数最多的子树元素和。

关键点:
- 使用 DFS 计算子树元素和。
- 使用哈希表记录每个子树元素和的出现次数。
- 找到出现次数最多的子树元素和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只被访问一次。
空间复杂度: O(n)，递归调用栈的深度最多为 n，哈希表的空间复杂度也是 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_frequent_tree_sum(root: Optional[TreeNode]) -> List[int]:
    """
    返回出现次数最多的子树元素和。
    """
    if not root:
        return []

    # 哈希表记录每个子树元素和的出现次数
    sum_count = {}

    def dfs(node: TreeNode) -> int:
        """
        递归计算以当前节点为根的子树元素和。
        """
        if not node:
            return 0

        # 计算当前节点的子树元素和
        subtree_sum = node.val + dfs(node.left) + dfs(node.right)

        # 更新哈希表
        if subtree_sum in sum_count:
            sum_count[subtree_sum] += 1
        else:
            sum_count[subtree_sum] = 1

        return subtree_sum

    # 计算所有子树元素和
    dfs(root)

    # 找到出现次数最多的子树元素和
    max_count = max(sum_count.values())
    result = [subtree_sum for subtree_sum, count in sum_count.items() if count == max_count]

    return result

Solution = create_solution(find_frequent_tree_sum)