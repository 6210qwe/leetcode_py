# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000216
标题: 乐团站位
难度: medium
链接: https://leetcode.cn/problems/SNJvJP/
题目类型: 数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 29. 乐团站位 - 某乐团的演出场地可视作 `num * num` 的二维矩阵 `grid`（左上角坐标为 `[0,0]`)，每个位置站有一位成员。乐团共有 `9` 种乐器，乐器编号为 `1~9`，每位成员持有 `1` 个乐器。 为保证声乐混合效果，成员站位规则为：自 `grid` 左上角开始顺时针螺旋形向内循环以 `1，2，...，9` 循环重复排列。例如当 num = `5` 时，站位如图所示 ![image.png](https://pic.leetcode.cn/1616125411-WOblWH-image.png) 请返回位于场地坐标 [`Xpos`,`Ypos`] 的成员所持乐器编号。 **示例 1：** >输入：`num = 3, Xpos = 0, Ypos = 2` > >输出：`3` > >解释： ![image.png](https://pic.leetcode.cn/1616125437-WUOwsu-image.png) **示例 2：** >输入：`num = 4, Xpos = 1, Ypos = 2` > >输出：`5` > >解释： ![image.png](https://pic.leetcode.cn/1616125453-IIDpxg-image.png) **提示：** - `1 <= num <= 10^9` - `0 <= Xpos, Ypos < num`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过计算目标位置在螺旋矩阵中的相对位置，确定其对应的乐器编号。

算法步骤:
1. 计算目标位置所在的层数。
2. 根据层数计算目标位置在当前层的相对位置。
3. 根据相对位置计算出最终的乐器编号。

关键点:
- 通过数学公式直接计算目标位置的乐器编号，避免了模拟整个螺旋矩阵的构建。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def orchestra_layout(num: int, xPos: int, yPos: int) -> int:
    """
    函数式接口 - 计算位于 (xPos, yPos) 位置的乐器编号
    """
    # 计算目标位置所在的层数
    layer = min(min(xPos, num - 1 - xPos), min(yPos, num - 1 - yPos))
    
    # 计算当前层的边长
    side_length = num - 2 * layer
    
    # 计算当前层的总元素数
    total_elements_in_layer = 4 * (side_length - 1)
    
    # 计算目标位置在当前层的相对位置
    if xPos == layer:
        position = yPos - layer
    elif yPos == num - 1 - layer:
        position = side_length - 1 + (xPos - layer)
    elif xPos == num - 1 - layer:
        position = 2 * (side_length - 1) + (num - 1 - layer - yPos)
    else:
        position = 3 * (side_length - 1) + (num - 1 - layer - xPos)
    
    # 计算最终的乐器编号
    instrument_number = (position + 1) % 9
    return 1 if instrument_number == 0 else instrument_number


Solution = create_solution(orchestra_layout)