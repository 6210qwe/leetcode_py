# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 378
标题: Kth Smallest Element in a Sorted Matrix
难度: medium
链接: https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/
题目类型: 数组、二分查找、矩阵、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
378. 有序矩阵中第 K 小的元素 - 给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。 请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。 你必须找到一个内存复杂度优于 O(n2) 的解决方案。 示例 1： 输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8 输出：13 解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13 示例 2： 输入：matrix = [[-5]], k = 1 输出：-5 提示： * n == matrix.length * n == matrix[i].length * 1 <= n <= 300 * -109 <= matrix[i][j] <= 109 * 题目数据 保证 matrix 中的所有行和列都按 非递减顺序 排列 * 1 <= k <= n2 进阶： * 你能否用一个恒定的内存(即 O(1) 内存复杂度)来解决这个问题? * 你能在 O(n) 的时间复杂度下解决这个问题吗?这个方法对于面试来说可能太超前了，但是你会发现阅读这篇文章（ this paper [http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf] ）很有趣。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 有序矩阵上的值域二分：在元素值范围上二分答案，通过按行线性扫描统计「≤ mid 的元素个数」来判断收缩区间

算法步骤:
1. 由于每行、每列均非递减，可知矩阵整体的最小值为 left = matrix[0][0]，最大值为 right = matrix[n-1][n-1]。
2. 在区间 [left, right] 上进行二分，mid = (left + right) // 2。
3. 对于每个 mid，利用矩阵有序性从左下角或右上角开始计数：
   - 从左下角 (i=n-1, j=0) 出发，若 matrix[i][j] ≤ mid，则该列 j 在 0..i 的所有元素均 ≤ mid，count += i+1，j++；
   - 否则 matrix[i][j] > mid，说明该元素所在行的当前及右侧都 > mid，i-- 向上移动。
4. 完成计数后：
   - 如果 count ≥ k，说明第 k 小元素不大于 mid，将 right 收缩为 mid；
   - 否则 left = mid + 1。
5. 最终 left 即为第 k 小的元素值。

关键点:
- 在矩阵上按「Z 字形」走法统计 ≤ mid 的元素个数，时间复杂度为 O(n)。 
- 二分的是值域而不是下标，不需要将矩阵展开或拷贝。
- 注意使用 64 位整型保存中间值，避免大值运算时溢出（Python 无此问题）。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 log V) - V 为元素值域大小，每次二分统计花费 O(n^2) 或优化为 O(n)（标准做法是 O(n)）。
空间复杂度: O(1) - 只使用常数级辅助变量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def kth_smallest_element_in_a_sorted_matrix(matrix: List[List[int]], k: int) -> int:
    """
    在行列均有序的矩阵中找到第 k 小的元素。

    采用值域二分 + 从左下角开始的线性计数。
    """
    n = len(matrix)
    left, right = matrix[0][0], matrix[-1][-1]

    def count_leq(x: int) -> int:
        """统计矩阵中 <= x 的元素个数。"""
        i, j = n - 1, 0
        cnt = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= x:
                cnt += i + 1
                j += 1
            else:
                i -= 1
        return cnt

    while left < right:
        mid = (left + right) // 2
        if count_leq(mid) >= k:
            right = mid
        else:
            left = mid + 1

    return left


# 自动生成Solution类（无需手动编写）
Solution = create_solution(kth_smallest_element_in_a_sorted_matrix)
