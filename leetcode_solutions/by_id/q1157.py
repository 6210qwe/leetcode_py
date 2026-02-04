# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1157
标题: Insufficient Nodes in Root to Leaf Paths
难度: medium
链接: https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1080. 根到叶路径上的不足节点 - 给你二叉树的根节点 root 和一个整数 limit ，请你同时删除树中所有 不足节点 ，并返回最终二叉树的根节点。 假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为 不足节点 ，需要被删除。 叶子节点，就是没有子节点的节点。 示例 1： [https://assets.leetcode.com/uploads/2019/06/05/insufficient-11.png] 输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1 输出：[1,2,3,4,null,null,7,8,9,null,14] 示例 2： [https://assets.leetcode.com/uploads/2019/06/05/insufficient-3.png] 输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22 输出：[5,4,8,11,null,17,4,7,null,null,null,5] 示例 3： [https://assets.leetcode.com/uploads/2019/06/11/screen-shot-2019-06-11-at-83301-pm.png] 输入：root = [1,2,-3,-5,null,4,null], limit = -1 输出：[1,null,-3,4] 提示： * 树中节点数目在范围 [1, 5000] 内 * -105 <= Node.val <= 105 * -109 <= limit <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来遍历树，并在回溯时决定是否删除当前节点。

算法步骤:
1. 定义一个递归函数 `dfs`，用于从当前节点开始进行深度优先搜索。
2. 在每个节点处，计算从根到当前节点的路径和。
3. 如果当前节点是叶子节点，检查路径和是否小于 `limit`，如果是则删除该节点。
4. 如果当前节点不是叶子节点，递归处理其左右子节点。
5. 回溯时，如果当前节点的某个子节点被删除且另一个子节点也不存在或被删除，则删除当前节点。
6. 返回处理后的根节点。

关键点:
- 使用递归进行深度优先搜索。
- 在回溯时根据子节点的状态决定是否删除当前节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只会被访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def insufficient_nodes_in_root_to_leaf_paths(root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
    """
    删除树中所有不足节点，并返回最终二叉树的根节点。
    """
    def dfs(node: Optional[TreeNode], path_sum: int) -> bool:
        if not node:
            return True
        
        # 计算当前路径和
        path_sum += node.val
        
        # 如果是叶子节点，检查路径和是否小于 limit
        if not node.left and not node.right:
            return path_sum < limit
        
        # 递归处理左右子节点
        left_deleted = dfs(node.left, path_sum)
        right_deleted = dfs(node.right, path_sum)
        
        # 如果左子节点被删除，设置左子节点为 None
        if left_deleted:
            node.left = None
        # 如果右子节点被删除，设置右子节点为 None
        if right_deleted:
            node.right = None
        
        # 如果当前节点的两个子节点都被删除，则删除当前节点
        return left_deleted and right_deleted
    
    # 如果根节点被删除，返回 None
    if dfs(root, 0):
        return None
    return root


Solution = create_solution(insufficient_nodes_in_root_to_leaf_paths)