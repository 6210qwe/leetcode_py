# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2103
标题: Find All Groups of Farmland
难度: medium
链接: https://leetcode.cn/problems/find-all-groups-of-farmland/
题目类型: 深度优先搜索、广度优先搜索、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1992. 找到所有的农场组 - 给你一个下标从 0 开始，大小为 m x n 的二进制矩阵 land ，其中 0 表示一单位的森林土地，1 表示一单位的农场土地。 为了让农场保持有序，农场土地之间以矩形的 农场组 的形式存在。每一个农场组都 仅 包含农场土地。且题目保证不会有两个农场组相邻，也就是说一个农场组中的任何一块土地都 不会 与另一个农场组的任何一块土地在四个方向上相邻。 land 可以用坐标系统表示，其中 land 左上角坐标为 (0, 0) ，右下角坐标为 (m-1, n-1) 。请你找到所有 农场组 最左上角和最右下角的坐标。一个左上角坐标为 (r1, c1) 且右下角坐标为 (r2, c2) 的 农场组 用长度为 4 的数组 [r1, c1, r2, c2] 表示。 请你返回一个二维数组，它包含若干个长度为 4 的子数组，每个子数组表示 land 中的一个 农场组 。如果没有任何农场组，请你返回一个空数组。可以以 任意顺序 返回所有农场组。 示例 1： [https://assets.leetcode.com/uploads/2021/07/27/screenshot-2021-07-27-at-12-23-15-copy-of-diagram-drawio-diagrams-net.png] 输入：land = [[1,0,0],[0,1,1],[0,1,1]] 输出：[[0,0,0,0],[1,1,2,2]] 解释： 第一个农场组的左上角为 land[0][0] ，右下角为 land[0][0] 。 第二个农场组的左上角为 land[1][1] ，右下角为 land[2][2] 。 示例 2： [https://assets.leetcode.com/uploads/2021/07/27/screenshot-2021-07-27-at-12-30-26-copy-of-diagram-drawio-diagrams-net.png] 输入：land = [[1,1],[1,1]] 输出：[[0,0,1,1]] 解释： 第一个农场组左上角为 land[0][0] ，右下角为 land[1][1] 。 示例 3： [https://assets.leetcode.com/uploads/2021/07/27/screenshot-2021-07-27-at-12-32-24-copy-of-diagram-drawio-diagrams-net.png] 输入：land = [[0]] 输出：[] 解释： 没有任何农场组。 提示： * m == land.length * n == land[i].length * 1 <= m, n <= 300 * land 只包含 0 和 1 。 * 农场组都是 矩形 的形状。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来找到每个农场组，并记录其边界。

算法步骤:
1. 初始化一个结果列表 `result` 来存储所有农场组的边界。
2. 遍历整个矩阵 `land`，对于每个未访问过的农场土地（值为1），启动一次DFS。
3. 在DFS过程中，更新当前农场组的右下角边界。
4. 将找到的农场组边界添加到结果列表中。
5. 返回结果列表。

关键点:
- 使用DFS来遍历并标记已访问的土地。
- 通过记录每个农场组的右下角边界来确定其范围。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是矩阵的行数和列数。每个元素最多被访问一次。
空间复杂度: O(m * n)，在最坏情况下，递归栈的深度可能达到 m * n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def findFarmland(land: List[List[int]]) -> List[List[int]]:
    """
    找到所有的农场组
    """
    def dfs(r, c, max_r, max_c):
        if r < 0 or r >= len(land) or c < 0 or c >= len(land[0]) or land[r][c] != 1:
            return
        # 更新右下角边界
        max_r[0] = max(max_r[0], r)
        max_c[0] = max(max_c[0], c)
        # 标记为已访问
        land[r][c] = -1
        # 递归访问四个方向
        dfs(r + 1, c, max_r, max_c)
        dfs(r - 1, c, max_r, max_c)
        dfs(r, c + 1, max_r, max_c)
        dfs(r, c - 1, max_r, max_c)

    result = []
    for r in range(len(land)):
        for c in range(len(land[0])):
            if land[r][c] == 1:
                max_r, max_c = [r], [c]
                dfs(r, c, max_r, max_c)
                result.append([r, c, max_r[0], max_c[0]])
    
    return result

Solution = create_solution(findFarmland)