# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1692
标题: Number of Ways to Reorder Array to Get Same BST
难度: hard
链接: https://leetcode.cn/problems/number-of-ways-to-reorder-array-to-get-same-bst/
题目类型: 树、并查集、二叉搜索树、记忆化搜索、数组、数学、分治、动态规划、二叉树、组合数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1569. 将子数组重新排序得到同一个二叉搜索树的方案数 - 给你一个数组 nums 表示 1 到 n 的一个排列。我们按照元素在 nums 中的顺序依次插入一个初始为空的二叉搜索树（BST）。请你统计将 nums 重新排序后，统计满足如下条件的方案数：重排后得到的二叉搜索树与 nums 原本数字顺序得到的二叉搜索树相同。 比方说，给你 nums = [2,1,3]，我们得到一棵 2 为根，1 为左孩子，3 为右孩子的树。数组 [2,3,1] 也能得到相同的 BST，但 [3,2,1] 会得到一棵不同的 BST 。 请你返回重排 nums 后，与原数组 nums 得到相同二叉搜索树的方案数。 由于答案可能会很大，请将结果对 10^9 + 7 取余数。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/30/bb.png] 输入：nums = [2,1,3] 输出：1 解释：我们将 nums 重排， [2,3,1] 能得到相同的 BST 。没有其他得到相同 BST 的方案了。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/30/ex1.png] 输入：nums = [3,4,5,1,2] 输出：5 解释：下面 5 个数组会得到相同的 BST： [3,1,2,4,5] [3,1,4,2,5] [3,1,4,5,2] [3,4,1,2,5] [3,4,1,5,2] 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/30/ex4.png] 输入：nums = [1,2,3] 输出：0 解释：没有别的排列顺序能得到相同的 BST 。 提示： * 1 <= nums.length <= 1000 * 1 <= nums[i] <= nums.length * nums 中所有数 互不相同 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归和组合数学来计算满足条件的排列数。

算法步骤:
1. 定义一个递归函数 `count_ways` 来计算以某个节点为根的子树的排列数。
2. 在递归函数中，首先将当前节点的左右子树分别递归计算排列数。
3. 计算左右子树的排列数之和，使用组合数学公式 C(n, k) 来计算总的排列数。
4. 返回总排列数，并对结果取模 1e9+7。

关键点:
- 使用组合数学公式 C(n, k) 来计算排列数。
- 递归地处理每个节点的左右子树。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是 nums 的长度。递归调用的时间复杂度是 O(n)，每次递归调用中需要计算组合数，最坏情况下需要 O(n) 时间。
空间复杂度: O(n)，递归调用栈的深度最多为 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import math

MOD = 10**9 + 7

def count_ways(nums: List[int]) -> int:
    if len(nums) < 3:
        return 1
    
    root = nums[0]
    left = [x for x in nums if x < root]
    right = [x for x in nums if x > root]
    
    left_ways = count_ways(left)
    right_ways = count_ways(right)
    
    total_ways = (left_ways * right_ways * math.comb(len(nums) - 1, len(left))) % MOD
    return total_ways

def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 计算将 nums 重新排序后，与原数组 nums 得到相同二叉搜索树的方案数。
    """
    if not nums:
        return 0
    return (count_ways(nums) - 1) % MOD

Solution = create_solution(solution_function_name)