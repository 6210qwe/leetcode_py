# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3434
标题: Find the Number of Distinct Colors Among the Balls
难度: medium
链接: https://leetcode.cn/problems/find-the-number-of-distinct-colors-among-the-balls/
题目类型: 数组、哈希表、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3160. 所有球里面不同颜色的数目 - 给你一个整数 limit 和一个大小为 n x 2 的二维数组 queries 。 总共有 limit + 1 个球，每个球的编号为 [0, limit] 中一个 互不相同 的数字。一开始，所有球都没有颜色。queries 中每次操作的格式为 [x, y] ，你需要将球 x 染上颜色 y 。每次操作之后，你需要求出所有球颜色的数目。 请你返回一个长度为 n 的数组 result ，其中 result[i] 是第 i 次操作以后颜色的数目。 注意 ，没有染色的球不算作一种颜色。 示例 1： 输入：limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]] 输出：[1,2,2,3] 解释： [https://assets.leetcode.com/uploads/2024/04/17/ezgifcom-crop.gif] * 操作 0 后，球 1 颜色为 4 。 * 操作 1 后，球 1 颜色为 4 ，球 2 颜色为 5 。 * 操作 2 后，球 1 颜色为 3 ，球 2 颜色为 5 。 * 操作 3 后，球 1 颜色为 3 ，球 2 颜色为 5 ，球 3 颜色为 4 。 示例 2： 输入：limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]] 输出：[1,2,2,3,4] 解释： [https://assets.leetcode.com/uploads/2024/04/17/ezgifcom-crop2.gif] * 操作 0 后，球 0 颜色为 1 。 * 操作 1 后，球 0 颜色为 1 ，球 1 颜色为 2 。 * 操作 2 后，球 0 颜色为 1 ，球 1 和 2 颜色为 2 。 * 操作 3 后，球 0 颜色为 1 ，球 1 和 2 颜色为 2 ，球 3 颜色为 4 。 * 操作 4 后，球 0 颜色为 1 ，球 1 和 2 颜色为 2 ，球 3 颜色为 4 ，球 4 颜色为 5 。 提示： * 1 <= limit <= 109 * 1 <= n == queries.length <= 105 * queries[i].length == 2 * 0 <= queries[i][0] <= limit * 1 <= queries[i][1] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个球的颜色，并使用集合记录当前出现的颜色种类。

算法步骤:
1. 初始化一个哈希表 `ball_colors` 用于记录每个球的颜色。
2. 初始化一个集合 `distinct_colors` 用于记录当前出现的颜色种类。
3. 遍历 `queries`，对于每个查询：
   - 如果球已经染过色，从 `distinct_colors` 中移除旧颜色。
   - 更新 `ball_colors` 和 `distinct_colors`。
   - 记录当前 `distinct_colors` 的大小作为结果的一部分。

关键点:
- 使用哈希表和集合来高效地记录和更新颜色信息。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 queries 的长度。每个查询的操作都是 O(1) 的。
空间复杂度: O(n)，需要存储每个球的颜色和当前出现的颜色种类。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def distinct_colors_after_queries(limit: int, queries: List[List[int]]) -> List[int]:
    ball_colors = {}  # 记录每个球的颜色
    distinct_colors = set()  # 记录当前出现的颜色种类
    result = []  # 存储每次操作后的颜色数目
    
    for query in queries:
        ball, color = query
        if ball in ball_colors:
            old_color = ball_colors[ball]
            distinct_colors.discard(old_color)
        ball_colors[ball] = color
        distinct_colors.add(color)
        result.append(len(distinct_colors))
    
    return result

Solution = create_solution(distinct_colors_after_queries)