# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 668
标题: Kth Smallest Number in Multiplication Table
难度: hard
链接: https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/
题目类型: 数学、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
668. 乘法表中第k小的数 - 几乎每一个人都用 乘法表 [https://baike.baidu.com/item/%E4%B9%98%E6%B3%95%E8%A1%A8]。但是你能在乘法表中快速找到第 k 小的数字吗？ 乘法表是大小为 m x n 的一个整数矩阵，其中 mat[i][j] == i * j（下标从 1 开始）。 给你三个整数 m、n 和 k，请你在大小为 m x n 的乘法表中，找出并返回第 k 小的数字。 示例 1： [https://assets.leetcode.com/uploads/2021/05/02/multtable1-grid.jpg] 输入：m = 3, n = 3, k = 5 输出：3 解释：第 5 小的数字是 3 。 示例 2： [https://assets.leetcode.com/uploads/2021/05/02/multtable2-grid.jpg] 输入：m = 2, n = 3, k = 6 输出：6 解释：第 6 小的数字是 6 。 提示： * 1 <= m, n <= 3 * 104 * 1 <= k <= m * n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来确定第 k 小的数字。通过计算乘法表中小于等于 mid 的数字个数来进行判断。

算法步骤:
1. 初始化二分查找的左右边界 left 和 right。
2. 计算中间值 mid。
3. 计算乘法表中小于等于 mid 的数字个数 count。
4. 如果 count 小于 k，则说明第 k 小的数字在 mid 的右边，更新 left。
5. 否则，更新 right。
6. 最终返回 left 即为第 k 小的数字。

关键点:
- 使用二分查找来缩小搜索范围。
- 计算乘法表中小于等于 mid 的数字个数时，可以逐行计算每行中小于等于 mid 的数字个数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * log(m * n))
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_kth_number(m: int, n: int, k: int) -> int:
    """
    在大小为 m x n 的乘法表中，找出并返回第 k 小的数字。
    """
    def count_less_equal(mid: int) -> int:
        """计算乘法表中小于等于 mid 的数字个数。"""
        count = 0
        for i in range(1, m + 1):
            count += min(mid // i, n)
        return count

    left, right = 1, m * n
    while left < right:
        mid = (left + right) // 2
        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left


Solution = create_solution(find_kth_number)