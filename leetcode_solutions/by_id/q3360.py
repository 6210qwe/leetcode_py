# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3360
标题: Minimum Deletions to Make String K-Special
难度: medium
链接: https://leetcode.cn/problems/minimum-deletions-to-make-string-k-special/
题目类型: 贪心、哈希表、字符串、计数、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3085. 成为 K 特殊字符串需要删除的最少字符数 - 给你一个字符串 word 和一个整数 k。 如果 |freq(word[i]) - freq(word[j])| <= k 对于字符串中所有下标 i 和 j 都成立，则认为 word 是 k 特殊字符串。 此处，freq(x) 表示字符 x 在 word 中的出现频率，而 |y| 表示 y 的绝对值。 返回使 word 成为 k 特殊字符串 需要删除的字符的最小数量。 示例 1： 输入：word = "aabcaba", k = 0 输出：3 解释：可以删除 2 个 "a" 和 1 个 "c" 使 word 成为 0 特殊字符串。word 变为 "baba"，此时 freq('a') == freq('b') == 2。 示例 2： 输入：word = "dabdcbdcdcd", k = 2 输出：2 解释：可以删除 1 个 "a" 和 1 个 "d" 使 word 成为 2 特殊字符串。word 变为 "bdcbdcdcd"，此时 freq('b') == 2，freq('c') == 3，freq('d') == 4。 示例 3： 输入：word = "aaabaaa", k = 2 输出：1 解释：可以删除 1 个 "b" 使 word 成为 2特殊字符串。因此，word 变为 "aaaaaa"，此时每个字母的频率都是 6。 提示： * 1 <= word.length <= 105 * 0 <= k <= 105 * word 仅由小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和计数来找到最小的删除次数。

算法步骤:
1. 统计每个字符的频率。
2. 将字符频率排序。
3. 从最高频率开始，尝试将其他频率调整到当前频率的范围内 [freq - k, freq + k]。
4. 计算需要删除的字符数，选择最小的删除次数。

关键点:
- 通过排序和贪心算法，确保每次调整都尽量减少删除次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是字符串的长度。排序操作的时间复杂度是 O(n log n)，统计频率和遍历操作是 O(n)。
空间复杂度: O(1)，因为只使用了常数级的额外空间（忽略输入输出）。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_deletions_to_make_k_special(word: str, k: int) -> int:
    """
    函数式接口 - 计算使字符串成为 k 特殊字符串需要删除的最少字符数
    """
    # 统计每个字符的频率
    freq = [0] * 26
    for char in word:
        freq[ord(char) - ord('a')] += 1
    
    # 去除频率为 0 的字符
    freq = [f for f in freq if f > 0]
    
    # 将字符频率排序
    freq.sort()
    
    # 计算最小删除次数
    min_deletions = float('inf')
    for i in range(len(freq)):
        target_freq = freq[i]
        deletions = 0
        for j in range(len(freq)):
            if freq[j] < target_freq - k:
                deletions += freq[j]
            elif freq[j] > target_freq + k:
                deletions += freq[j] - (target_freq + k)
        
        min_deletions = min(min_deletions, deletions)
    
    return min_deletions


Solution = create_solution(minimum_deletions_to_make_k_special)