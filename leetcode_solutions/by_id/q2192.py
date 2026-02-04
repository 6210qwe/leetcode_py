# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2192
标题: Minimum Cost Homecoming of a Robot in a Grid
难度: medium
链接: https://leetcode.cn/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/
题目类型: 贪心、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2087. 网格图中机器人回家的最小代价 - 给你一个 m x n 的网格图，其中 (0, 0) 是最左上角的格子，(m - 1, n - 1) 是最右下角的格子。给你一个整数数组 startPos ，startPos = [startrow, startcol] 表示 初始 有一个 机器人 在格子 (startrow, startcol) 处。同时给你一个整数数组 homePos ，homePos = [homerow, homecol] 表示机器人的 家 在格子 (homerow, homecol) 处。 机器人需要回家。每一步它可以往四个方向移动：上，下，左，右，同时机器人不能移出边界。每一步移动都有一定代价。再给你两个下标从 0 开始的额整数数组：长度为 m 的数组 rowCosts 和长度为 n 的数组 colCosts 。 * 如果机器人往 上 或者往 下 移动到第 r 行 的格子，那么代价为 rowCosts[r] 。 * 如果机器人往 左 或者往 右 移动到第 c 列 的格子，那么代价为 colCosts[c] 。 请你返回机器人回家需要的 最小总代价 。 示例 1： [https://assets.leetcode.com/uploads/2021/10/11/eg-1.png] 输入：startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7] 输出：18 解释：一个最优路径为： 从 (1, 0) 开始 -> 往下走到 (2, 0) 。代价为 rowCosts[2] = 3 。 -> 往右走到 (2, 1) 。代价为 colCosts[1] = 2 。 -> 往右走到 (2, 2) 。代价为 colCosts[2] = 6 。 -> 往右走到 (2, 3) 。代价为 colCosts[3] = 7 。 总代价为 3 + 2 + 6 + 7 = 18 示例 2： 输入：startPos = [0, 0], homePos = [0, 0], rowCosts = [5], colCosts = [26] 输出：0 解释：机器人已经在家了，所以不需要移动。总代价为 0 。 提示： * m == rowCosts.length * n == colCosts.length * 1 <= m, n <= 105 * 0 <= rowCosts[r], colCosts[c] <= 104 * startPos.length == 2 * homePos.length == 2 * 0 <= startrow, homerow < m * 0 <= startcol, homecol < n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，分别计算行和列的移动代价。

算法步骤:
1. 计算行移动的代价。
2. 计算列移动的代价。
3. 返回总代价。

关键点:
- 分别处理行和列的移动，确保每次移动都选择最优路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m + n)，其中 m 和 n 分别是行数和列数。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def min_cost(start_pos: List[int], home_pos: List[int], row_costs: List[int], col_costs: List[int]) -> int:
    """
    计算机器人回家的最小代价。
    
    :param start_pos: 机器人起始位置 [start_row, start_col]
    :param home_pos: 机器人目标位置 [home_row, home_col]
    :param row_costs: 每行的移动代价
    :param col_costs: 每列的移动代价
    :return: 机器人回家的最小代价
    """
    start_row, start_col = start_pos
    home_row, home_col = home_pos
    
    # 计算行移动的代价
    if start_row < home_row:
        row_cost = sum(row_costs[start_row + 1:home_row + 1])
    else:
        row_cost = sum(row_costs[home_row:start_row])
    
    # 计算列移动的代价
    if start_col < home_col:
        col_cost = sum(col_costs[start_col + 1:home_col + 1])
    else:
        col_cost = sum(col_costs[home_col:start_col])
    
    return row_cost + col_cost

Solution = create_solution(min_cost)