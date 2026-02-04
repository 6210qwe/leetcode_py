# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3278
标题: Find the Number of Ways to Place People I
难度: medium
链接: https://leetcode.cn/problems/find-the-number-of-ways-to-place-people-i/
题目类型: 几何、数组、数学、枚举、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3025. 人员站位的方案数 I - 给你一个 n x 2 的二维数组 points ，它表示二维平面上的一些点坐标，其中 points[i] = [xi, yi] 。 计算点对 (A, B) 的数量，其中 * A 在 B 的左上角，并且 * 它们形成的长方形中（或直线上）没有其它点（包括边界），除了点 A 和点 B。 返回数量。 示例 1： 输入：points = [[1,1],[2,2],[3,3]] 输出：0 解释： [https://assets.leetcode.com/uploads/2024/01/04/example1alicebob.png] 没有办法选择 A 和 B，使得 A 在 B 的左上角。 示例 2： 输入：points = [[6,2],[4,4],[2,6]] 输出：2 解释： [https://assets.leetcode.com/uploads/2024/06/25/t2.jpg] * 左边的是点对 (points[1], points[0])，其中 points[1] 在 points[0] 的左上角，并且形成的长方形内部是空的。 * 中间的是点对 (points[2], points[1])，和左边的一样是合法的点对。 * 右边的是点对 (points[2], points[0])，其中 points[2] 在 points[0] 的左上角，但 points[1] 在长方形内部，所以不是一个合法的点对。 示例 3： 输入：points = [[3,1],[1,3],[1,1]] 输出：2 解释： [https://assets.leetcode.com/uploads/2024/06/25/t3.jpg] * 左边的是点对 (points[2], points[0])，其中 points[2] 在 points[0] 的左上角并且在它们形成的直线上没有其它点。注意两个点形成一条线的情况是合法的。 * 中间的是点对 (points[1], points[2])，和左边一样也是合法的点对。 * 右边的是点对 (points[1], points[0])，它不是合法的点对，因为 points[2] 在长方形的边上。 提示： * 2 <= n <= 50 * points[i].length == 2 * 0 <= points[i][0], points[i][1] <= 50 * points[i] 点对两两不同。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过排序和双指针方法来找到所有符合条件的点对。

算法步骤:
1. 将点按 x 坐标升序排序，如果 x 相同，则按 y 坐标降序排序。
2. 使用双指针遍历排序后的点，找到所有满足条件的点对。
3. 对于每个点，使用另一个指针从当前点向后查找，确保没有其他点在它们形成的长方形内。

关键点:
- 排序保证了 x 坐标的顺序，同时 y 坐标的降序排列可以方便地处理 y 坐标相同的情况。
- 双指针方法有效地减少了不必要的比较。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_valid_pairs(points: List[List[int]]) -> int:
    """
    计算满足条件的点对数量
    """
    # 按 x 坐标升序排序，如果 x 相同，则按 y 坐标降序排序
    points.sort(key=lambda p: (p[0], -p[1]))
    
    count = 0
    n = len(points)
    
    for i in range(n):
        max_y = -1
        for j in range(i + 1, n):
            if points[j][1] > max_y and points[j][1] < points[i][1]:
                count += 1
                max_y = points[j][1]
    
    return count


Solution = create_solution(count_valid_pairs)