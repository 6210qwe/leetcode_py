# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000439
标题: 信物传送
难度: medium
链接: https://leetcode.cn/problems/6UEx57/
题目类型: 广度优先搜索、图、数组、矩阵、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 56. 信物传送 - 欢迎各位勇者来到力扣城，本次试炼主题为「信物传送」。 本次试炼场地设有若干传送带，matrix[i][j] 表示第 i 行 j 列的传送带运作方向，"^","v","<",">" 这四种符号分别表示 上、下、左、右 四个方向。信物会随传送带的方向移动。勇者每一次施法操作，可临时变更一处传送带的方向，在物品经过后传送带恢复原方向。lcp (2).gif [https://pic.leetcode.cn/1649835246-vfupSL-lcp%20(2).gif] 通关信物初始位于坐标 start处，勇者需要将其移动到坐标 end 处，请返回勇者施法操作的最少次数。 注意： * start 和 end 的格式均为 [i,j] 示例 1： > 输入：matrix = [">>v","v^<","<><"], start = [0,1], end = [2,0] > > 输出：1 > > 解释： 如上图所示 当信物移动到 [1,1] 时，勇者施法一次将 [1,1] 的传送方向 ^ 从变更为 < 从而信物移动到 [1,0]，后续到达 end 位置 因此勇者最少需要施法操作 1 次 示例 2： > 输入：matrix = [">>v",">>v","^<<"], start = [0,0], end = [1,1] > > 输出：0 > > 解释：勇者无需施法，信物将自动传送至 end 位置 示例 3： > 输入：matrix = [">^^>","<^v>","^v^<"], start = [0,0], end = [1,3] > > 输出：3 提示： * matrix 中仅包含 '^'、'v'、'<'、'>' * 0 < matrix.length <= 100 * 0 < matrix[i].length <= 100 * 0 <= start[0],end[0] < matrix.length * 0 <= start[1],end[1] < matrix[i].length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: BFS+状态压缩，记录到达每个位置的最少施法次数

算法步骤:
1. 使用BFS，状态为(位置, 施法次数)
2. 按照传送带方向移动，如果方向不对则施法
3. 使用优先队列，优先处理施法次数少的

关键点:
- BFS+优先队列
- 时间复杂度O(n*m*4)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n*m*4) - n*m为矩阵大小
空间复杂度: O(n*m) - 存储状态
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def conveyor_belt(matrix: List[str], start: List[int], end: List[int]) -> int:
    """
    函数式接口 - 信物传送
    
    实现思路:
    BFS+优先队列，找到最少施法次数。
    
    Args:
        matrix: 传送带矩阵
        start: 起始位置
        end: 目标位置
        
    Returns:
        最少施法次数
        
    Example:
        >>> conveyor_belt([">>v","v^<","<><"], [0,1], [2,0])
        1
    """
    m, n = len(matrix), len(matrix[0])
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    
    # 优先队列：(施法次数, 行, 列)
    heap = [(0, start[0], start[1])]
    visited = {(start[0], start[1]): 0}
    
    while heap:
        cost, r, c = heapq.heappop(heap)
        
        if [r, c] == end:
            return cost
        
        if visited.get((r, c), float('inf')) < cost:
            continue
        
        # 按照当前传送带方向移动（不施法）
        dir_char = matrix[r][c]
        dr, dc = directions[dir_char]
        nr, nc = r + dr, c + dc
        if 0 <= nr < m and 0 <= nc < n:
            if cost < visited.get((nr, nc), float('inf')):
                visited[(nr, nc)] = cost
                heapq.heappush(heap, (cost, nr, nc))
        
        # 尝试施法改变方向
        for new_dir, (dr, dc) in directions.items():
            if new_dir == dir_char:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                new_cost = cost + 1
                if new_cost < visited.get((nr, nc), float('inf')):
                    visited[(nr, nc)] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))
    
    return -1


Solution = create_solution(conveyor_belt)
