# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2206
标题: Detonate the Maximum Bombs
难度: medium
链接: https://leetcode.cn/problems/detonate-the-maximum-bombs/
题目类型: 深度优先搜索、广度优先搜索、图、几何、数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2101. 引爆最多的炸弹 - 给你一个炸弹列表。一个炸弹的 爆炸范围 定义为以炸弹为圆心的一个圆。 炸弹用一个下标从 0 开始的二维整数数组 bombs 表示，其中 bombs[i] = [xi, yi, ri] 。xi 和 yi 表示第 i 个炸弹的 X 和 Y 坐标，ri 表示爆炸范围的 半径 。 你需要选择引爆 一个 炸弹。当这个炸弹被引爆时，所有 在它爆炸范围内的炸弹都会被引爆，这些炸弹会进一步将它们爆炸范围内的其他炸弹引爆。 给你数组 bombs ，请你返回在引爆 一个 炸弹的前提下，最多 能引爆的炸弹数目。 示例 1： [https://assets.leetcode.com/uploads/2021/11/06/desmos-eg-3.png] 输入：bombs = [[2,1,3],[6,1,4]] 输出：2 解释： 上图展示了 2 个炸弹的位置和爆炸范围。 如果我们引爆左边的炸弹，右边的炸弹不会被影响。 但如果我们引爆右边的炸弹，两个炸弹都会爆炸。 所以最多能引爆的炸弹数目是 max(1, 2) = 2 。 示例 2： [https://assets.leetcode.com/uploads/2021/11/06/desmos-eg-2.png] 输入：bombs = [[1,1,5],[10,10,5]] 输出：1 解释： 引爆任意一个炸弹都不会引爆另一个炸弹。所以最多能引爆的炸弹数目为 1 。 示例 3： [https://assets.leetcode.com/uploads/2021/11/07/desmos-eg1.png] 输入：bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]] 输出：5 解释： 最佳引爆炸弹为炸弹 0 ，因为： - 炸弹 0 引爆炸弹 1 和 2 。红色圆表示炸弹 0 的爆炸范围。 - 炸弹 2 引爆炸弹 3 。蓝色圆表示炸弹 2 的爆炸范围。 - 炸弹 3 引爆炸弹 4 。绿色圆表示炸弹 3 的爆炸范围。 所以总共有 5 个炸弹被引爆。 提示： * 1 <= bombs.length <= 100 * bombs[i].length == 3 * 1 <= xi, yi, ri <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来模拟每个炸弹的引爆过程，并记录每个炸弹能引爆的最大数量。

算法步骤:
1. 构建一个图，表示每个炸弹可以引爆哪些其他炸弹。
2. 对于每个炸弹，使用 BFS 来计算其能引爆的最大炸弹数量。
3. 返回最大值。

关键点:
- 使用欧几里得距离公式来判断一个炸弹是否在另一个炸弹的爆炸范围内。
- 使用 BFS 来遍历每个炸弹的引爆路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是炸弹的数量。构建图的时间复杂度为 O(n^2)，每个炸弹的 BFS 时间复杂度为 O(n)。
空间复杂度: O(n^2)，用于存储图和 BFS 过程中的队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import collections

def maximum_detonation(bombs: List[List[int]]) -> int:
    def can_detonate(bomb1, bomb2):
        x1, y1, r1 = bomb1
        x2, y2, r2 = bomb2
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return distance <= r1

    n = len(bombs)
    graph = collections.defaultdict(list)
    
    # 构建图
    for i in range(n):
        for j in range(n):
            if i != j and can_detonate(bombs[i], bombs[j]):
                graph[i].append(j)

    def bfs(start):
        queue = collections.deque([start])
        visited = set([start])
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return count

    max_detonated = 0
    for i in range(n):
        max_detonated = max(max_detonated, bfs(i))
    
    return max_detonated

Solution = create_solution(maximum_detonation)