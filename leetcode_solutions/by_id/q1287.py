# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1287
标题: Distance Between Bus Stops
难度: easy
链接: https://leetcode.cn/problems/distance-between-bus-stops/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1184. 公交站间的距离 - 环形公交路线上有 n 个站，按次序从 0 到 n - 1 进行编号。我们已知每一对相邻公交站之间的距离，distance[i] 表示编号为 i 的车站和编号为 (i + 1) % n 的车站之间的距离。 环线上的公交车都可以按顺时针和逆时针的方向行驶。 返回乘客从出发点 start 到目的地 destination 之间的最短距离。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/09/08/untitled-diagram-1.jpg] 输入：distance = [1,2,3,4], start = 0, destination = 1 输出：1 解释：公交站 0 和 1 之间的距离是 1 或 9，最小值是 1。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/09/08/untitled-diagram-1-1.jpg] 输入：distance = [1,2,3,4], start = 0, destination = 2 输出：3 解释：公交站 0 和 2 之间的距离是 3 或 7，最小值是 3。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/09/08/untitled-diagram-1-2.jpg] 输入：distance = [1,2,3,4], start = 0, destination = 3 输出：4 解释：公交站 0 和 3 之间的距离是 6 或 4，最小值是 4。 提示： * 1 <= n <= 10^4 * distance.length == n * 0 <= start, destination < n * 0 <= distance[i] <= 10^4
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
