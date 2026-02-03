# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1257
标题: Rank Transform of a Matrix
难度: hard
链接: https://leetcode.cn/problems/rank-transform-of-a-matrix/
题目类型: 并查集、图、拓扑排序、数组、矩阵、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1632. 矩阵转换后的排名 - 给你一个 m x n 的矩阵 matrix ，请你返回一个新的矩阵 answer ，其中 answer[row][col] 是 matrix[row][col] 的排名。 每个元素的 排名 是一个整数，表示这个元素相对于其他元素的大小关系，它按照如下规则计算： * 排名是从 1 开始的一个整数。 * 如果两个元素 p 和 q 在 同一行 或者 同一列 ，那么： * 如果 p < q ，那么 rank(p) < rank(q) * 如果 p == q ，那么 rank(p) == rank(q) * 如果 p > q ，那么 rank(p) > rank(q) * 排名 需要越 小 越好。 题目保证按照上面规则 answer 数组是唯一的。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/10/25/rank1.jpg] 输入：matrix = [[1,2],[3,4]] 输出：[[1,2],[2,3]] 解释： matrix[0][0] 的排名为 1 ，因为它是所在行和列的最小整数。 matrix[0][1] 的排名为 2 ，因为 matrix[0][1] > matrix[0][0] 且 matrix[0][0] 的排名为 1 。 matrix[1][0] 的排名为 2 ，因为 matrix[1][0] > matrix[0][0] 且 matrix[0][0] 的排名为 1 。 matrix[1][1] 的排名为 3 ，因为 matrix[1][1] > matrix[0][1]， matrix[1][1] > matrix[1][0] 且 matrix[0][1] 和 matrix[1][0] 的排名都为 2 。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/10/25/rank2.jpg] 输入：matrix = [[7,7],[7,7]] 输出：[[1,1],[1,1]] 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/10/25/rank3.jpg] 输入：matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]] 输出：[[4,2,3],[1,3,4],[5,1,6],[1,3,4]] 提示： * m == matrix.length * n == matrix[i].length * 1 <= m, n <= 500 * -109 <= matrix[row][col] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
