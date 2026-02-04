# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 787
标题: Sliding Puzzle
难度: hard
链接: https://leetcode.cn/problems/sliding-puzzle/
题目类型: 广度优先搜索、记忆化搜索、数组、动态规划、回溯、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
773. 滑动谜题 - 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示。一次 移动 定义为选择 0 与一个相邻的数字（上下左右）进行交换. 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。 给出一个谜板的初始状态 board ，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。 示例 1： [https://assets.leetcode.com/uploads/2021/06/29/slide1-grid.jpg] 输入：board = [[1,2,3],[4,0,5]] 输出：1 解释：交换 0 和 5 ，1 步完成 示例 2: [https://assets.leetcode.com/uploads/2021/06/29/slide2-grid.jpg] 输入：board = [[1,2,3],[5,4,0]] 输出：-1 解释：没有办法完成谜板 示例 3: [https://assets.leetcode.com/uploads/2021/06/29/slide3-grid.jpg] 输入：board = [[4,1,2],[5,0,3]] 输出：5 解释： 最少完成谜板的最少移动次数是 5 ， 一种移动路径: 尚未移动: [[4,1,2],[5,0,3]] 移动 1 次: [[4,1,2],[0,5,3]] 移动 2 次: [[0,1,2],[4,5,3]] 移动 3 次: [[1,0,2],[4,5,3]] 移动 4 次: [[1,2,0],[4,5,3]] 移动 5 次: [[1,2,3],[4,5,0]] 提示： * board.length == 2 * board[i].length == 3 * 0 <= board[i][j] <= 5 * board[i][j] 中每个值都 不同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从初始状态到目标状态的最短路径。

算法步骤:
1. 将初始状态转换为字符串形式，并将其加入队列。
2. 使用集合记录已访问的状态，避免重复访问。
3. 对于队列中的每个状态，尝试所有可能的移动（上下左右），生成新的状态。
4. 如果新状态为目标状态，返回当前步数。
5. 如果新状态未被访问过，将其加入队列和已访问集合。
6. 如果队列为空且未找到目标状态，返回 -1。

关键点:
- 使用字符串表示状态，方便比较和存储。
- 使用集合记录已访问状态，避免重复计算。
- 使用队列进行层次遍历，确保找到的路径是最短的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 状态总数固定为 6! = 720 种。
空间复杂度: O(1) - 使用的额外空间与状态总数成正比。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def sliding_puzzle(board: List[List[int]]) -> int:
    """
    使用广度优先搜索（BFS）来找到从初始状态到目标状态的最短路径。
    """
    # 目标状态
    target = "123450"
    
    # 将初始状态转换为字符串
    start = "".join(str(num) for row in board for num in row)
    
    # 记录已访问状态
    visited = set([start])
    
    # 队列用于层次遍历
    queue = [(start, 0)]
    
    # 可能的移动方向
    moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4],
        4: [1, 3, 5],
        5: [2, 4]
    }
    
    while queue:
        state, steps = queue.pop(0)
        
        if state == target:
            return steps
        
        zero_index = state.index("0")
        
        for next_index in moves[zero_index]:
            next_state = list(state)
            next_state[zero_index], next_state[next_index] = next_state[next_index], next_state[zero_index]
            next_state = "".join(next_state)
            
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, steps + 1))
    
    return -1


Solution = create_solution(sliding_puzzle)