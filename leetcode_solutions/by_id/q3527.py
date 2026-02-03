# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3527
标题: Alternating Groups III
难度: hard
链接: https://leetcode.cn/problems/alternating-groups-iii/
题目类型: 树状数组、数组、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3245. 交替组 III - 给你一个整数数组 colors 和一个二维整数数组 queries 。colors表示一个由红色和蓝色瓷砖组成的环，第 i 块瓷砖的颜色为 colors[i] ： * colors[i] == 0 表示第 i 块瓷砖的颜色是 红色 。 * colors[i] == 1 表示第 i 块瓷砖的颜色是 蓝色 。 环中连续若干块瓷砖的颜色如果是 交替 颜色（也就是说这组瓷砖中除了第一块和最后一块瓷砖以外，中间瓷砖的颜色与它 左边 和 右边 的颜色都不同），那么它被称为一个 交替组。 你需要处理两种类型的查询： * queries[i] = [1, sizei]，确定大小为sizei的 交替组 的数量。 * queries[i] = [2, indexi, colori]，将colors[indexi]更改为colori。 返回数组 answer，数组中按顺序包含第一种类型查询的结果。 注意 ，由于 colors 表示一个 环 ，第一块 瓷砖和 最后一块 瓷砖是相邻的。 示例 1： 输入：colors = [0,1,1,0,1], queries = [[2,1,0],[1,4]] 输出：[2] 解释： 第一次查询： 将 colors[1] 改为 0。 [https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-20-25.png] 第二次查询： 统计大小为 4 的交替组的数量： [https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-25-02-2.png][https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-24-12.png] 示例 2： 输入：colors = [0,0,1,0,1,1], queries = [[1,3],[2,3,0],[1,5]] 输出：[2,0] 解释： [https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-35-50.png] 第一次查询： 统计大小为 3 的交替组的数量。 [https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-37-13.png][https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-36-40.png] 第二次查询：colors不变。 第三次查询：不存在大小为 5 的交替组。 提示： * 4 <= colors.length <= 5 * 104 * 0 <= colors[i] <= 1 * 1 <= queries.length <= 5 * 104 * queries[i][0] == 1 或 queries[i][0] == 2 * 对于所有的i： * queries[i][0] == 1： queries[i].length == 2, 3 <= queries[i][1] <= colors.length - 1 * queries[i][0] == 2： queries[i].length == 3, 0 <= queries[i][1] <= colors.length - 1, 0 <= queries[i][2] <= 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
