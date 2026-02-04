# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000567
标题: 提取咒文
难度: medium
链接: https://leetcode.cn/problems/kjpLFZ/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 79. 提取咒文 - 随着兽群逐渐远去，一座大升降机缓缓的从地下升到了远征队面前。借由这台升降机，他们将能够到达地底的永恒至森。 在升降机的操作台上，是一个由魔法符号组成的矩阵，为了便于辨识，我们用小写字母来表示。 `matrix[i][j]` 表示矩阵第 `i` 行 `j` 列的字母。该矩阵上有一个提取装置，可以对所在位置的字母提取。 提取装置初始位于矩阵的左上角 `[0,0]`，可以通过每次操作移动到上、下、左、右相邻的 1 格位置中。提取装置每次移动或每次提取均记为一次操作。 远征队需要按照顺序，从矩阵中逐一取出字母以组成 `mantra`，才能够成功的启动升降机。请返回他们 **最少** 需要消耗的操作次数。如果无法完成提取，返回 `-1`。 **注意：** - 提取装置可对同一位置的字母重复提取，每次提取一个 - 提取字母时，需按词语顺序依次提取 **示例 1：** >输入：`matrix = ["sd","ep"], mantra = "speed"` > >输出：`10` > >解释：如下图所示 ![矩阵 (2).gif](https://pic.leetcode.cn/1646288670-OTlvAl-%E7%9F%A9%E9%98%B5%20\(2\).gif) **示例 2：** >输入：`matrix = ["abc","daf","geg"]， mantra = "sad"` > >输出：`-1` > >解释：矩阵中不存在 `s` ，无法提取词语 **提示：** - `0 < matrix.length, matrix[i].length <= 100` - `0 < mantra.length <= 100` - `matrix 和 mantra` 仅由小写字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从起点到每个字符的最短路径，并使用动态规划（DP）来记录每个字符在当前步骤下的最小操作次数。

算法步骤:
1. 初始化一个二维数组 `dp`，其中 `dp[i][j]` 表示提取完 `mantra` 的前 `i` 个字符后，提取装置在位置 `(x, y)` 的最小操作次数。
2. 使用 BFS 来计算从起点到每个字符的最短路径。
3. 使用 DP 来更新每个字符在当前步骤下的最小操作次数。
4. 返回 `dp` 数组中的最小值，如果没有找到则返回 `-1`。

关键点:
- 使用 BFS 来计算从起点到每个字符的最短路径。
- 使用 DP 来记录每个字符在当前步骤下的最小操作次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * k)，其中 m 和 n 分别是矩阵的行数和列数，k 是 `mantra` 的长度。
空间复杂度: O(m * n * k)，用于存储 DP 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from collections import deque

def solution_function_name(matrix: List[str], mantra: str) -> int:
    """
    函数式接口 - 使用 BFS 和 DP 来找到从起点到每个字符的最短路径，并记录每个字符在当前步骤下的最小操作次数。
    """
    if not matrix or not matrix[0]:
        return -1

    m, n = len(matrix), len(matrix[0])
    k = len(mantra)
    
    # 初始化 DP 数组
    dp = [[[float('inf')] * n for _ in range(m)] for _ in range(k + 1)]
    dp[0][0][0] = 0
    
    # 定义方向数组
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    for i in range(1, k + 1):
        queue = deque([(0, 0)])
        visited = set()
        while queue:
            x, y = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if matrix[nx][ny] == mantra[i - 1]:
                        dp[i][nx][ny] = min(dp[i][nx][ny], dp[i - 1][x][y] + 1)
                    dp[i][nx][ny] = min(dp[i][nx][ny], dp[i][x][y] + 1)
                    queue.append((nx, ny))
    
    result = min([min(row) for row in dp[k]])
    return result if result != float('inf') else -1

Solution = create_solution(solution_function_name)