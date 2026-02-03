# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1663
标题: Detect Cycles in 2D Grid
难度: medium
链接: https://leetcode.cn/problems/detect-cycles-in-2d-grid/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1559. 二维网格图中探测环 - 给你一个二维字符网格数组 grid ，大小为 m x n ，你需要检查 grid 中是否存在 相同值 形成的环。 一个环是一条开始和结束于同一个格子的长度 大于等于 4 的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，可以移动的前提是这两个格子有 相同的值 。 同时，你也不能回到上一次移动时所在的格子。比方说，环 (1, 1) -> (1, 2) -> (1, 1) 是不合法的，因为从 (1, 2) 移动到 (1, 1) 回到了上一次移动时的格子。 如果 grid 中有相同值形成的环，请你返回 true ，否则返回 false 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/22/5482e1.png] 输入：grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]] 输出：true 解释：如下图所示，有 2 个用不同颜色标出来的环： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/22/5482e11.png] 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/22/5482e2.png] 输入：grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]] 输出：true 解释：如下图所示，只有高亮所示的一个合法环： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/22/5482e22.png] 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/22/5482e3.png] 输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]] 输出：false 提示： * m == grid.length * n == grid[i].length * 1 <= m <= 500 * 1 <= n <= 500 * grid 只包含小写英文字母。
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
