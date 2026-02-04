# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1968
标题: Maximum Building Height
难度: hard
链接: https://leetcode.cn/problems/maximum-building-height/
题目类型: 数组、数学、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1840. 最高建筑高度 - 在一座城市里，你需要建 n 栋新的建筑。这些新的建筑会从 1 到 n 编号排成一列。 这座城市对这些新建筑有一些规定： * 每栋建筑的高度必须是一个非负整数。 * 第一栋建筑的高度 必须 是 0 。 * 任意两栋相邻建筑的高度差 不能超过 1 。 除此以外，某些建筑还有额外的最高高度限制。这些限制会以二维整数数组 restrictions 的形式给出，其中 restrictions[i] = [idi, maxHeighti] ，表示建筑 idi 的高度 不能超过 maxHeighti 。 题目保证每栋建筑在 restrictions 中 至多出现一次 ，同时建筑 1 不会 出现在 restrictions 中。 请你返回 最高 建筑能达到的 最高高度 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/04/25/ic236-q4-ex1-1.png] 输入：n = 5, restrictions = [[2,1],[4,1]] 输出：2 解释：上图中的绿色区域为每栋建筑被允许的最高高度。 我们可以使建筑高度分别为 [0,1,2,1,2] ，最高建筑的高度为 2 。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/04/25/ic236-q4-ex2.png] 输入：n = 6, restrictions = [] 输出：5 解释：上图中的绿色区域为每栋建筑被允许的最高高度。 我们可以使建筑高度分别为 [0,1,2,3,4,5] ，最高建筑的高度为 5 。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/04/25/ic236-q4-ex3.png] 输入：n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]] 输出：5 解释：上图中的绿色区域为每栋建筑被允许的最高高度。 我们可以使建筑高度分别为 [0,1,2,3,3,4,4,5,4,3] ，最高建筑的高度为 5 。 提示： * 2 <= n <= 109 * 0 <= restrictions.length <= min(n - 1, 105) * 2 <= idi <= n * idi 是 唯一的 。 * 0 <= maxHeighti <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 对于每个限制条件，计算其左侧和右侧的最大可能高度。
2. 通过两次遍历限制条件，分别从左到右和从右到左更新每个限制条件的实际最大高度。
3. 计算所有限制条件之间的最大高度。

算法步骤:
1. 将限制条件按位置排序，并添加虚拟限制条件 (1, 0) 和 (n+1, n)。
2. 从左到右遍历限制条件，更新每个限制条件的实际最大高度。
3. 从右到左遍历限制条件，更新每个限制条件的实际最大高度。
4. 计算所有限制条件之间的最大高度。

关键点:
- 通过两次遍历确保每个限制条件的实际最大高度是正确的。
- 计算两个限制条件之间的最大高度时，需要考虑它们之间的距离和高度差。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m log m + m)，其中 m 是限制条件的数量。排序操作的时间复杂度是 O(m log m)，两次遍历的时间复杂度是 O(m)。
空间复杂度: O(m)，用于存储限制条件及其实际最大高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_building_height(n: int, restrictions: List[List[int]]) -> int:
    """
    计算最高建筑能达到的最高高度
    """
    # 添加虚拟限制条件 (1, 0) 和 (n+1, n)
    restrictions.append([1, 0])
    restrictions.append([n + 1, n])
    restrictions.sort()

    # 从左到右遍历限制条件，更新每个限制条件的实际最大高度
    for i in range(1, len(restrictions)):
        restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + restrictions[i][0] - restrictions[i - 1][0])

    # 从右到左遍历限制条件，更新每个限制条件的实际最大高度
    for i in range(len(restrictions) - 2, -1, -1):
        restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + restrictions[i + 1][0] - restrictions[i][0])

    # 计算所有限制条件之间的最大高度
    max_height = 0
    for i in range(1, len(restrictions)):
        prev_pos, prev_height = restrictions[i - 1]
        curr_pos, curr_height = restrictions[i]
        max_height = max(max_height, (curr_pos - prev_pos + prev_height + curr_height) // 2)

    return max_height


Solution = create_solution(max_building_height)