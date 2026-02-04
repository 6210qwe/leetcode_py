# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1207
标题: Delete Nodes And Return Forest
难度: medium
链接: https://leetcode.cn/problems/delete-nodes-and-return-forest/
题目类型: 树、深度优先搜索、数组、哈希表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1110. 删点成林 - 给出二叉树的根节点 root，树上每个节点都有一个不同的值。 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。 返回森林中的每棵树。你可以按任意顺序组织答案。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/07/05/screen-shot-2019-07-01-at-53836-pm.png] 输入：root = [1,2,3,4,5,6,7], to_delete = [3,5] 输出：[[1,2,null,4],[6],[7]] 示例 2： 输入：root = [1,2,4,null,3], to_delete = [3] 输出：[[1,2,4]] 提示： * 树中的节点数最大为 1000。 * 每个节点都有一个介于 1 到 1000 之间的值，且各不相同。 * to_delete.length <= 1000 * to_delete 包含一些从 1 到 1000、各不相同的值。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历树，并在遇到需要删除的节点时将其子节点加入结果列表。

算法步骤:
1. 将 `to_delete` 转换为集合以实现 O(1) 查找。
2. 定义一个递归函数 `dfs` 来处理每个节点。
3. 在 `dfs` 函数中：
   - 如果当前节点为空，返回 None。
   - 递归处理左子节点和右子节点。
   - 如果当前节点需要删除，则将非空子节点加入结果列表，并返回 None。
   - 否则，返回当前节点。
4. 初始化结果列表，并调用 `dfs` 函数处理根节点。
5. 如果根节点不需要删除，将其加入结果列表。

关键点:
- 使用集合来存储 `to_delete` 以实现 O(1) 查找。
- 递归处理每个节点，并在需要删除的节点处断开连接。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只被访问一次。
空间复杂度: O(n)，递归调用栈的深度最多为树的高度，最坏情况下为 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def delNodes(root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    to_delete_set = set(to_delete)
    result = []

    def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None
        node.left = dfs(node.left)
        node.right = dfs(node.right)
        if node.val in to_delete_set:
            if node.left:
                result.append(node.left)
            if node.right:
                result.append(node.right)
            return None
        return node

    if dfs(root):
        result.append(root)
    return result

Solution = create_solution(delNodes)