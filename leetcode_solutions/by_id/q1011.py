# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1011
标题: Flip Binary Tree To Match Preorder Traversal
难度: medium
链接: https://leetcode.cn/problems/flip-binary-tree-to-match-preorder-traversal/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
971. 翻转二叉树以匹配先序遍历 - 给你一棵二叉树的根节点 root ，树中有 n 个节点，每个节点都有一个不同于其他节点且处于 1 到 n 之间的值。 另给你一个由 n 个值组成的行程序列 voyage ，表示 预期 的二叉树 先序遍历 [https://baike.baidu.com/item/%E5%85%88%E5%BA%8F%E9%81%8D%E5%8E%86/6442839?fr=aladdin] 结果。 通过交换节点的左右子树，可以 翻转 该二叉树中的任意节点。例，翻转节点 1 的效果如下： [https://assets.leetcode.com/uploads/2021/02/15/fliptree.jpg] 请翻转 最少 的树中节点，使二叉树的 先序遍历 与预期的遍历行程 voyage 相匹配 。 如果可以，则返回 翻转的 所有节点的值的列表。你可以按任何顺序返回答案。如果不能，则返回列表 [-1]。 示例 1： [https://assets.leetcode.com/uploads/2019/01/02/1219-01.png] 输入：root = [1,2], voyage = [2,1] 输出：[-1] 解释：翻转节点无法令先序遍历匹配预期行程。 示例 2： [https://assets.leetcode.com/uploads/2019/01/02/1219-02.png] 输入：root = [1,2,3], voyage = [1,3,2] 输出：[1] 解释：交换节点 2 和 3 来翻转节点 1 ，先序遍历可以匹配预期行程。 示例 3： [https://assets.leetcode.com/uploads/2019/01/02/1219-02.png] 输入：root = [1,2,3], voyage = [1,2,3] 输出：[] 解释：先序遍历已经匹配预期行程，所以不需要翻转节点。 提示： * 树中的节点数目为 n * n == voyage.length * 1 <= n <= 100 * 1 <= Node.val, voyage[i] <= n * 树中的所有值 互不相同 * voyage 中的所有值 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来遍历树，并在必要时翻转节点。

算法步骤:
1. 初始化一个结果列表 `flipped` 用于存储需要翻转的节点值。
2. 使用一个索引 `i` 来跟踪当前在 `voyage` 中的位置。
3. 定义一个递归函数 `dfs`，该函数接受当前节点作为参数。
4. 在 `dfs` 函数中：
   - 如果当前节点为空，直接返回。
   - 如果当前节点的值与 `voyage[i]` 不匹配，设置 `flipped` 为 `[-1]` 并返回。
   - 如果当前节点的左子节点存在且其值与 `voyage[i+1]` 不匹配，则翻转当前节点的左右子树，并将当前节点的值加入 `flipped`。
   - 递归调用 `dfs` 处理左子树和右子树。
5. 调用 `dfs` 函数从根节点开始遍历。
6. 返回 `flipped` 列表。

关键点:
- 使用索引来跟踪 `voyage` 中的当前位置。
- 在必要时翻转节点，并记录翻转的节点值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def flip_match_voyage(root: Optional[TreeNode], voyage: List[int]) -> List[int]:
    flipped = []
    i = 0
    
    def dfs(node: Optional[TreeNode]):
        nonlocal i
        if not node:
            return
        if node.val != voyage[i]:
            flipped[:] = [-1]
            return
        i += 1
        if node.left and i < len(voyage) and node.left.val != voyage[i]:
            flipped.append(node.val)
            dfs(node.right)
            dfs(node.left)
        else:
            dfs(node.left)
            dfs(node.right)
    
    dfs(root)
    return flipped

Solution = create_solution(flip_match_voyage)