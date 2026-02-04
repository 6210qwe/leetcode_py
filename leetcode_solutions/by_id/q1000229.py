# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000229
标题: 组合总和
难度: medium
链接: https://leetcode.cn/problems/Ygoe9J/
题目类型: 数组、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 081. 组合总和 - 给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。 candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是不同的。 对于给定的输入，保证和为 target 的唯一组合数少于 150 个。 示例 1： 输入: candidates = [2,3,6,7], target = 7< 输出: [[7],[2,2,3]] 示例 2： 输入: candidates = [2,3,5], target = 8 输出: [[2,2,2,2],[2,3,3],[3,5]] 示例 3： 输入: candidates = [2], target = 1 输出: [] 示例 4： 输入: candidates = [1], target = 1 输出: [[1]] 示例 5： 输入: candidates = [1], target = 2 输出: [[1,1]] 提示： * 1 <= candidates.length <= 30 * 1 <= candidates[i] <= 200 * candidate 中的每个元素都是独一无二的。 * 1 <= target <= 500 注意：本题与主站 39 题相同： https://leetcode.cn/problems/combination-sum/ [https://leetcode.cn/problems/combination-sum/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法来找到所有可能的组合。

算法步骤:
1. 定义一个递归函数 `backtrack`，该函数接受当前组合 `path`、当前目标值 `remaining` 和当前起始索引 `start` 作为参数。
2. 如果 `remaining` 等于 0，说明找到了一个有效的组合，将其加入结果列表 `result` 中。
3. 如果 `remaining` 小于 0，直接返回，因为不可能再找到有效的组合。
4. 从 `start` 开始遍历 `candidates`，对于每个候选数，将其加入当前组合 `path`，并递归调用 `backtrack` 函数。
5. 递归调用结束后，移除当前组合 `path` 中的最后一个元素，继续尝试下一个候选数。

关键点:
- 使用回溯法，通过递归和剪枝来找到所有可能的组合。
- 通过 `start` 参数来避免重复组合。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^t)，其中 t 是 target 的值。在最坏情况下，每个数字都可以选择或不选择，因此时间复杂度为指数级。
空间复杂度: O(t)，递归调用栈的深度最多为 target 的值。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(path, remaining, start):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(path, remaining - candidates[i], i)
            path.pop()

    result = []
    backtrack([], target, 0)
    return result


Solution = create_solution(combination_sum)