# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3463
标题: Alternating Groups I
难度: easy
链接: https://leetcode.cn/problems/alternating-groups-i/
题目类型: 数组、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3206. 交替组 I - 给你一个整数数组 colors ，它表示一个由红色和蓝色瓷砖组成的环，第 i 块瓷砖的颜色为 colors[i] ： * colors[i] == 0 表示第 i 块瓷砖的颜色是 红色 。 * colors[i] == 1 表示第 i 块瓷砖的颜色是 蓝色 。 环中连续 3 块瓷砖的颜色如果是 交替 颜色（也就是说中间瓷砖的颜色与它 左边 和 右边 的颜色都不同），那么它被称为一个 交替 组。 请你返回 交替 组的数目。 注意 ，由于 colors 表示一个 环 ，第一块 瓷砖和 最后一块 瓷砖是相邻的。 示例 1： 输入：colors = [1,1,1] 输出：0 解释： [https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-53-171.png] 示例 2： 输入：colors = [0,1,0,0,1] 输出：3 解释： [https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-47-491.png] 交替组包括： [https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-50-441.png][https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-48-211.png][https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-49-351.png] 提示： * 3 <= colors.length <= 100 * 0 <= colors[i] <= 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过遍历数组并检查每个长度为3的子数组是否满足交替条件来计算交替组的数量。

算法步骤:
1. 将数组扩展为原来的两倍，以便处理环形结构。
2. 遍历扩展后的数组，检查每个长度为3的子数组是否满足交替条件。
3. 如果满足条件，则计数器加一。

关键点:
- 扩展数组以处理环形结构。
- 检查每个长度为3的子数组是否满足交替条件。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 colors 的长度。我们只需要遍历一次扩展后的数组。
空间复杂度: O(n)，扩展后的数组需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_alternating_groups(colors: List[int]) -> int:
    """
    函数式接口 - 计算交替组的数量
    """
    # 扩展数组以处理环形结构
    extended_colors = colors + colors
    
    count = 0
    n = len(colors)
    
    for i in range(1, n + 1):
        if extended_colors[i] != extended_colors[i - 1] and extended_colors[i] != extended_colors[i + 1]:
            count += 1
    
    return count


Solution = create_solution(count_alternating_groups)