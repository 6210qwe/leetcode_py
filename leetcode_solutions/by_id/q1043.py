# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1043
标题: Grid Illumination
难度: hard
链接: https://leetcode.cn/problems/grid-illumination/
题目类型: 数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1001. 网格照明 - 在大小为 n x n 的网格 grid 上，每个单元格都有一盏灯，最初灯都处于 关闭 状态。 给你一个由灯的位置组成的二维数组 lamps ，其中 lamps[i] = [rowi, coli] 表示 打开 位于 grid[rowi][coli] 的灯。即便同一盏灯可能在 lamps 中多次列出，不会影响这盏灯处于 打开 状态。 当一盏灯处于打开状态，它将会照亮 自身所在单元格 以及同一 行 、同一 列 和两条 对角线 上的 所有其他单元格 。 另给你一个二维数组 queries ，其中 queries[j] = [rowj, colj] 。对于第 j 个查询，如果单元格 [rowj, colj] 是被照亮的，则查询结果为 1 ，否则为 0 。在第 j 次查询之后 [按照查询的顺序] ，关闭 位于单元格 grid[rowj][colj] 上及相邻 8 个方向上（与单元格 grid[rowi][coli] 共享角或边）的任何灯。 返回一个整数数组 ans 作为答案， ans[j] 应等于第 j 次查询 queries[j] 的结果，1 表示照亮，0 表示未照亮。 示例 1： [https://assets.leetcode.com/uploads/2020/08/19/illu_1.jpg] 输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]] 输出：[1,0] 解释：最初所有灯都是关闭的。在执行查询之前，打开位于 [0, 0] 和 [4, 4] 的灯。第 0 次查询检查 grid[1][1] 是否被照亮（蓝色方框）。该单元格被照亮，所以 ans[0] = 1 。然后，关闭红色方框中的所有灯。 [https://assets.leetcode.com/uploads/2020/08/19/illu_step1.jpg] 第 1 次查询检查 grid[1][0] 是否被照亮（蓝色方框）。该单元格没有被照亮，所以 ans[1] = 0 。然后，关闭红色矩形中的所有灯。 [https://assets.leetcode.com/uploads/2020/08/19/illu_step2.jpg] 示例 2： 输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]] 输出：[1,1] 示例 3： 输入：n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]] 输出：[1,1,0] 提示： * 1 <= n <= 109 * 0 <= lamps.length <= 20000 * 0 <= queries.length <= 20000 * lamps[i].length == 2 * 0 <= rowi, coli < n * queries[j].length == 2 * 0 <= rowj, colj < n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表来记录每一行、每一列和对角线上的灯的数量，以便快速判断某个单元格是否被照亮。

算法步骤:
1. 初始化四个哈希表分别记录每一行、每一列、主对角线和副对角线上的灯的数量。
2. 遍历 `lamps` 数组，将每盏灯的位置记录到对应的哈希表中。
3. 对于每个查询，检查目标单元格所在的行、列、主对角线和副对角线是否有灯，如果有则返回 1，否则返回 0。
4. 查询后，关闭目标单元格及其相邻 8 个方向上的灯，并更新哈希表。

关键点:
- 使用哈希表来高效地记录和查询灯的状态。
- 通过计算主对角线和副对角线的索引来避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(L + Q)，其中 L 是 `lamps` 的长度，Q 是 `queries` 的长度。
空间复杂度: O(L)，用于存储哈希表中的灯的位置。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def gridIllumination(n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
    # 哈希表记录每一行、每一列、主对角线和副对角线上的灯的数量
    row, col, diag, anti_diag = {}, {}, {}, {}
    
    # 记录灯的位置
    for r, c in lamps:
        if (r, c) not in row:
            row[r] = 0
        if (r, c) not in col:
            col[c] = 0
        if (r, c) not in diag:
            diag[r - c] = 0
        if (r, c) not in anti_diag:
            anti_diag[r + c] = 0
        row[r] += 1
        col[c] += 1
        diag[r - c] += 1
        anti_diag[r + c] += 1
    
    # 查询并处理结果
    result = []
    for r, c in queries:
        if row.get(r, 0) > 0 or col.get(c, 0) > 0 or diag.get(r - c, 0) > 0 or anti_diag.get(r + c, 0) > 0:
            result.append(1)
        else:
            result.append(0)
        
        # 关闭目标单元格及其相邻 8 个方向上的灯
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) in row:
                    row[nr] -= 1
                    if row[nr] == 0:
                        del row[nr]
                    col[nc] -= 1
                    if col[nc] == 0:
                        del col[nc]
                    diag[nr - nc] -= 1
                    if diag[nr - nc] == 0:
                        del diag[nr - nc]
                    anti_diag[nr + nc] -= 1
                    if anti_diag[nr + nc] == 0:
                        del anti_diag[nr + nc]
    
    return result

Solution = create_solution(gridIllumination)