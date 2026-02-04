# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3210
标题: Count Beautiful Substrings I
难度: medium
链接: https://leetcode.cn/problems/count-beautiful-substrings-i/
题目类型: 哈希表、数学、字符串、枚举、数论、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2947. 统计美丽子字符串 I - 给你一个字符串 s 和一个正整数 k 。 用 vowels 和 consonants 分别表示字符串中元音字母和辅音字母的数量。 如果某个字符串满足以下条件，则称其为 美丽字符串 ： * vowels == consonants，即元音字母和辅音字母的数量相等。 * (vowels * consonants) % k == 0，即元音字母和辅音字母的数量的乘积能被 k 整除。 返回字符串 s 中 非空美丽子字符串 的数量。 子字符串是字符串中的一个连续字符序列。 英语中的 元音字母 为 'a'、'e'、'i'、'o' 和 'u' 。 英语中的 辅音字母 为除了元音字母之外的所有字母。 示例 1： 输入：s = "baeyh", k = 2 输出：2 解释：字符串 s 中有 2 个美丽子字符串。 - 子字符串 "baeyh"，vowels = 2（["a","e"]），consonants = 2（["y","h"]）。 可以看出字符串 "aeyh" 是美丽字符串，因为 vowels == consonants 且 vowels * consonants % k == 0 。 - 子字符串 "baeyh"，vowels = 2（["a","e"]），consonants = 2（["b","y"]）。 可以看出字符串 "baey" 是美丽字符串，因为 vowels == consonants 且 vowels * consonants % k == 0 。 可以证明字符串 s 中只有 2 个美丽子字符串。 示例 2： 输入：s = "abba", k = 1 输出：3 解释：字符串 s 中有 3 个美丽子字符串。 - 子字符串 "abba"，vowels = 1（["a"]），consonants = 1（["b"]）。 - 子字符串 "abba"，vowels = 1（["a"]），consonants = 1（["b"]）。 - 子字符串 "abba"，vowels = 2（["a","a"]），consonants = 2（["b","b"]）。 可以证明字符串 s 中只有 3 个美丽子字符串。 示例 3： 输入：s = "bcdf", k = 1 输出：0 解释：字符串 s 中没有美丽子字符串。 提示： * 1 <= s.length <= 1000 * 1 <= k <= 1000 * s 仅由小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和来记录每个位置的元音和辅音数量，并使用哈希表来记录不同前缀和出现的位置。

算法步骤:
1. 初始化前缀和数组 `prefix_sum` 和哈希表 `prefix_count`。
2. 遍历字符串 `s`，更新前缀和数组 `prefix_sum`。
3. 对于每个位置 `i`，检查是否存在之前的前缀和 `j` 满足 `(prefix_sum[i] - prefix_sum[j]) % 2 == 0` 且 `(prefix_sum[i] - prefix_sum[j]) // 2 * (prefix_sum[i] - prefix_sum[j]) // 2 % k == 0`。
4. 更新哈希表 `prefix_count`，记录当前前缀和出现的位置。

关键点:
- 使用前缀和来快速计算任意子字符串的元音和辅音数量。
- 使用哈希表来记录前缀和出现的位置，以便快速查找。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_beautiful_substrings(s: str, k: int) -> int:
    n = len(s)
    vowels = set('aeiou')
    prefix_sum = [0] * (n + 1)
    prefix_count = {}
    result = 0

    for i in range(1, n + 1):
        if s[i - 1] in vowels:
            prefix_sum[i] = prefix_sum[i - 1] + 1
        else:
            prefix_sum[i] = prefix_sum[i - 1] - 1

        current_sum = prefix_sum[i]
        if current_sum not in prefix_count:
            prefix_count[current_sum] = []

        for j in prefix_count[current_sum]:
            length = i - j
            if (length // 2) * (length // 2) % k == 0:
                result += 1

        prefix_count[current_sum].append(i)

    return result


Solution = create_solution(count_beautiful_substrings)