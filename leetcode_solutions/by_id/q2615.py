# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2615
标题: Make Number of Distinct Characters Equal
难度: medium
链接: https://leetcode.cn/problems/make-number-of-distinct-characters-equal/
题目类型: 哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2531. 使字符串中不同字符的数目相等 - 给你两个下标从 0 开始的字符串 word1 和 word2 。 一次 移动 由以下两个步骤组成： * 选中两个下标 i 和 j ，分别满足 0 <= i < word1.length 和 0 <= j < word2.length ， * 交换 word1[i] 和 word2[j] 。 如果可以通过 恰好一次 移动，使 word1 和 word2 中不同字符的数目相等，则返回 true ；否则，返回 false 。 示例 1： 输入：word1 = "ac", word2 = "b" 输出：false 解释：交换任何一组下标都会导致第一个字符串中有 2 个不同的字符，而在第二个字符串中只有 1 个不同字符。 示例 2： 输入：word1 = "abcc", word2 = "aab" 输出：true 解释：交换第一个字符串的下标 2 和第二个字符串的下标 0 。之后得到 word1 = "abac" 和 word2 = "cab" ，各有 3 个不同字符。 示例 3： 输入：word1 = "abcde", word2 = "fghij" 输出：true 解释：无论交换哪一组下标，两个字符串中都会有 5 个不同字符。 提示： * 1 <= word1.length, word2.length <= 105 * word1 和 word2 仅由小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过交换一个字符来使两个字符串的不同字符数量相等。我们需要检查每个可能的交换，并计算交换后的不同字符数量。

算法步骤:
1. 计算初始状态下 word1 和 word2 的不同字符数量。
2. 遍历所有可能的字符对 (c1, c2)，其中 c1 来自 word1，c2 来自 word2。
3. 对于每一对字符，模拟交换后的情况，更新不同字符的数量。
4. 如果交换后的不同字符数量相等，则返回 True。
5. 如果遍历完所有可能的交换后仍未找到符合条件的交换，则返回 False。

关键点:
- 使用 Counter 来高效地计算和更新不同字符的数量。
- 通过模拟交换来避免实际修改字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是 word1 和 word2 的长度。我们只需要遍历每个字符串一次来计算初始的不同字符数量，然后遍历所有可能的字符对。
空间复杂度: O(1)，因为我们只使用了常数级的额外空间来存储不同字符的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from collections import Counter

def solution_function_name(word1: str, word2: str) -> bool:
    """
    函数式接口 - 通过一次交换使两个字符串的不同字符数量相等
    """
    # 计算初始的不同字符数量
    counter1 = Counter(word1)
    counter2 = Counter(word2)
    distinct1 = len(counter1)
    distinct2 = len(counter2)
    
    # 遍历所有可能的字符对
    for c1 in counter1:
        for c2 in counter2:
            new_distinct1 = distinct1 - (counter1[c1] == 1) + (c2 not in counter1)
            new_distinct2 = distinct2 - (counter2[c2] == 1) + (c1 not in counter2)
            if new_distinct1 == new_distinct2:
                return True
    
    return False

Solution = create_solution(solution_function_name)