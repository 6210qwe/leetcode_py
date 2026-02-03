# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 363
标题: Max Sum of Rectangle No Larger Than K
难度: hard
链接: https://leetcode.cn/problems/max-sum-of-rectangle-no-larger-than-k/
题目类型: 数组、二分查找、矩阵、有序集合、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
363. 矩形区域不超过 K 的最大数值和 - 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。 题目数据保证总会存在一个数值和不超过 k 的矩形区域。 示例 1： [https://assets.leetcode.com/uploads/2021/03/18/sum-grid.jpg] 输入：matrix = [[1,0,1],[0,-2,3]], k = 2 输出：2 解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。 示例 2： 输入：matrix = [[2,2,-1]], k = 3 输出：3 提示： * m == matrix.length * n == matrix[i].length * 1 <= m, n <= 100 * -100 <= matrix[i][j] <= 100 * -105 <= k <= 105 进阶：如果行数远大于列数，该如何设计解决方案？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 固定上下边界，将二维问题压缩成一维「子数组不超过 k 的最大和」，再用前缀和 + 有序集合在 O(n log n) 内求解

算法步骤:
1. 设矩阵大小为 m×n，枚举上边界 row\_top，从 row\_top 向下逐行扩展下边界 row\_bottom。
2. 对于每一对 (row\_top, row\_bottom)，用一个长度为 n 的数组 col\_sum 累加这两行之间每一列的元素之和，把该二维子矩阵转化为一维数组问题：在 col\_sum 中寻找不超过 k 的最大子数组和。
3. 对一维数组部分：
   - 维护前缀和 prefix，以及一个按升序存储的前缀和集合 S（如使用平衡二叉树或有序列表）。
   - 对于当前前缀和 prefix\_j，希望找到集合中最小的 prefix\_i 使得 prefix\_j - prefix\_i ≤ k，即 prefix\_i ≥ prefix\_j - k，可通过二分在 S 中查找。
   - 用 prefix\_j - prefix\_i 更新答案，同时将 prefix\_j 插入 S。
4. 枚举所有上、下边界组合并更新全局最优答案，若刚好达到 k 可以及早返回。

关键点:
- 固定较短的一维（行或列），若行远多于列，应先在代码中转置矩阵以减少外层枚举规模。
- 一维子问题的经典做法是「前缀和 + 有序集合 + 二分」，可复用为子函数。
- 注意处理包含负数的情况，不能使用简单的滑动窗口或 Kadane 算法。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(min(m, n)^2 * max(m, n) * log max(m, n)) - 通过在行列间选择较短的一维作为外层循环以优化复杂度。
空间复杂度: O(max(m, n)) - 需要一个列（或行）累加数组和一个有序前缀和集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from bisect import bisect_left, insort
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_sum_of_rectangle_no_larger_than_k(matrix: List[List[int]], k: int) -> int:
    """
    寻找矩阵中和不超过 k 的最大子矩形和。

    通过固定上下边界，将二维压缩成一维前缀和数组，
    再利用「前缀和 + 有序集合 + 二分」在 O(n log n) 内求子数组和上界为 k 的最大值。
    """
    if not matrix or not matrix[0]:
        return float("-inf")

    m, n = len(matrix), len(matrix[0])

    # 为减少外层循环复杂度，固定较短的一维
    if m > n:
        # 转置矩阵
        matrix = [list(row) for row in zip(*matrix)]
        m, n = n, m

    res = float("-inf")

    for top in range(m):
        col_sum = [0] * n
        for bottom in range(top, m):
            # 累加 top..bottom 行之间的每列和
            for c in range(n):
                col_sum[c] += matrix[bottom][c]

            # 在 col_sum 中寻找不超过 k 的最大子数组和
            prefix = 0
            prefix_sums = [0]  # 有序前缀和集合
            cur_best = float("-inf")
            for x in col_sum:
                prefix += x
                # 需要最小的 prev >= prefix - k
                target = prefix - k
                i = bisect_left(prefix_sums, target)
                if i < len(prefix_sums):
                    cur_best = max(cur_best, prefix - prefix_sums[i])
                # 将当前前缀和插入有序列表
                insort(prefix_sums, prefix)

            res = max(res, cur_best)
            if res == k:
                return res

    return res


# 自动生成Solution类（无需手动编写）
Solution = create_solution(max_sum_of_rectangle_no_larger_than_k)
