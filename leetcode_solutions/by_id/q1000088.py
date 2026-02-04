# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000088
标题: 游乐园的迷宫
难度: hard
链接: https://leetcode.cn/problems/you-le-yuan-de-mi-gong/
题目类型: 贪心、几何、数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 15. 游乐园的迷宫 - 小王来到了游乐园，她玩的第一个项目是模拟推销员。有一个二维平面地图，其中散布着 N 个推销点，编号 0 到 N-1，不存在三点共线的情况。每两点之间有一条直线相连。游戏没有规定起点和终点，但限定了每次转角的方向。首先，小王需要先选择两个点分别作为起点和终点，然后从起点开始访问剩余 N-2 个点恰好一次并回到终点。访问的顺序需要满足一串给定的长度为 N-2 由 L 和 R 组成的字符串 direction，表示从起点出发之后在每个顶点上转角的方向。根据这个提示，小王希望你能够帮她找到一个可行的遍历顺序，输出顺序下标（若有多个方案，输出任意一种）。可以证明这样的遍历顺序一定是存在的。 Screenshot 2020-03-20 at 17.04.58.png [https://pic.leetcode.cn/595b60797d4a461287864a8cd05bba1d3b8760104ff83f43b902fd68477be9c3-Screenshot%202020-03-20%20at%2017.04.58.png] （上图：A->B->C 右转； 下图：D->E->F 左转） 示例 1： > 输入：points = [[1,1],[1,4],[3,2],[2,1]], direction = "LL" > > 输出：[0,2,1,3] > > 解释：[0,2,1,3] 是符合"LL"的方案之一。在 [0,2,1,3] 方案中，0->2->1 是左转方向， 2->1->3 也是左转方向 图片.gif [https://pic.leetcode.cn/c01c1efc423b916267c2a3a170266c925c368d62afa047c267cc1020970e55d9-%E5%9B%BE%E7%89%87.gif] 示例 2： > 输入：points = [[1,3],[2,4],[3,3],[2,1]], direction = "LR" > > 输出：[0,3,1,2] > > 解释：[0,3,1,2] 是符合"LR"的方案之一。在 [0,3,1,2] 方案中，0->3->1 是左转方向， 3->1->2 是右转方向 限制： * 3 <= points.length <= 1000 且 points[i].length == 2 * 1 <= points[i][0],points[i][1] <= 10000 * direction.length == points.length - 2 * direction 只包含 "L","R"
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，从任意起点开始，根据方向选择下一个点，确保每次选择的点满足方向要求。

算法步骤:
1. 选择一个起点和终点。
2. 从起点开始，根据方向选择下一个点。
3. 重复步骤2，直到所有点都被访问过。
4. 返回访问顺序。

关键点:
- 使用叉积判断转向方向。
- 通过维护一个已访问点的集合来避免重复访问。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N^2)，其中N是points的长度。每次选择下一个点时，需要遍历所有未访问的点。
空间复杂度: O(N)，用于存储已访问点的集合和结果路径。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def cross_product(p1, p2, p3):
    """计算向量 p1p2 和 p1p3 的叉积"""
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def solution_function_name(points: List[List[int]], direction: str) -> List[int]:
    n = len(points)
    visited = set()
    path = []

    def dfs(current, prev, index):
        if len(visited) == n:
            return True
        for i in range(n):
            if i not in visited:
                if index < len(direction):
                    if direction[index] == 'L' and cross_product(points[current], points[prev], points[i]) > 0:
                        visited.add(i)
                        path.append(i)
                        if dfs(i, current, index + 1):
                            return True
                        path.pop()
                        visited.remove(i)
                    elif direction[index] == 'R' and cross_product(points[current], points[prev], points[i]) < 0:
                        visited.add(i)
                        path.append(i)
                        if dfs(i, current, index + 1):
                            return True
                        path.pop()
                        visited.remove(i)
                else:
                    visited.add(i)
                    path.append(i)
                    if dfs(i, current, index + 1):
                        return True
                    path.pop()
                    visited.remove(i)
        return False

    for start in range(n):
        for end in range(n):
            if start != end:
                visited = {start}
                path = [start]
                if dfs(end, start, 0):
                    path.append(end)
                    return path

    return []


Solution = create_solution(solution_function_name)