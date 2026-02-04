# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3143
标题: Longest Unequal Adjacent Groups Subsequence I
难度: easy
链接: https://leetcode.cn/problems/longest-unequal-adjacent-groups-subsequence-i/
题目类型: 贪心、数组、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2900. 最长相邻不相等子序列 I - 给定一个字符串数组 words ，和一个 二进制 数组 groups ，两个数组长度都是 n 。 如果 words 的一个 子序列 是交替的，那么对于序列中的任意两个连续字符串，它们在 groups 中相同索引的对应元素是 不同 的（也就是说，不能有连续的 0 或 1）， 你需要从 words 中选出 最长交替子序列。 返回选出的子序列。如果有多个答案，返回 任意 一个。 注意：words 中的元素是不同的 。 示例 1： 输入：words = ["e","a","b"], groups = [0,0,1] 输出：["e","b"] 解释：一个可行的子序列是 [0,2] ，因为 groups[0] != groups[2] 。 所以一个可行的答案是 [words[0],words[2]] = ["e","b"] 。 另一个可行的子序列是 [1,2] ，因为 groups[1] != groups[2] 。 得到答案为 [words[1],words[2]] = ["a","b"] 。 这也是一个可行的答案。 符合题意的最长子序列的长度为 2 。 示例 2： 输入：words = ["a","b","c","d"], groups = [1,0,1,1] 输出：["a","b","c"] 解释：一个可行的子序列为 [0,1,2] 因为 groups[0] != groups[1] 且 groups[1] != groups[2] 。 所以一个可行的答案是 [words[0],words[1],words[2]] = ["a","b","c"] 。 另一个可行的子序列为 [0,1,3] 因为 groups[0] != groups[1] 且 groups[1] != groups[3] 。 得到答案为 [words[0],words[1],words[3]] = ["a","b","d"] 。 这也是一个可行的答案。 符合题意的最长子序列的长度为 3 。 提示： * 1 <= n == words.length == groups.length <= 100 * 1 <= words[i].length <= 10 * groups[i] 是 0 或 1。 * words 中的字符串 互不相同 。 * words[i] 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，从左到右遍历数组，选择满足条件的最长子序列。

算法步骤:
1. 初始化结果列表 `result` 和上一个选中的组 `last_group`。
2. 遍历 `words` 和 `groups`，如果当前组与 `last_group` 不同，则将当前单词加入 `result` 并更新 `last_group`。
3. 返回 `result`。

关键点:
- 通过一次遍历即可找到最长的交替子序列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 words 的长度。
空间复杂度: O(1)，除了结果列表外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(words: List[str], groups: List[int]) -> List[str]:
    """
    函数式接口 - 实现最优解法
    """
    result = []
    last_group = None
    
    for i in range(len(words)):
        if last_group is None or groups[i] != last_group:
            result.append(words[i])
            last_group = groups[i]
    
    return result


Solution = create_solution(solution_function_name)