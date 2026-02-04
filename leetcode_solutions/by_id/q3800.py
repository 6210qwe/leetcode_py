# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3800
标题: Longest Common Prefix Between Adjacent Strings After Removals
难度: medium
链接: https://leetcode.cn/problems/longest-common-prefix-between-adjacent-strings-after-removals/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3598. 相邻字符串之间的最长公共前缀 - 给你一个字符串数组 words，对于范围 [0, words.length - 1] 内的每个下标 i，执行以下步骤： * 从 words 数组中移除下标 i 处的元素。 * 计算修改后的数组中所有 相邻对 之间的 最长公共前缀 的长度。 返回一个数组 answer，其中 answer[i] 是移除下标 i 后，相邻对之间最长公共前缀的长度。如果 不存在 相邻对，或者 不存在 公共前缀，则 answer[i] 应为 0。 字符串的前缀是从字符串的开头开始延伸到任意位置的子字符串。 示例 1： 输入： words = ["jump","run","run","jump","run"] 输出： [3,0,0,3,3] 解释： * 移除下标 0： * words 变为 ["run", "run", "jump", "run"] * 最长的相邻对是 ["run", "run"]，其公共前缀为 "run"（长度为 3） * 移除下标 1： * words 变为 ["jump", "run", "jump", "run"] * 没有相邻对有公共前缀（长度为 0） * 移除下标 2： * words 变为 ["jump", "run", "jump", "run"] * 没有相邻对有公共前缀（长度为 0） * 移除下标 3： * words 变为 ["jump", "run", "run", "run"] * 最长的相邻对是 ["run", "run"]，其公共前缀为 "run"（长度为 3） * 移除下标 4： * words 变为 ["jump", "run", "run", "jump"] * 最长的相邻对是 ["run", "run"]，其公共前缀为 "run"（长度为 3） 示例 2： 输入： words = ["dog","racer","car"] 输出： [0,0,0] 解释： * 移除任意下标都会导致答案为 0。 提示： * 1 <= words.length <= 105 * 1 <= words[i].length <= 104 * words[i] 仅由小写英文字母组成。 * words[i] 的长度总和不超过 105。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 预计算每个相邻对的最长公共前缀。
2. 对于每个下标 i，移除该下标后，只需要考虑移除前后相邻对的变化。

算法步骤:
1. 计算原始数组中所有相邻对的最长公共前缀。
2. 对于每个下标 i，移除该下标后，更新相邻对的最长公共前缀。
3. 返回每个下标 i 移除后的最长公共前缀的最大值。

关键点:
- 使用预计算来减少重复计算。
- 通过动态更新相邻对的最长公共前缀来优化时间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 words 的长度，m 是单词的平均长度。
空间复杂度: O(n)，用于存储相邻对的最长公共前缀。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_common_prefix(s1: str, s2: str) -> int:
    """计算两个字符串的最长公共前缀长度"""
    min_len = min(len(s1), len(s2))
    for i in range(min_len):
        if s1[i] != s2[i]:
            return i
    return min_len


def solution_function_name(words: List[str]) -> List[int]:
    """
    函数式接口 - 实现
    """
    n = len(words)
    if n == 1:
        return [0]

    # 预计算所有相邻对的最长公共前缀
    lcp = [0] * (n - 1)
    for i in range(n - 1):
        lcp[i] = longest_common_prefix(words[i], words[i + 1])

    # 结果数组
    result = [0] * n

    # 处理第一个和最后一个元素
    result[0] = lcp[0]
    result[-1] = lcp[-1]

    # 处理中间元素
    for i in range(1, n - 1):
        result[i] = max(lcp[i - 1], lcp[i])

    return result


Solution = create_solution(solution_function_name)