# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3947
标题: Balanced K-Factor Decomposition
难度: medium
链接: https://leetcode.cn/problems/balanced-k-factor-decomposition/
题目类型: 数学、回溯、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3669. K 因数分解 - 给你两个整数 n 和 k，将数字 n 恰好分割成 k 个正整数，使得这些整数的 乘积 等于 n。 返回一个分割方案，使得这些数字中 最大值 和 最小值 之间的 差值 最小化。结果可以以 任意顺序 返回。 示例 1： 输入：n = 100, k = 2 输出：[10,10] 解释： 分割方案 [10, 10] 的结果是 10 * 10 = 100，且最大值与最小值的差值为 0，这是最小可能值。 示例 2： 输入：n = 44, k = 3 输出：[2,2,11] 解释： * 分割方案 [1, 1, 44] 的差值为 43 * 分割方案 [1, 2, 22] 的差值为 21 * 分割方案 [1, 4, 11] 的差值为 10 * 分割方案 [2, 2, 11] 的差值为 9 因此，[2, 2, 11] 是最优分割方案，其差值最小，为 9。 提示： * 4 <= n <= 105 * 2 <= k <= 5 * k 严格小于 n 的正因数的总数。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法找到所有可能的 k 个因子的组合，并选择其中差值最小的组合。

算法步骤:
1. 初始化结果列表和当前组合。
2. 使用回溯法生成所有可能的 k 个因子的组合。
3. 对每个组合计算最大值和最小值的差值，并更新最优解。
4. 返回最优解。

关键点:
- 使用回溯法生成所有可能的组合。
- 通过剪枝减少不必要的计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^(k-1)) - 在最坏情况下，需要遍历所有可能的 k 个因子的组合。
空间复杂度: O(k) - 递归调用栈的深度最多为 k。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(n: int, k: int) -> List[int]:
    """
    函数式接口 - 实现最优解法
    """
    def backtrack(start: int, path: List[int]):
        if len(path) == k:
            if path[0] * path[-1] == n // (path[0] * path[-1]) ** (k - 2):
                result.append(path[:])
            return
        for i in range(start, int(n ** (1 / (k - len(path)))) + 1):
            if n % (i * (path[0] * path[-1]) ** (k - len(path) - 1)) == 0:
                path.append(i)
                backtrack(i, path)
                path.pop()

    result = []
    backtrack(1, [])
    min_diff = float('inf')
    best_combination = []

    for combination in result:
        diff = max(combination) - min(combination)
        if diff < min_diff:
            min_diff = diff
            best_combination = combination

    return best_combination


Solution = create_solution(solution_function_name)