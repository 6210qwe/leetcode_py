# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2779
标题: Number of Adjacent Elements With the Same Color
难度: medium
链接: https://leetcode.cn/problems/number-of-adjacent-elements-with-the-same-color/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2672. 有相同颜色的相邻元素数目 - 给定一个整数 n 表示一个长度为 n 的数组 colors，初始所有元素均为 0 ，表示是 未染色 的。同时给定一个二维整数数组 queries，其中 queries[i] = [indexi, colori]。对于第 i 个 查询： * 将 colors[indexi] 染色为 colori。 * 统计 colors 中颜色相同的相邻对的数量（无论 colori）。 请你返回一个长度与 queries 相等的数组 answer ，其中 answer[i]是前 i 个操作的答案。 示例 1： 输入：n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]] 输出：[0,1,1,0,2] 解释： * 一开始 colors = [0,0,0,0]，其中 0 表示数组中未染色的元素。 * 在第 1 次查询后 colors = [2,0,0,0]。颜色相同的相邻对的数量是 0。 * 在第 2 次查询后 colors = [2,2,0,0]。颜色相同的相邻对的数量是 1。 * 在第 3 次查询后 colors = [2,2,0,1]。颜色相同的相邻对的数量是 1。 * 在第 4 次查询后 colors = [2,1,0,1]。颜色相同的相邻对的数量是 0。 * 在第 5 次查询后 colors = [2,1,1,1]。颜色相同的相邻对的数量是 2。 示例 2： 输入：n = 1, queries = [[0,100000]] 输出：[0] 解释： 在第一次查询后 colors = [100000]。颜色相同的相邻对的数量是 0。 提示： * 1 <= n <= 105 * 1 <= queries.length <= 105 * queries[i].length == 2 * 0 <= indexi <= n - 1 * 1 <= colori <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个数组来记录当前的颜色状态，并在每次查询时更新相邻对的数量。

算法步骤:
1. 初始化一个长度为 n 的数组 colors，所有元素初始为 0。
2. 初始化一个变量 count 来记录颜色相同的相邻对的数量。
3. 遍历每个查询：
   - 如果当前索引的颜色与新的颜色不同，则更新相邻对的数量。
   - 更新 colors 数组中的颜色。
   - 将当前的 count 添加到结果列表中。

关键点:
- 通过维护一个 count 变量来高效地更新相邻对的数量。
- 仅在颜色变化时更新相邻对的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q)，其中 n 是数组的长度，q 是查询的数量。
空间复杂度: O(n)，用于存储 colors 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(n: int, queries: List[List[int]]) -> List[int]:
    """
    函数式接口 - 实现最优解法
    """
    colors = [0] * n
    count = 0
    result = []

    for index, color in queries:
        # 更新相邻对的数量
        if 0 <= index - 1 < n and colors[index] == colors[index - 1] and colors[index] != 0:
            count -= 1
        if 0 <= index + 1 < n and colors[index] == colors[index + 1] and colors[index] != 0:
            count -= 1

        # 更新颜色
        colors[index] = color

        # 再次更新相邻对的数量
        if 0 <= index - 1 < n and colors[index] == colors[index - 1]:
            count += 1
        if 0 <= index + 1 < n and colors[index] == colors[index + 1]:
            count += 1

        # 记录当前的 count
        result.append(count)

    return result


Solution = create_solution(solution_function_name)