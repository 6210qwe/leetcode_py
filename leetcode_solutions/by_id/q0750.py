# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 750
标题: Contain Virus
难度: hard
链接: https://leetcode.cn/problems/contain-virus/
题目类型: 深度优先搜索、广度优先搜索、数组、矩阵、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
749. 隔离病毒 - 病毒扩散得很快，现在你的任务是尽可能地通过安装防火墙来隔离病毒。 假设世界由 m x n 的二维矩阵 isInfected 组成， isInfected[i][j] == 0 表示该区域未感染病毒，而 isInfected[i][j] == 1 表示该区域已感染病毒。可以在任意 2 个相邻单元之间的共享边界上安装一个防火墙（并且只有一个防火墙）。 每天晚上，病毒会从被感染区域向相邻未感染区域扩散，除非被防火墙隔离。现由于资源有限，每天你只能安装一系列防火墙来隔离其中一个被病毒感染的区域（一个区域或连续的一片区域），且该感染区域对未感染区域的威胁最大且 保证唯一 。 你需要努力使得最后有部分区域不被病毒感染，如果可以成功，那么返回需要使用的防火墙个数; 如果无法实现，则返回在世界被病毒全部感染时已安装的防火墙个数。 示例 1： [https://assets.leetcode.com/uploads/2021/06/01/virus11-grid.jpg] 输入: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]] 输出: 10 解释:一共有两块被病毒感染的区域。 在第一天，添加 5 墙隔离病毒区域的左侧。病毒传播后的状态是: [https://assets.leetcode.com/uploads/2021/06/01/virus12edited-grid.jpg] 第二天，在右侧添加 5 个墙来隔离病毒区域。此时病毒已经被完全控制住了。 [https://assets.leetcode.com/uploads/2021/06/01/virus13edited-grid.jpg] 示例 2： [https://assets.leetcode.com/uploads/2021/06/01/virus2-grid.jpg] 输入: isInfected = [[1,1,1],[1,0,1],[1,1,1]] 输出: 4 解释: 虽然只保存了一个小区域，但却有四面墙。 注意，防火墙只建立在两个不同区域的共享边界上。 示例 3: 输入: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]] 输出: 13 解释: 在隔离右边感染区域后，隔离左边病毒区域只需要 2 个防火墙。 提示: * m == isInfected.length * n == isInfected[i].length * 1 <= m, n <= 50 * isInfected[i][j] is either 0 or 1 * 在整个描述的过程中，总有一个相邻的病毒区域，它将在下一轮 严格地感染更多未受污染的方块
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来找到所有感染区域，并记录每个区域将要感染的未感染区域。选择威胁最大的区域进行隔离，并更新矩阵。

算法步骤:
1. 初始化变量，包括防火墙数量和标记矩阵。
2. 使用 DFS 找到所有感染区域，并记录每个区域将要感染的未感染区域。
3. 选择威胁最大的区域进行隔离，并更新矩阵。
4. 重复上述步骤直到没有新的感染区域。

关键点:
- 使用 DFS 找到所有感染区域。
- 记录每个区域将要感染的未感染区域。
- 选择威胁最大的区域进行隔离。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * (m + n))，其中 m 和 n 分别是矩阵的行数和列数。每次 DFS 的时间复杂度是 O(m * n)，最多进行 m * n 次 DFS。
空间复杂度: O(m * n)，用于存储标记矩阵和其他辅助数据结构。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def contain_virus(is_infected: List[List[int]]) -> int:
    def dfs(x: int, y: int, index: int):
        if x < 0 or x >= m or y < 0 or y >= n or is_infected[x][y] != 1:
            return
        is_infected[x][y] = -index
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if is_infected[nx][ny] == 0:
                    threat[index].add((nx, ny))
                    walls[index] += 1
                elif is_infected[nx][ny] == 1:
                    dfs(nx, ny, index)

    m, n = len(is_infected), len(is_infected[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    result = 0

    while True:
        regions = []
        threat = [set() for _ in range(m * n + 1)]
        walls = [0 for _ in range(m * n + 1)]
        index = 0

        for i in range(m):
            for j in range(n):
                if is_infected[i][j] == 1:
                    index += 1
                    regions.append(index)
                    dfs(i, j, index)

        if not regions:
            break

        max_threat_index = max(regions, key=lambda x: len(threat[x]))
        result += walls[max_threat_index]

        for i in range(m):
            for j in range(n):
                if is_infected[i][j] < 0:
                    if is_infected[i][j] == -max_threat_index:
                        is_infected[i][j] = 2  # Mark as contained
                    else:
                        is_infected[i][j] = 1  # Reset to infected

        for i in range(m):
            for j in range(n):
                if is_infected[i][j] == 0:
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < m and 0 <= ny < n and is_infected[nx][ny] == 1:
                            is_infected[i][j] = 1
                            break

    return result


Solution = create_solution(contain_virus)