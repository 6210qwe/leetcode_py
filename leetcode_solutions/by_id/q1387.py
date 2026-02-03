# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1387
标题: Find Elements in a Contaminated Binary Tree
难度: medium
链接: https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、设计、哈希表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1261. 在受污染的二叉树中查找元素 - 给出一个满足下述规则的二叉树： 1. root.val == 0 2. 对于任意 treeNode： a. 如果 treeNode.val 为 x 且 treeNode.left != null，那么 treeNode.left.val == 2 * x + 1 b. 如果 treeNode.val 为 x 且 treeNode.right != null，那么 treeNode.right.val == 2 * x + 2 现在这个二叉树受到「污染」，所有的 treeNode.val 都变成了 -1。 请你先还原二叉树，然后实现 FindElements 类： * FindElements(TreeNode* root) 用受污染的二叉树初始化对象，你需要先把它还原。 * bool find(int target) 判断目标值 target 是否存在于还原后的二叉树中并返回结果。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/11/16/untitled-diagram-4-1.jpg] 输入： ["FindElements","find","find"] [[[-1,null,-1]],[1],[2]] 输出： [null,false,true] 解释： FindElements findElements = new FindElements([-1,null,-1]); findElements.find(1); // return False findElements.find(2); // return True 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/11/16/untitled-diagram-4.jpg] 输入： ["FindElements","find","find","find"] [[[-1,-1,-1,-1,-1]],[1],[3],[5]] 输出： [null,true,true,false] 解释： FindElements findElements = new FindElements([-1,-1,-1,-1,-1]); findElements.find(1); // return True findElements.find(3); // return True findElements.find(5); // return False 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/11/16/untitled-diagram-4-1-1.jpg] 输入： ["FindElements","find","find","find","find"] [[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]] 输出： [null,true,false,false,true] 解释： FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]); findElements.find(2); // return True findElements.find(3); // return False findElements.find(4); // return False findElements.find(5); // return True 提示： * TreeNode.val == -1 * 二叉树的高度不超过 20 * 节点的总数在 [1, 104] 之间 * 调用 find() 的总次数在 [1, 104] 之间 * 0 <= target <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
