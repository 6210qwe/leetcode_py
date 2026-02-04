# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2567
标题: Closest Nodes Queries in a Binary Search Tree
难度: medium
链接: https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/
题目类型: 树、深度优先搜索、二叉搜索树、数组、二分查找、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2476. 二叉搜索树最近节点查询 - 给你一个 二叉搜索树 的根节点 root ，和一个由正整数组成、长度为 n 的数组 queries 。 请你找出一个长度为 n 的 二维 答案数组 answer ，其中 answer[i] = [mini, maxi] ： * mini 是树中小于等于 queries[i] 的 最大值 。如果不存在这样的值，则使用 -1 代替。 * maxi 是树中大于等于 queries[i] 的 最小值 。如果不存在这样的值，则使用 -1 代替。 返回数组 answer 。 示例 1 ： [https://assets.leetcode.com/uploads/2022/09/28/bstreeedrawioo.png] 输入：root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16] 输出：[[2,2],[4,6],[15,-1]] 解释：按下面的描述找出并返回查询的答案： - 树中小于等于 2 的最大值是 2 ，且大于等于 2 的最小值也是 2 。所以第一个查询的答案是 [2,2] 。 - 树中小于等于 5 的最大值是 4 ，且大于等于 5 的最小值是 6 。所以第二个查询的答案是 [4,6] 。 - 树中小于等于 16 的最大值是 15 ，且大于等于 16 的最小值不存在。所以第三个查询的答案是 [15,-1] 。 示例 2 ： [https://assets.leetcode.com/uploads/2022/09/28/bstttreee.png] 输入：root = [4,null,9], queries = [3] 输出：[[-1,4]] 解释：树中不存在小于等于 3 的最大值，且大于等于 3 的最小值是 4 。所以查询的答案是 [-1,4] 。 提示： * 树中节点的数目在范围 [2, 105] 内 * 1 <= Node.val <= 106 * n == queries.length * 1 <= n <= 105 * 1 <= queries[i] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用中序遍历将二叉搜索树转换为有序数组，然后对每个查询使用二分查找找到最接近的节点。

算法步骤:
1. 中序遍历二叉搜索树，生成一个有序数组。
2. 对于每个查询，使用二分查找找到小于等于查询值的最大值和大于等于查询值的最小值。
3. 将结果存储在答案数组中并返回。

关键点:
- 二叉搜索树的中序遍历结果是一个有序数组。
- 二分查找可以在 O(log n) 时间内找到最接近的节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q log n)，其中 n 是树中节点的数量，q 是查询的数量。中序遍历的时间复杂度是 O(n)，每次查询的时间复杂度是 O(log n)。
空间复杂度: O(n)，用于存储中序遍历的结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def closest_nodes_queries(root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
    def inorder_traversal(node: Optional[TreeNode]):
        if not node:
            return
        inorder_traversal(node.left)
        values.append(node.val)
        inorder_traversal(node.right)

    def binary_search(target: int):
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid] == target:
                return mid, mid
            elif values[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return right, left

    values = []
    inorder_traversal(root)
    result = []

    for query in queries:
        min_index, max_index = binary_search(query)
        min_val = values[min_index] if min_index >= 0 and min_index < len(values) else -1
        max_val = values[max_index] if max_index >= 0 and max_index < len(values) else -1
        result.append([min_val, max_val])

    return result

Solution = create_solution(closest_nodes_queries)