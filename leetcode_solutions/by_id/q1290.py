# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1290
标题: Make Array Strictly Increasing
难度: hard
链接: https://leetcode.cn/problems/make-array-strictly-increasing/
题目类型: 数组、二分查找、动态规划、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1187. 使数组严格递增 - 给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。 每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。 如果无法让 arr1 严格递增，请返回 -1。 示例 1： 输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4] 输出：1 解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。 示例 2： 输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1] 输出：2 解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。 示例 3： 输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3] 输出：-1 解释：无法使 arr1 严格递增。 提示： * 1 <= arr1.length, arr2.length <= 2000 * 0 <= arr1[i], arr2[i] <= 10^9
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和二分查找来解决这个问题。

算法步骤:
1. 对 arr2 进行排序。
2. 定义一个二维 DP 数组 dp，其中 dp[i][j] 表示将 arr1 的前 i 个元素变为严格递增所需的最小操作次数，并且最后一个元素是 arr2[j]。
3. 初始化 dp 数组。
4. 遍历 arr1，对于每个元素，使用二分查找找到 arr2 中第一个大于当前元素的值。
5. 更新 dp 数组。
6. 最后，返回 dp 数组中的最小值，如果最小值为无穷大，则返回 -1。

关键点:
- 使用二分查找来优化查找过程。
- 动态规划的状态转移方程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m * log m)，其中 n 是 arr1 的长度，m 是 arr2 的长度。
空间复杂度: O(n * m)，用于存储 DP 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import bisect

def make_array_strictly_increasing(arr1: List[int], arr2: List[int]) -> int:
    """
    函数式接口 - 使数组严格递增
    """
    arr2 = sorted(set(arr2))  # 去重并排序
    n, m = len(arr1), len(arr2)
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # 初始状态

    for i in range(1, n + 1):
        for j in range(m + 1):
            if j > 0:
                prev_val = arr2[j - 1]
                if i == 1 or (i > 1 and (dp[i - 1][j - 1] != float('inf') and prev_val > arr1[i - 2])):
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
            if i == 1 or (i > 1 and (dp[i - 1][0] != float('inf') and arr1[i - 1] > arr1[i - 2])):
                dp[i][0] = min(dp[i][0], dp[i - 1][0])

    result = min(dp[n])
    return result if result != float('inf') else -1

Solution = create_solution(make_array_strictly_increasing)