# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1859
标题: Change Minimum Characters to Satisfy One of Three Conditions
难度: medium
链接: https://leetcode.cn/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/
题目类型: 哈希表、字符串、计数、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1737. 满足三条件之一需改变的最少字符数 - 给你两个字符串 a 和 b ，二者均由小写字母组成。一步操作中，你可以将 a 或 b 中的 任一字符 改变为 任一小写字母 。 操作的最终目标是满足下列三个条件 之一 ： * a 中的 每个字母 在字母表中 严格小于 b 中的 每个字母 。 * b 中的 每个字母 在字母表中 严格小于 a 中的 每个字母 。 * a 和 b 都 由 同一个 字母组成。 返回达成目标所需的 最少 操作数。 示例 1： 输入：a = "aba", b = "caa" 输出：2 解释：满足每个条件的最佳方案分别是： 1) 将 b 变为 "ccc"，2 次操作，满足 a 中的每个字母都小于 b 中的每个字母； 2) 将 a 变为 "bbb" 并将 b 变为 "aaa"，3 次操作，满足 b 中的每个字母都小于 a 中的每个字母； 3) 将 a 变为 "aaa" 并将 b 变为 "aaa"，2 次操作，满足 a 和 b 由同一个字母组成。 最佳的方案只需要 2 次操作（满足条件 1 或者条件 3）。 示例 2： 输入：a = "dabadd", b = "cda" 输出：3 解释：满足条件 1 的最佳方案是将 b 变为 "eee" 。 提示： * 1 <= a.length, b.length <= 105 * a 和 b 只由小写字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过计算字符频率并使用前缀和来找到满足三个条件所需的最少操作数。

算法步骤:
1. 计算字符串 a 和 b 的字符频率。
2. 使用前缀和数组来快速计算满足条件 1 和条件 2 所需的操作数。
3. 计算满足条件 3 所需的操作数。
4. 返回三个条件中的最小操作数。

关键点:
- 使用前缀和数组来优化计算过程。
- 通过比较字符频率来确定所需的操作数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是字符串 a 和 b 的长度。
空间复杂度: O(1)，因为字符频率数组和前缀和数组的大小都是固定的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_characters_to_satisfy_conditions(a: str, b: str) -> int:
    """
    函数式接口 - 计算满足三个条件之一所需的最少操作数
    """
    # 计算字符频率
    count_a = [0] * 26
    count_b = [0] * 26
    for char in a:
        count_a[ord(char) - ord('a')] += 1
    for char in b:
        count_b[ord(char) - ord('a')] += 1

    # 计算前缀和
    prefix_sum_a = [0] * 27
    prefix_sum_b = [0] * 27
    for i in range(26):
        prefix_sum_a[i + 1] = prefix_sum_a[i] + count_a[i]
        prefix_sum_b[i + 1] = prefix_sum_b[i] + count_b[i]

    # 计算满足条件 1 和条件 2 所需的操作数
    min_ops = float('inf')
    for i in range(25):
        ops1 = prefix_sum_a[i + 1] + (prefix_sum_b[26] - prefix_sum_b[i + 1])
        ops2 = prefix_sum_b[i + 1] + (prefix_sum_a[26] - prefix_sum_a[i + 1])
        min_ops = min(min_ops, ops1, ops2)

    # 计算满足条件 3 所需的操作数
    for i in range(26):
        ops3 = (prefix_sum_a[26] - count_a[i]) + (prefix_sum_b[26] - count_b[i])
        min_ops = min(min_ops, ops3)

    return min_ops


Solution = create_solution(min_characters_to_satisfy_conditions)