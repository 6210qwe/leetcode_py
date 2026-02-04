# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1040
标题: Maximum Binary Tree II
难度: medium
链接: https://leetcode.cn/problems/maximum-binary-tree-ii/
题目类型: 树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
998. 最大二叉树 II - 最大树 定义：一棵树，并满足：其中每个节点的值都大于其子树中的任何其他值。 给你最大树的根节点 root 和一个整数 val 。 就像 之前的问题 [https://leetcode.cn/problems/maximum-binary-tree/] 那样，给定的树是利用 Construct(a) 例程从列表 a（root = Construct(a)）递归地构建的： * 如果 a 为空，返回 null 。 * 否则，令 a[i] 作为 a 的最大元素。创建一个值为 a[i] 的根节点 root 。 * root 的左子树将被构建为 Construct([a[0], a[1], ..., a[i - 1]]) 。 * root 的右子树将被构建为 Construct([a[i + 1], a[i + 2], ..., a[a.length - 1]]) 。 * 返回 root 。 请注意，题目没有直接给出 a ，只是给出一个根节点 root = Construct(a) 。 假设 b 是 a 的副本，并在末尾附加值 val。题目数据保证 b 中的值互不相同。 返回 Construct(b) 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/23/maximum-binary-tree-1-1.png][https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/23/maximum-binary-tree-1-2.png] 输入：root = [4,1,3,null,null,2], val = 5 输出：[5,4,null,1,3,null,null,2] 解释：a = [1,4,2,3], b = [1,4,2,3,5] 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/23/maximum-binary-tree-2-1.png][https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/23/maximum-binary-tree-2-2.png] 输入：root = [5,2,4,null,1], val = 3 输出：[5,2,4,null,1,null,3] 解释：a = [2,1,5,4], b = [2,1,5,4,3] 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/23/maximum-binary-tree-3-1.png][https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/23/maximum-binary-tree-3-2.png] 输入：root = [5,2,3,null,1], val = 4 输出：[5,2,4,null,1,3] 解释：a = [2,1,5,3], b = [2,1,5,3,4] 提示： * 树中节点数目在范围 [1, 100] 内 * 1 <= Node.val <= 100 * 树中的所有值 互不相同 * 1 <= val <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 在现有最大二叉树的基础上，插入一个新的节点。如果新节点的值大于当前根节点的值，则新节点成为新的根节点，原树成为新节点的左子树。否则，递归地在右子树中找到合适的位置插入新节点。

算法步骤:
1. 如果新节点的值大于当前根节点的值，创建一个新节点作为根节点，并将原树作为新节点的左子树。
2. 否则，递归地在右子树中找到合适的位置插入新节点。

关键点:
- 通过递归找到合适的位置插入新节点。
- 确保新节点插入后仍然满足最大二叉树的定义。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(h)，其中 h 是树的高度。最坏情况下，树的高度为 n，即 O(n)。
空间复杂度: O(h)，递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def insert_into_max_tree(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    在现有最大二叉树的基础上，插入一个新的节点。
    """
    if not root or root.val < val:
        new_node = TreeNode(val)
        new_node.left = root
        return new_node
    
    # 递归地在右子树中找到合适的位置插入新节点
    root.right = insert_into_max_tree(root.right, val)
    return root

Solution = create_solution(insert_into_max_tree)