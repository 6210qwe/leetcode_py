# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3483
标题: Alternating Groups II
难度: medium
链接: https://leetcode.cn/problems/alternating-groups-ii/
题目类型: 数组、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3208. 交替组 II - 给你一个整数数组 colors 和一个整数 k ，colors表示一个由红色和蓝色瓷砖组成的环，第 i 块瓷砖的颜色为 colors[i] ： * colors[i] == 0 表示第 i 块瓷砖的颜色是 红色 。 * colors[i] == 1 表示第 i 块瓷砖的颜色是 蓝色 。 环中连续 k 块瓷砖的颜色如果是 交替 颜色（也就是说除了第一块和最后一块瓷砖以外，中间瓷砖的颜色与它 左边 和 右边 的颜色都不同），那么它被称为一个 交替 组。 请你返回 交替 组的数目。 注意 ，由于 colors 表示一个 环 ，第一块 瓷砖和 最后一块 瓷砖是相邻的。 示例 1： 输入：colors = [0,1,0,1,0], k = 3 输出：3 解释： [https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183519.png] 交替组包括： [https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-182448.png][https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-182844.png][https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-183057.png] 示例 2： 输入：colors = [0,1,0,0,1,0,1], k = 6 输出：2 解释： [https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183907.png] 交替组包括： [https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184128.png][https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184240.png] 示例 3： 输入：colors = [1,1,0,1], k = 4 输出：0 解释： [https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184516.png] 提示： * 3 <= colors.length <= 105 * 0 <= colors[i] <= 1 * 3 <= k <= colors.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来检查每个长度为 k 的子数组是否满足交替条件，并处理环形数组。

算法步骤:
1. 将数组扩展为两倍长度以处理环形数组。
2. 使用滑动窗口遍历扩展后的数组，检查每个长度为 k 的子数组是否满足交替条件。
3. 计算满足条件的子数组数量。

关键点:
- 扩展数组以处理环形数组。
- 使用滑动窗口高效地检查每个子数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def count_alternating_groups(colors: List[int], k: int) -> int:
    n = len(colors)
    extended_colors = colors + colors  # 扩展数组以处理环形数组
    count = 0
    
    for i in range(n):
        is_alternating = True
        for j in range(k - 1):
            if extended_colors[i + j] == extended_colors[i + j + 1]:
                is_alternating = False
                break
        if is_alternating:
            count += 1
    
    return count

Solution = create_solution(count_alternating_groups)