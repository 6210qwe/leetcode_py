# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2217
标题: Step-By-Step Directions From a Binary Tree Node to Another
难度: medium
链接: https://leetcode.cn/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
题目类型: 树、深度优先搜索、字符串、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2096. 从二叉树一个节点到另一个节点每一步的方向 - 给你一棵 二叉树 的根节点 root ，这棵二叉树总共有 n 个节点。每个节点的值为 1 到 n 中的一个整数，且互不相同。给你一个整数 startValue ，表示起点节点 s 的值，和另一个不同的整数 destValue ，表示终点节点 t 的值。 请找到从节点 s 到节点 t 的 最短路径 ，并以字符串的形式返回每一步的方向。每一步用 大写 字母 'L' ，'R' 和 'U' 分别表示一种方向： * 'L' 表示从一个节点前往它的 左孩子 节点。 * 'R' 表示从一个节点前往它的 右孩子 节点。 * 'U' 表示从一个节点前往它的 父 节点。 请你返回从 s 到 t 最短路径 每一步的方向。 示例 1： [https://assets.leetcode.com/uploads/2021/11/15/eg1.png] 输入：root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6 输出："UURL" 解释：最短路径为：3 → 1 → 5 → 2 → 6 。 示例 2： [https://assets.leetcode.com/uploads/2021/11/15/eg2.png] 输入：root = [2,1], startValue = 2, destValue = 1 输出："L" 解释：最短路径为：2 → 1 。 提示： * 树中节点数目为 n 。 * 2 <= n <= 105 * 1 <= Node.val <= n * 树中所有节点的值 互不相同 。 * 1 <= startValue, destValue <= n * startValue != destValue
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 找到从根节点到起点和终点的路径，然后计算从起点到终点的最短路径。

算法步骤:
1. 使用 DFS 找到从根节点到起点和终点的路径。
2. 计算两个路径的公共前缀，这是它们的最近公共祖先。
3. 构建从起点到终点的路径，通过将起点路径中的非公共部分替换为 'U'，然后连接终点路径的非公共部分。

关键点:
- 使用 DFS 找到路径。
- 计算公共前缀以确定最近公共祖先。
- 构建最终路径时，使用 'U' 替换起点路径中的非公共部分。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。DFS 遍历整个树一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode

def find_path(root: TreeNode, target: int, path: List[str]) -> bool:
    if not root:
        return False
    if root.val == target:
        return True
    if find_path(root.left, target, path):
        path.append('L')
        return True
    if find_path(root.right, target, path):
        path.append('R')
        return True
    return False

def get_directions(root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    start_path = []
    dest_path = []
    
    # Find paths from root to start and destination
    find_path(root, startValue, start_path)
    find_path(root, destValue, dest_path)
    
    # Reverse the paths to make them easier to work with
    start_path.reverse()
    dest_path.reverse()
    
    # Find the common prefix
    i = 0
    while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
        i += 1
    
    # Construct the final path
    result = 'U' * (len(start_path) - i) + ''.join(dest_path[i:])
    return result

Solution = create_solution(get_directions)