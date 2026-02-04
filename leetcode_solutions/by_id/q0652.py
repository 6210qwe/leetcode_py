# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 652
标题: Find Duplicate Subtrees
难度: medium
链接: https://leetcode.cn/problems/find-duplicate-subtrees/
题目类型: 树、深度优先搜索、哈希表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
652. 寻找重复的子树 - 给你一棵二叉树的根节点 root ，返回所有 重复的子树 。 对于同一类的重复子树，你只需要返回其中任意 一棵 的根结点即可。 如果两棵树具有 相同的结构 和 相同的结点值 ，则认为二者是 重复 的。 示例 1： [https://assets.leetcode.com/uploads/2020/08/16/e1.jpg] 输入：root = [1,2,3,4,null,2,4,null,null,4] 输出：[[2,4],[4]] 示例 2： [https://assets.leetcode.com/uploads/2020/08/16/e2.jpg] 输入：root = [2,1,1] 输出：[[1]] 示例 3： [https://assets.leetcode.com/uploads/2020/08/16/e33.jpg] 输入：root = [2,2,2,3,null,3,null] 输出：[[2,3],[3]] 提示： * 树中的结点数在 [1, 5000] 范围内。 * -200 <= Node.val <= 200
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）遍历树，并将每个子树序列化为字符串。使用哈希表记录每个子树出现的次数，如果某个子树出现多次，则将其根节点加入结果列表。

算法步骤:
1. 定义一个递归函数 `traverse` 来遍历树，并将每个子树序列化为字符串。
2. 使用哈希表 `subtree_count` 记录每个子树出现的次数。
3. 如果某个子树出现两次，则将其根节点加入结果列表 `res`。
4. 返回结果列表 `res`。

关键点:
- 使用前序遍历（根-左-右）来序列化子树。
- 使用哈希表记录子树的出现次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只会被访问一次。
空间复杂度: O(n)，存储子树序列化的哈希表和递归调用栈的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_duplicate_subtrees(root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    """
    函数式接口 - 寻找重复的子树
    """
    def traverse(node: Optional[TreeNode]) -> str:
        if not node:
            return "#"
        
        # 序列化当前子树
        subtree = f"{node.val},{traverse(node.left)},{traverse(node.right)}"
        
        # 记录子树出现的次数
        subtree_count[subtree] += 1
        
        # 如果子树出现两次，将其根节点加入结果列表
        if subtree_count[subtree] == 2:
            res.append(node)
        
        return subtree
    
    subtree_count = {}
    res = []
    
    traverse(root)
    
    return res

Solution = create_solution(find_duplicate_subtrees)