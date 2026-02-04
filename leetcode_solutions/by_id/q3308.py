# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3308
标题: Apply Operations to Make String Empty
难度: medium
链接: https://leetcode.cn/problems/apply-operations-to-make-string-empty/
题目类型: 数组、哈希表、计数、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3039. 进行操作使字符串为空 - 给你一个字符串 s 。 请你进行以下操作直到 s 为 空 ： * 每次操作 依次 遍历 'a' 到 'z'，如果当前字符出现在 s 中，那么删除出现位置 最早 的该字符（如果存在的话）。 例如，最初 s = "aabcbbca"。我们执行下述操作： * 移除下划线的字符 s = "aabcbbca"。结果字符串为 s = "abbca"。 * 移除下划线的字符 s = "abbca"。结果字符串为 s = "ba"。 * 移除下划线的字符 s = "ba"。结果字符串为 s = ""。 请你返回进行 最后 一次操作 之前 的字符串 s 。在上面的例子中，答案是 "ba"。 示例 1： 输入：s = "aabcbbca" 输出："ba" 解释：已经在题目描述中解释。 示例 2： 输入：s = "abcd" 输出："abcd" 解释：我们进行以下操作： - 删除 s = "abcd" 中加粗加斜字符，得到字符串 s = "" 。 进行最后一次操作之前的字符串为 "abcd" 。 提示： * 1 <= s.length <= 5 * 105 * s 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个指针来追踪每个字符的最后出现位置，并使用一个集合来记录已经删除的字符。

算法步骤:
1. 初始化一个字典 `last_occurrence` 来记录每个字符的最后出现位置。
2. 从右到左遍历字符串 `s`，填充 `last_occurrence` 字典。
3. 初始化一个集合 `deleted_chars` 来记录已经删除的字符。
4. 从 'a' 到 'z' 遍历每个字符，如果字符在 `last_occurrence` 中且不在 `deleted_chars` 中，则将其从 `s` 中删除，并更新 `deleted_chars`。
5. 返回最后一次操作之前的字符串。

关键点:
- 使用字典记录每个字符的最后出现位置，以便快速查找。
- 使用集合记录已删除的字符，避免重复删除。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + 26) = O(n)，其中 n 是字符串 s 的长度。我们需要遍历字符串两次，一次是从右到左填充字典，另一次是从 'a' 到 'z' 遍历字符。
空间复杂度: O(26) = O(1)，因为字典和集合的大小都是常数级别的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(s: str) -> str:
    """
    函数式接口 - 实现最优解法
    """
    # 记录每个字符的最后出现位置
    last_occurrence = {}
    for i in range(len(s) - 1, -1, -1):
        if s[i] not in last_occurrence:
            last_occurrence[s[i]] = i

    # 记录已经删除的字符
    deleted_chars = set()

    # 从 'a' 到 'z' 遍历每个字符
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in last_occurrence and char not in deleted_chars:
            index = last_occurrence[char]
            s = s[:index] + s[index + 1:]
            deleted_chars.add(char)

    return s


Solution = create_solution(solution_function_name)