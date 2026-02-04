# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1487
标题: Cinema Seat Allocation
难度: medium
链接: https://leetcode.cn/problems/cinema-seat-allocation/
题目类型: 贪心、位运算、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1386. 安排电影院座位 - [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/21/cinema_seats_1.png] 如上图所示，电影院的观影厅中有 n 行座位，行编号从 1 到 n ，且每一行内总共有 10 个座位，列编号从 1 到 10 。 给你数组 reservedSeats ，包含所有已经被预约了的座位。比如说，reservedSeats[i]=[3,8] ，它表示第 3 行第 8 个座位被预约了。 请你返回 最多能安排多少个 4 人家庭 。4 人家庭要占据 同一行内连续 的 4 个座位。隔着过道的座位（比方说 [3,3] 和 [3,4]）不是连续的座位，但是如果你可以将 4 人家庭拆成过道两边各坐 2 人，这样子是允许的。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/21/cinema_seats_3.png] 输入：n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]] 输出：4 解释：上图所示是最优的安排方案，总共可以安排 4 个家庭。蓝色的叉表示被预约的座位，橙色的连续座位表示一个 4 人家庭。 示例 2： 输入：n = 2, reservedSeats = [[2,1],[1,8],[2,6]] 输出：2 示例 3： 输入：n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]] 输出：4 提示： * 1 <= n <= 10^9 * 1 <= reservedSeats.length <= min(10*n, 10^4) * reservedSeats[i].length == 2 * 1 <= reservedSeats[i][0] <= n * 1 <= reservedSeats[i][1] <= 10 * 所有 reservedSeats[i] 都是互不相同的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用位运算来标记每行的座位状态，并根据这些状态来计算最多能安排多少个4人家庭。

算法步骤:
1. 初始化一个字典 `row_status` 来记录每行的座位状态，使用位运算来标记哪些座位被预定。
2. 遍历 `reservedSeats`，更新 `row_status` 中对应行的座位状态。
3. 对于每行，检查是否有足够的连续座位来安排4人家庭。根据位运算的结果，判断该行可以安排的家庭数量。
4. 计算总的可以安排的家庭数量。

关键点:
- 使用位运算来高效地表示和处理每行的座位状态。
- 通过预定义的掩码来快速判断每行的可用座位组合。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m)，其中 m 是 `reservedSeats` 的长度。
空间复杂度: O(min(n, m))，因为 `row_status` 字典的大小取决于 `reservedSeats` 的长度或行数 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_number_of_families(n: int, reservedSeats: List[List[int]]) -> int:
    """
    函数式接口 - 计算最多能安排多少个4人家庭
    """
    # 位掩码表示每个可能的4人家庭座位组合
    left_mask = 0b1111000000
    right_mask = 0b0000011110
    middle_mask = 0b0011110000
    full_mask = 0b1111111110
    
    # 初始化每行的座位状态
    row_status = {}
    
    # 更新每行的座位状态
    for row, seat in reservedSeats:
        if row not in row_status:
            row_status[row] = full_mask
        row_status[row] &= ~(1 << (seat - 1))
    
    # 计算可以安排的家庭数量
    families = 0
    for row in range(1, n + 1):
        if row in row_status:
            row_mask = row_status[row]
            if row_mask & left_mask == left_mask and row_mask & right_mask == right_mask:
                families += 2
            elif row_mask & left_mask == left_mask or row_mask & right_mask == right_mask or row_mask & middle_mask == middle_mask:
                families += 1
        else:
            families += 2
    
    return families


Solution = create_solution(max_number_of_families)